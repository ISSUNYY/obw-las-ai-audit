"""Inicia o fiscal da Luna a partir da pasta de scripts do projeto."""

from __future__ import annotations

import sys
from importlib import import_module
from pathlib import Path


def run() -> int:
    """Carrega o código do projeto e encaminha os argumentos da linha de comando."""

    source = Path(__file__).resolve().parents[1] / "src"
    source_text = str(source)
    if source_text not in sys.path:
        sys.path.insert(0, source_text)
    project_guard = import_module("obw.project_guard")
    return int(project_guard.main())


if __name__ == "__main__":
    raise SystemExit(run())
