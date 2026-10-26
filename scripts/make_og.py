#!/usr/bin/env python3
"""Генератор OG-картинок 1200×630 в фирменном стиле «НЕО КОНСАЛТИНГ».

Требует Pillow (`pip install pillow`) и системный шрифт DejaVu Sans (обычно
лежит в `/usr/share/fonts/truetype/dejavu/`). Скрипт применяется только при
добавлении новых страниц — в CI он не нужен, готовые JPG лежат в
`assets/img/og/`.

Запуск:
    python3 scripts/make_og.py smena-buhgaltera
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")

BG = (15, 15, 26)
SURFACE = (251, 251, 249)
INK_SOFT = (184, 189, 208)
ACCENT = (46, 94, 78)
GOLD = (232, 185, 49)

# slug -> (заголовок, золотой подзаголовок, подпись слева внизу)
CARDS = {
    "smena-buhgaltera": (
        "Как сменить бухгалтера",
        "Передача учёта без штрафов и потерь",
        "Практика · Аутсорсинг и учёт в 2026 году",
    ),
    "shtatny-buhgalter-ili-autsorsing": (
        "Штатный бухгалтер\nили аутсорсинг",
        "Как выбрать для ИП и ООО на УСН",
        "Практика · Стоимость и риски учёта",
    ),
    "zarplata-i-kadry": (
        "Зарплата и кадры",
        "Расчёт, НДФЛ, взносы и отчётность",
        "Практика · Зарплатный участок в 2026",
    ),
    "registraciya-i-zakrytie": (
        "Регистрация и закрытие",
        "ИП и ООО: документы и сроки",
        "Практика · Старт и закрытие бизнеса",
    ),
    "avtonomnaya-nekommercheskaya-organizaciya": (
        "АНО: налоги и учёт",
        "Целевые поступления, гранты, отчётность",
        "Право · Некоммерческие организации",
    ),
    "osno": (
        "ОСНО: общая система",
        "НДС, прибыль и переход с УСН",
        "Налоги · Режим учёта в 2026 году",
    ),
}


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_DIR / name), size)


def render(slug: str) -> Path:
    title, subtitle, caption = CARDS[slug]
    img = Image.new("RGB", (1200, 630), BG)
    d = ImageDraw.Draw(img)

    # левая акцентная полоса
    d.rectangle([0, 0, 12, 630], fill=ACCENT)

    # бейдж «НК»
    d.rounded_rectangle([72, 52, 136, 116], radius=12, fill=ACCENT)
    badge_font = font("DejaVuSans-Bold.ttf", 30)
    tw = d.textlength("НК", font=badge_font)
    d.text((104 - tw / 2, 70), "НК", font=badge_font, fill=SURFACE)

    # название и подпись
    d.text((160, 56), "НЕО КОНСАЛТИНГ", font=font("DejaVuSans-Bold.ttf", 34), fill=SURFACE)
    d.text((160, 100), "бухгалтерский аутсорсинг · Санкт-Петербург",
           font=font("DejaVuSans.ttf", 24), fill=INK_SOFT)

    # заголовок (с переносами из \n)
    title_font = font("DejaVuSans-Bold.ttf", 62)
    y = 236
    for line in title.split("\n"):
        d.text((72, y), line, font=title_font, fill=SURFACE)
        y += 78

    # золотая линия
    d.rectangle([72, y + 6, 180, y + 14], fill=GOLD)

    # золотой подзаголовок
    d.text((72, y + 44), subtitle, font=font("DejaVuSans-Bold.ttf", 34), fill=GOLD)

    # нижняя подпись
    d.text((72, 566), caption, font=font("DejaVuSans.ttf", 22), fill=INK_SOFT)

    # правый нижний бренд с золтым подчёркиванием
    brand = "НЕО КОНСАЛТИНГ"
    brand_font = font("DejaVuSans-Bold.ttf", 26)
    bw = d.textlength(brand, font=brand_font)
    d.text((1128 - bw, 552), brand, font=brand_font, fill=SURFACE)
    d.rectangle([1128 - bw, 586, 1128, 591], fill=GOLD)

    out = ROOT / "assets" / "img" / "og" / f"og-{slug}.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "JPEG", quality=88, optimize=True, progressive=True)
    return out


def main() -> int:
    slugs = sys.argv[1:] or list(CARDS)
    for slug in slugs:
        if slug not in CARDS:
            print(f"нет описания для {slug}")
            return 1
        path = render(slug)
        print(f"{path.relative_to(ROOT)} ({path.stat().st_size // 1024} КБ)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
