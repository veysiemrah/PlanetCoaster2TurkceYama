"""cobra-tools subprocess sarmalayıcısı.

cobra-tools'u Python modülü olarak import etmek yerine, kendi CLI'sını (ovl_tool_cmd.py)
subprocess olarak çağırıyoruz. Bu, cobra-tools'un iç bağımlılıklarından (PyQt5, gui vb.)
ve circular import sorunlarından bizi korur.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
COBRA_DIR = REPO_ROOT / "cobra-tools"
COBRA_CMD = COBRA_DIR / "ovl_tool_cmd.py"
GAME_NAME = "Planet Coaster 2"


def _run_cobra(args: list[str]) -> None:
    """cobra-tools CLI'sını çağır."""
    if not COBRA_CMD.exists():
        raise FileNotFoundError(
            f"cobra-tools bulunamadı: {COBRA_CMD}\n"
            "Kurulum için docs/DEVELOPMENT.md dosyasına bak."
        )
    full_args = [sys.executable, str(COBRA_CMD), *args]
    result = subprocess.run(
        full_args,
        cwd=str(COBRA_DIR),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"cobra-tools başarısız (exit={result.returncode}):\n"
            f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )


def extract_ovl_txt(ovl_path: Path, out_dir: Path) -> dict[str, str]:
    """Bir Loc.ovl dosyasındaki tüm .txt stringlerini çıkarır.

    Args:
        ovl_path: Kaynak .ovl dosyası yolu.
        out_dir: Geçici extract dizini (temizlenmez).

    Returns:
        {string_id: metin} dictionary'si.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    # Subprocess cobra-tools dizininde çalışır, bu yüzden relative path'ler bozulur.
    # Tüm yolları absolute'a çevir.
    _run_cobra([
        "extract",
        str(Path(ovl_path).resolve()),
        "-o", str(out_dir.resolve()),
        "-g", GAME_NAME,
        "--type", ".txt",
    ])

    entries: dict[str, str] = {}
    for txt in out_dir.rglob("*.txt"):
        name = txt.stem
        try:
            content = txt.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = txt.read_text(encoding="latin-1")
        entries[name] = content

    return entries


def build_ovl_from_dir(input_dir: Path, output_ovl: Path, *, force: bool = True) -> None:
    """Bir dizindeki dosyalardan yeni bir OVL oluşturur.

    Args:
        input_dir: Dosyaların bulunduğu dizin (OVL içi yapıyla aynı olmalı).
        output_ovl: Çıkış .ovl dosyası yolu.
        force: True ise mevcut dosyanın üzerine yaz.
    """
    output_ovl.parent.mkdir(parents=True, exist_ok=True)
    # Subprocess cobra-tools dizininde çalışır — absolute path zorunlu.
    args = [
        "new",
        "-g", GAME_NAME,
        "-i", str(Path(input_dir).resolve()),
        "-o", str(Path(output_ovl).resolve()),
    ]
    if force:
        args.append("-f")
    _run_cobra(args)
