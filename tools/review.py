"""
Çeviri kalite kontrol aracı.

Kullanım:
  python review.py                     # Tüm kategorileri listele
  python review.py hud                 # Belirli kategoriyi incele
  python review.py hud --output md     # Markdown dosyasına dışa aktar
  python review.py hud --find "Park"   # Belirli metni ara
"""
import json
import sys
import re
from pathlib import Path

TR_JSON = Path("../translations/Content0/tr.json")
REVIEW_DIR = Path("../reviews")


def load_data():
    return json.loads(TR_JSON.read_text(encoding="utf-8"))


def save_data(data):
    TR_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def list_categories(data):
    cats = {}
    for key, entry in data["strings"].items():
        cat = entry.get("category", "")
        status = entry.get("status", "pending")
        if cat not in cats:
            cats[cat] = {"translated": 0, "pending": 0, "total": 0}
        cats[cat]["total"] += 1
        if status == "translated":
            cats[cat]["translated"] += 1
        else:
            cats[cat]["pending"] += 1

    print("\n=== KATEGORI DURUMU ===\n")
    total_t = sum(c["translated"] for c in cats.values())
    total_all = sum(c["total"] for c in cats.values())
    print(f"GENEL: {total_t}/{total_all} ({total_t*100//total_all}%)\n")

    for cat, c in sorted(cats.items()):
        if not cat:
            cat_label = "(kategorisiz)"
        else:
            cat_label = cat
        pct = c["translated"] * 100 // c["total"]
        bar = "#" * (pct // 5)
        print(f"  {cat_label:<32} {c['translated']:>5}/{c['total']:<5} {pct:>3}%  [{bar:<20}]")


def review_category(data, category, output_format=None, search=None):
    strings = data["strings"]
    results = []

    for key, entry in strings.items():
        if entry.get("category") != category:
            continue
        src = entry.get("source", "")
        tr = entry.get("translation", "")
        status = entry.get("status", "pending")
        if search and search.lower() not in src.lower() and search.lower() not in tr.lower():
            continue
        results.append((key, src, tr, status))

    if not results:
        print(f"Kategori bulunamadi veya bos: {category}")
        return

    if output_format == "md":
        REVIEW_DIR.mkdir(exist_ok=True)
        out_path = REVIEW_DIR / f"{category}_review.md"
        lines = [f"# {category} Çeviri İncelemesi\n\n"]
        lines.append(f"Toplam: {len(results)} string\n\n")
        lines.append("| Key | İngilizce | Türkçe | Durum |\n")
        lines.append("|-----|-----------|--------|-------|\n")
        for key, src, tr, status in results:
            flag = "✓" if status == "translated" else "⏳"
            src_esc = src.replace("|", "\\|").replace("\n", " ")
            tr_esc = tr.replace("|", "\\|").replace("\n", " ") if tr else "—"
            lines.append(f"| `{key}` | {src_esc} | {tr_esc} | {flag} |\n")
        out_path.write_text("".join(lines), encoding="utf-8")
        print(f"Markdown inceleme dosyasi: {out_path}")
    else:
        print(f"\n=== {category.upper()} ({len(results)} string) ===\n")
        for key, src, tr, status in results:
            flag = "[OK]" if status == "translated" else "[--]"
            print(f"{flag} {key}")
            print(f"     EN: {src[:80]}")
            if tr:
                print(f"     TR: {tr[:80]}")
            print()


def fix_translation(key, new_tr):
    """Belirli bir string'in çevirisini düzelt."""
    data = load_data()
    if key not in data["strings"]:
        print(f"Key bulunamadi: {key}")
        return
    data["strings"][key]["translation"] = new_tr
    data["strings"][key]["status"] = "translated"
    save_data(data)
    print(f"Guncellendi: {key}")
    print(f"  Yeni: {new_tr}")


def show_stats(data):
    list_categories(data)


if __name__ == "__main__":
    args = sys.argv[1:]
    data = load_data()

    if not args:
        show_stats(data)
        sys.exit(0)

    category = args[0]
    output_fmt = None
    search = None

    if "--output" in args:
        idx = args.index("--output")
        output_fmt = args[idx + 1]
    if "--find" in args:
        idx = args.index("--find")
        search = args[idx + 1]
    if "--fix" in args:
        idx = args.index("--fix")
        key = args[idx + 1]
        new_tr = args[idx + 2]
        fix_translation(key, new_tr)
        sys.exit(0)

    review_category(data, category, output_format=output_fmt, search=search)
