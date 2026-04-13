# Geliştirme Rehberi

## Gereksinimler
- Python 3.10+
- Git

## Kurulum

```bash
python -m venv venv
source venv/Scripts/activate  # Windows (bash)
# veya: venv\Scripts\activate.bat  # Windows (cmd)

git clone https://github.com/OpenNaja/cobra-tools.git
./venv/Scripts/python.exe -m pip install "imageio>=2.26.0" "numpy>=1.26.4,<2.0.0" "pillow>=10.0.1" "bitarray~=2.9.2" "PyQt5~=5.15.4" vdf mouse
./venv/Scripts/python.exe -m pip install -r requirements.txt
```

### cobra-tools Patch

Python 3.12 ve yeni sürümlerde cobra-tools'ta circular import bug'ı var.
`cobra-tools/modules/formats/utils/__init__.py` içinde `from gui.app_utils import WINDOWS_WINE`
satırı modül seviyesinden fonksiyon içine taşınmalı:

```python
def check_call_smart(args: list[str]):
    from gui.app_utils import WINDOWS_WINE  # lazy import
    ...

def prep_arg(arg: str):
    from gui.app_utils import WINDOWS_WINE  # lazy import
    ...
```

## Araçlar

- `python tools/extract.py` — OVL'den JSON çıkart
- `python tools/validate.py` — çeviri doğrula
- `python tools/build.py` — JSON'dan OVL yap

## Test

```bash
pytest tests/
```
