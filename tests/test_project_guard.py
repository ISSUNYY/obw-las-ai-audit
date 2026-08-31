"""Testes do controle de formatação e privacidade do projeto."""

import unittest

from obw.project_guard import check_text, is_forbidden_path, validate_gemini_result


class ProjectGuardTests(unittest.TestCase):
    def test_rejects_private_and_reference_paths(self) -> None:
        self.assertTrue(is_forbidden_path("Documentos de Referêcia/data/example.las"))
        self.assertTrue(is_forbidden_path("outputs/report.json"))
        self.assertTrue(is_forbidden_path("paper.pdf"))
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

    def test_rejects_gemini_path_that_was_not_sent(self) -> None:
        result = {
            "approved": True,
            "mepa_score": 12,
            "zero_criteria": [],
            "issues": [
                {
                    "path": "private.txt",
                    "severity": "aviso",
                    "rule": "clareza",
                    "explanation": "Exemplo.",
                    "suggestion": "Revisar.",
                }
            ],
            "summary": "Aprovado.",
        }
        errors = validate_gemini_result(result, {"README.md"})
        self.assertTrue(any("caminho não enviado" in error for error in errors))

    def test_accepts_well_formed_gemini_result(self) -> None:
        result = {
            "approved": True,
            "mepa_score": 12,
            "zero_criteria": [],
            "issues": [],
            "summary": "Aprovado.",
        }
        self.assertEqual(validate_gemini_result(result, {"README.md"}), [])


if __name__ == "__main__":
    unittest.main()
