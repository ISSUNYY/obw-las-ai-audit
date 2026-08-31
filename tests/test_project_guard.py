"""Testes do controle de organização, formatação e privacidade do projeto."""

import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from typing import Self
from unittest.mock import Mock, patch

from obw.project_guard import (
    call_luna,
    check_text,
    is_forbidden_path,
    run_git,
    validate_luna_result,
)


class ProjectGuardTests(unittest.TestCase):
    def test_git_commands_do_not_open_a_window(self) -> None:
        completed = Mock(returncode=0, stdout=b"", stderr=b"")
        with patch("obw.project_guard.subprocess.run", return_value=completed) as mocked:
            run_git(["status"], cwd=Path.cwd())

        expected = getattr(subprocess, "CREATE_NO_WINDOW", 0)
        self.assertEqual(mocked.call_args.kwargs["creationflags"], expected)

    def test_rejects_private_and_reference_paths(self) -> None:
        self.assertTrue(is_forbidden_path("Documentos de Referêcia/data/example.las"))
        self.assertTrue(is_forbidden_path("outputs/report.json"))
        self.assertTrue(is_forbidden_path("paper.pdf"))
        self.assertTrue(is_forbidden_path(".env"))
        self.assertTrue(is_forbidden_path("config/.env.local"))
        self.assertTrue(is_forbidden_path("private-key.pem"))
        self.assertTrue(is_forbidden_path("tests/fixtures/paper.pdf"))
        self.assertFalse(is_forbidden_path("outputs/.gitkeep"))
        self.assertFalse(is_forbidden_path("tests/fixtures/synthetic.las"))
        self.assertFalse(is_forbidden_path("tests/fixtures/synthetic.las.json"))

    def test_detects_markdown_formatting_errors(self) -> None:
        content = b"# Titulo\nTexto com espaco. \n"
        errors = check_text("docs/exemplo.md", content)
        self.assertTrue(any("linha vazia" in error for error in errors))
        self.assertTrue(any("fim da linha" in error for error in errors))

    def test_accepts_valid_markdown(self) -> None:
        content = b"# Titulo\n\nTexto curto.\n"
        self.assertEqual(check_text("docs/exemplo.md", content), [])

    def review_result(self) -> dict[str, object]:
        """Cria um parecer mínimo válido da Luna."""

        return {
            "approved": True,
            "mepa_score": 12,
            "zero_criteria": [],
            "issues": [],
            "file_recommendations": [],
            "summary": "Aprovado.",
        }

    def test_rejects_luna_path_that_was_not_sent(self) -> None:
        result = {
            **self.review_result(),
            "issues": [
                {
                    "path": "private.txt",
                    "severity": "aviso",
                    "rule": "clareza",
                    "explanation": "Exemplo.",
                    "suggestion": "Revisar.",
                }
            ],
        }
        errors = validate_luna_result(result, {"README.md"})
        self.assertTrue(any("caminho não enviado" in error for error in errors))

    def test_rejects_removal_without_two_evidences(self) -> None:
        result = self.review_result()
        result["file_recommendations"] = [
            {
                "path": "tests/test_old.py",
                "action": "revisar_remocao",
                "category": "teste_obsoleto",
                "confidence": "alta",
                "evidence": ["Não há importações."],
                "explanation": "Pode estar obsoleto.",
                "target": "",
            }
        ]
        errors = validate_luna_result(result, {"tests/test_old.py"})
        self.assertTrue(any("duas evidências" in error for error in errors))

    def test_accepts_well_formed_luna_result(self) -> None:
        self.assertEqual(validate_luna_result(self.review_result(), {"README.md"}), [])

    def test_luna_request_disables_storage_and_uses_structured_output(self) -> None:
        response_payload = {
            "output": [
                {
                    "type": "message",
                    "content": [
                        {
                            "type": "output_text",
                            "text": json.dumps(self.review_result()),
                        }
                    ],
                }
            ]
        }

        class Response:
            def __enter__(self) -> Self:
                return self

            def __exit__(self, *args: object) -> None:
                return None

            def read(self) -> bytes:
                return json.dumps(response_payload).encode("utf-8")

        captured: dict[str, object] = {}

        def fake_urlopen(http_request: object, timeout: float) -> Response:
            captured["request"] = http_request
            captured["timeout"] = timeout
            return Response()

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs" / "GUIA_DE_ESCRITA.md").write_text(
                "# Guia\n\nTexto.\n", encoding="utf-8"
            )
            with patch("obw.project_guard.request.urlopen", fake_urlopen):
                result = call_luna(
                    root,
                    {"README.md": "# Projeto\n\nExecute scripts/luna.py.\n"},
                    "segredo",
                    inventory_paths=[
                        ".githooks/pre-commit",
                        "README.md",
                        "scripts/luna.py",
                    ],
                )

        sent = json.loads(captured["request"].data.decode("utf-8"))
        self.assertFalse(sent["store"])
        self.assertEqual(sent["model"], "gpt-5.6-luna")
        self.assertEqual(sent["text"]["format"]["type"], "json_schema")
        self.assertIn(".githooks/pre-commit", sent["input"])
        self.assertIn("scripts/luna.py: função estrutural", sent["input"])
        self.assertIn("referenciado por: README.md", sent["input"])
        self.assertNotIn("segredo", sent)
        self.assertEqual(result, self.review_result())


if __name__ == "__main__":
    unittest.main()
