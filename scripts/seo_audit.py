#!/usr/bin/env python3
"""SEO/социальный аудит статического сайта «НЕО КОНСАЛТИНГ».

Проверяет каждую HTML-страницу по чек-листу поисковой и социальной оптимизации
и сверяет служебные файлы (sitemap.xml, robots.txt, feed.xml).

Запуск:
    python3 scripts/seo_audit.py            # отчёт + код выхода 1 при ошибках
    python3 scripts/seo_audit.py --verbose  # с детализацией по каждой странице
    python3 scripts/seo_audit.py --json     # машиночитаемый отчёт

Правила намеренно жёсткие: длина title 30–70 символов, description 70–175,
обязательные OG/Twitter-теги, валидный JSON-LD, отсутствие внешних подресурсов
(шрифты/CDN), канонизация внутренних ссылок, полнота sitemap.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://bestdeejay-design.github.io/neo-consulting/"
HOST = urlparse(BASE).netloc

# Страницы, которые обязаны быть в индексе и в sitemap
PUBLIC_PAGES = [
    "index.html",
    "materials/index.html",
    "materials/nds-usn-2026.html",
    "materials/calendar-2026.html",
    "materials/ip-vznosy-2026.html",
    "materials/usn-object.html",
    "materials/amnistia.html",
    "materials/etrn-guide.html",
    "materials/1c-automation-guide.html",
    "materials/smena-buhgaltera.html",
    "materials/shtatny-buhgalter-ili-autsorsing.html",
    "materials/zarplata-i-kadry.html",
    "materials/registraciya-i-zakrytie.html",
    "materials/avtonomnaya-nekommercheskaya-organizaciya.html",
    "materials/osno.html",
]
# Страницы, которые в индекс попадать не должны (служебные)
NOINDEX_PAGES = ["presentation/index.html"]

TITLE_MIN, TITLE_MAX = 30, 70
DESC_MIN, DESC_MAX = 70, 175

# Внешние подресурсы, которых быть не должно (локальный сайт без CDN)
FORBIDDEN_HOSTS = (
    "fonts.googleapis.com",
    "fonts.gstatic.com",
    "cdn.jsdelivr.net",
    "unpkg.com",
    "google-analytics.com",
    "googletagmanager.com",
    "mc.yandex.ru",
)


class Report:
    def __init__(self) -> None:
        self.items: list[dict] = []

    def add(self, page: str, check: str, level: str, message: str) -> None:
        self.items.append({"page": page, "check": check, "level": level, "message": message})

    def ok(self, page: str, check: str) -> None:
        self.add(page, check, "ok", "")

    def fail(self, page: str, check: str, message: str) -> None:
        self.add(page, check, "error", message)

    def warn(self, page: str, check: str, message: str) -> None:
        self.add(page, check, "warn", message)

    @property
    def errors(self) -> list[dict]:
        return [i for i in self.items if i["level"] == "error"]

    @property
    def warnings(self) -> list[dict]:
        return [i for i in self.items if i["level"] == "warn"]


def expected_url(path: str) -> str:
    """Канонический URL страницы в опубликованном виде."""
    if path.endswith("index.html"):
        return BASE + path[: -len("index.html")]
    return BASE + path


def strip_code(source: str) -> str:
    source = re.sub(r"(?s)<script.*?</script>", " ", source)
    source = re.sub(r"(?s)<style.*?</style>", " ", source)
    return re.sub(r"<[^>]+>", " ", source)


def check_page(rep: Report, rel: str) -> str:
    page = rel
    path = ROOT / rel
    if not path.exists():
        rep.fail(page, "exists", "файл страницы отсутствует")
        return ""
    source = path.read_text(encoding="utf-8")

    # --- lang ---
    m = re.search(r"<html[^>]*\blang=\"([^\"]+)\"", source)
    if not m:
        rep.fail(page, "lang", "у <html> нет атрибута lang")
    elif not m.group(1).lower().startswith("ru"):
        rep.fail(page, "lang", f"lang=\"{m.group(1)}\", ожидается ru")
    else:
        rep.ok(page, "lang")

    # --- title ---
    m = re.search(r"(?s)<title>(.*?)</title>", source)
    if not m:
        rep.fail(page, "title", "нет <title>")
    else:
        title = html.unescape(m.group(1).strip())
        if len(title) < TITLE_MIN:
            rep.warn(page, "title", f"{len(title)} симв. — короткий (<{TITLE_MIN}): {title}")
        elif len(title) > TITLE_MAX:
            rep.fail(page, "title", f"{len(title)} симв. — обрежется в выдаче (>{TITLE_MAX}): {title}")
        else:
            rep.ok(page, "title")

    # --- description ---
    m = re.search(r'<meta name="description" content="(.*?)"', source)
    if not m:
        rep.fail(page, "description", "нет meta description")
    else:
        desc = html.unescape(m.group(1))
        if len(desc) < DESC_MIN:
            rep.warn(page, "description", f"{len(desc)} симв. — короткое (<{DESC_MIN})")
        elif len(desc) > DESC_MAX:
            rep.warn(page, "description", f"{len(desc)} симв. — обрежется (>{DESC_MAX})")
        else:
            rep.ok(page, "description")

    # --- canonical ---
    m = re.search(r'<link rel="canonical" href="([^"]+)"', source)
    if not m:
        rep.fail(page, "canonical", "нет rel=canonical")
    elif m.group(1) != expected_url(rel):
        rep.fail(page, "canonical", f"canonical={m.group(1)}, ожидается {expected_url(rel)}")
    else:
        rep.ok(page, "canonical")

    # --- robots ---
    m = re.search(r'<meta name="robots" content="([^"]+)"', source)
    robots = m.group(1).lower() if m else ""
    if rel in NOINDEX_PAGES:
        if "noindex" in robots:
            rep.ok(page, "robots")
        else:
            rep.fail(page, "robots", "служебная страница не закрыта от индексации (нет noindex)")
    else:
        if "noindex" in robots:
            rep.fail(page, "robots", "страница закрыта от индексации, но должна быть в поиске")
        else:
            rep.ok(page, "robots")

    # --- Open Graph / Twitter ---
    og_required = ["og:type", "og:title", "og:description", "og:url", "og:image", "og:image:alt"]
    missing = [t for t in og_required if f'property="{t}"' not in source]
    if missing:
        rep.fail(page, "open-graph", "нет: " + ", ".join(missing))
    else:
        rep.ok(page, "open-graph")

    tw_required = ["twitter:card", "twitter:title", "twitter:description", "twitter:image"]
    missing = [t for t in tw_required if f'name="{t}"' not in source]
    if missing:
        rep.warn(page, "twitter", "нет: " + ", ".join(missing))
    else:
        rep.ok(page, "twitter")

    m = re.search(r'property="og:image" content="([^"]+)"', source)
    if m:
        og_url = m.group(1)
        if not og_url.startswith("https://"):
            rep.fail(page, "og:image", "og:image должен быть абсолютным https-URL")
        else:
            local = ROOT / og_url.replace(BASE, "")
            if not local.exists():
                rep.fail(page, "og:image", f"файл не найден: {og_url}")
            else:
                rep.ok(page, "og:image")
    m = re.search(r'property="og:url" content="([^"]+)"', source)
    if m and m.group(1) != expected_url(rel):
        rep.fail(page, "og:url", f"og:url={m.group(1)} не совпадает с canonical")

    # --- заголовки ---
    h1 = len(re.findall(r"<h1\b", source))
    if h1 != 1:
        rep.fail(page, "h1", f"на странице {h1} тег(ов) <h1>, нужен ровно один")
    else:
        rep.ok(page, "h1")

    if html.unescape(re.sub(r"<[^>]+>", "", re.search(r"(?s)<h1[^>]*>(.*?)</h1>", source).group(1))).strip() == "":
        rep.fail(page, "h1", "пустой <h1>")

    # --- изображения ---
    imgs = re.findall(r"<img\b[^>]*>", source)
    no_alt = [i for i in imgs if "alt=" not in i]
    if no_alt:
        rep.fail(page, "img-alt", f"{len(no_alt)} изображений без alt")
    else:
        rep.ok(page, "img-alt")
    no_dim = [i for i in imgs if not ("width=" in i and "height=" in i)]
    if no_dim:
        rep.warn(page, "img-size", f"{len(no_dim)} изображений без width/height (CLS)")

    # --- внешние подресурсы ---
    offenders = [h for h in FORBIDDEN_HOSTS if h in source]
    if offenders:
        rep.fail(page, "no-external", "внешние запросы: " + ", ".join(offenders))
    else:
        rep.ok(page, "no-external")

    # --- JSON-LD ---
    blocks = re.findall(r'(?s)<script type="application/ld\+json">(.*?)</script>', source)
    if not blocks:
        rep.fail(page, "json-ld", "нет разметки schema.org")
    else:
        types: list[str] = []
        bad = False
        for raw in blocks:
            try:
                data = json.loads(raw)
            except json.JSONDecodeError as exc:
                rep.fail(page, "json-ld", f"невалидный JSON: {exc}")
                bad = True
                continue
            for node in data.get("@graph", [data]):
                t = node.get("@type")
                types.extend(t if isinstance(t, list) else [t])
        if not bad:
            rep.ok(page, "json-ld")

    if rel not in NOINDEX_PAGES:
        if not any(t in ("AccountingService", "ProfessionalService", "Organization", "LocalBusiness") for t in types):
            rep.fail(page, "schema-org", "нет узла организации в @graph")
        elif "#org" not in source:
            rep.warn(page, "schema-org", "узел организации не связан через @id #org")
        else:
            rep.ok(page, "schema-org")
        if rel.startswith("materials/") and rel != "materials/index.html":
            if "Article" not in types:
                rep.fail(page, "schema-article", "нет узла Article")
            elif "BreadcrumbList" not in types:
                rep.warn(page, "schema-article", "нет BreadcrumbList")
            else:
                rep.ok(page, "schema-article")

    # --- явные метаданные статьи ---
    if rel.startswith("materials/") and rel != "materials/index.html":
        for prop in ("article:published_time", "article:modified_time", "article:section"):
            if f'property="{prop}"' not in source:
                rep.warn(page, "article-meta", f"нет {prop}")
        if "doc-meta" not in source:
            rep.warn(page, "doc-meta", "нет видимой строки с датой и автором")

    # --- внутренние ссылки ---
    broken = []
    noncanonical = []
    for value in re.findall(r'(?:href|src)="([^"]+)"', source):
        if value.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
            continue
        target = value.split("#")[0].split("?")[0]
        if not target:
            continue
        if "index.html" in target and not target.startswith("index.html"):
            noncanonical.append(value)
        local = (path.parent / target).resolve()
        if path.parent.name == "materials" and target.endswith("/") and target == "../":
            local = ROOT / "index.html"
        elif target.endswith("/"):
            local = local / "index.html"
        if not local.exists():
            broken.append(value)
    if broken:
        rep.fail(page, "internal-links", "битые ссылки: " + ", ".join(sorted(set(broken))[:5]))
    else:
        rep.ok(page, "internal-links")
    if noncanonical:
        rep.fail(page, "link-canonical", "ссылки на /index.html дублируют главную: " + ", ".join(sorted(set(noncanonical))[:3]))
    else:
        rep.ok(page, "link-canonical")

    return source


def check_sitemap(rep: Report) -> None:
    path = ROOT / "sitemap.xml"
    if not path.exists():
        rep.fail("sitemap.xml", "exists", "файла нет")
        return
    try:
        tree = ET.parse(path)
    except ET.ParseError as exc:
        rep.fail("sitemap.xml", "xml", f"невалидный XML: {exc}")
        return
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [el.text.strip() for el in tree.getroot().findall("sm:url/sm:loc", ns)]
    rep.ok("sitemap.xml", "xml")

    expected = {expected_url(p) for p in PUBLIC_PAGES}
    missing = expected - set(locs)
    extra = set(locs) - expected
    if missing:
        rep.fail("sitemap.xml", "coverage", "нет URL: " + ", ".join(sorted(missing)))
    elif extra:
        rep.warn("sitemap.xml", "coverage", "лишние URL: " + ", ".join(sorted(extra)))
    else:
        rep.ok("sitemap.xml", "coverage")

    for loc in locs:
        if not loc.startswith(BASE):
            rep.fail("sitemap.xml", "host", f"чужая область: {loc}")
    if all(loc.startswith(BASE) for loc in locs):
        rep.ok("sitemap.xml", "host")

    mods = [el.text for el in tree.getroot().findall("sm:url/sm:lastmod", ns)]
    if any(not re.fullmatch(r"\d{4}-\d{2}-\d{2}", m or "") for m in mods):
        rep.fail("sitemap.xml", "lastmod", "lastmod должен быть в формате YYYY-MM-DD")
    else:
        rep.ok("sitemap.xml", "lastmod")


def check_robots(rep: Report) -> None:
    path = ROOT / "robots.txt"
    if not path.exists():
        rep.fail("robots.txt", "exists", "файла нет")
        return
    text = path.read_text(encoding="utf-8")
    if "sitemap.xml" not in text:
        rep.warn("robots.txt", "sitemap", "нет директивы Sitemap")
    if re.search(r"^Disallow:\s*/\s*$", text, re.M):
        rep.fail("robots.txt", "allow", "весь сайт закрыт от индексации")
    rep.ok("robots.txt", "content")


def check_feed(rep: Report) -> None:
    path = ROOT / "materials/feed.xml"
    if not path.exists():
        rep.warn("feed.xml", "exists", "нет RSS-фида для дистрибуции материалов")
        return
    try:
        tree = ET.parse(path)
    except ET.ParseError as exc:
        rep.fail("feed.xml", "xml", f"невалидный XML: {exc}")
        return
    items = tree.getroot().findall("./channel/item")
    if not items:
        rep.fail("feed.xml", "items", "в фиде нет ни одного материала")
    else:
        rep.ok("feed.xml", "items")


# Поля компании, без которых не работают локальная выдача, доверие и карточки.
# Пока данных нет — это предупреждения, а не ошибки: сайт работает, но недобирает.
NAP_FIELDS = [
    (
        "telephone",
        r'("telephone"\s*:|href="tel:)',
        "нет телефона (JSON-LD telephone и ссылка tel:) — не работают карточка организации "
        "и локальная выдача; телефон в шапке/подвале повышает конверсию",
    ),
    (
        "postalCode",
        r'"postalCode"\s*:',
        "нет почтового индекса в адресе организации — мешает сверке NAP с картами",
    ),
    (
        "openingHours",
        r'("openingHoursSpecification"|"openingHours")\s*:',
        "нет часов работы в разметке — поисковик не показывает «Открыто до…»",
    ),
    (
        "sameAs",
        r'"sameAs"\s*:',
        "нет sameAs — профили (VK, Telegram, 2ГИС, Яндекс Бизнес) не связаны с сайтом, "
        "поисковик не склеивает бренд в одну сущность",
    ),
    (
        "legal-ids",
        r'(ИНН\s*[0-9]{10}|ОГРН\s*[0-9]{13})',
        "нет ИНН/ОГРН в тексте — ниже доверие в YMYL-тематике и нет связки с ЕГРЮЛ",
    ),
]


NAV_DESKTOP = ["Услуги", "Тарифы", "Материалы", "О компании", "Контакты"]
NAV_MOBILE = [
    "Главная", "Услуги", "Тарифы", "Кому подходит", "О компании",
    "Кейсы", "Материалы", "Вопросы", "+7 921 640-02-34", "Контакты",
]


def _link_labels(html: str, cls: str) -> list[str]:
    return [
        re.sub(r"<[^>]+>", "", t).strip()
        for t in re.findall(rf'<a class="{cls}"[^>]*>(.*?)</a>', html, re.S)
    ]


def check_header(rep: Report) -> None:
    """Одна и та же шапка на всех публичных страницах (подписи пунктов)."""
    pages = list(PUBLIC_PAGES) + ["404.html"]
    for rel in pages:
        path = ROOT / rel
        if not path.exists():
            continue
        html = path.read_text(encoding="utf-8")
        if "site-header" not in html:
            rep.fail(rel, "header", "нет общей шапки site-header")
            continue
        desk = _link_labels(html, "nav__link")
        mob = _link_labels(html, "mobile-nav__link")
        if desk != NAV_DESKTOP:
            rep.fail(rel, "nav-desktop", f"ожидали {NAV_DESKTOP}, получили {desk}")
        else:
            rep.ok(rel, "nav-desktop")
        if mob != NAV_MOBILE:
            rep.fail(rel, "nav-mobile", f"ожидали {NAV_MOBILE}, получили {mob}")
        else:
            rep.ok(rel, "nav-mobile")
        if 'href="tel:+79216400234"' not in html:
            rep.fail(rel, "nav-phone", "в шапке нет tel:+79216400234")
        else:
            rep.ok(rel, "nav-phone")


def check_nap(rep: Report) -> None:
    """Проверяет наличие контактных и юридических данных компании."""
    source = (ROOT / "index.html").read_text(encoding="utf-8")
    for name, pattern, message in NAP_FIELDS:
        if re.search(pattern, source):
            rep.ok("index.html", name)
        else:
            rep.warn("index.html", name, message)


def main() -> int:
    parser = argparse.ArgumentParser(description="SEO-аудит статического сайта")
    parser.add_argument("--verbose", action="store_true", help="показать все проверки")
    parser.add_argument("--json", action="store_true", help="вывод в JSON")
    args = parser.parse_args()

    rep = Report()
    for rel in PUBLIC_PAGES + NOINDEX_PAGES:
        check_page(rep, rel)
    check_sitemap(rep)
    check_robots(rep)
    check_feed(rep)
    check_header(rep)
    check_nap(rep)

    if args.json:
        print(json.dumps(
            {
                "passed": not rep.errors,
                "errors": len(rep.errors),
                "warnings": len(rep.warnings),
                "checks": len(rep.items),
                "findings": [i for i in rep.items if i["level"] != "ok"],
            },
            ensure_ascii=False,
            indent=2,
        ))
        return 0 if not rep.errors else 1

    per_page: dict[str, list[dict]] = {}
    for item in rep.items:
        per_page.setdefault(item["page"], []).append(item)

    ok_total = sum(1 for i in rep.items if i["level"] == "ok")
    print("SEO-аудит «НЕО КОНСАЛТИНГ»")
    print(f"Проверок: {len(rep.items)} · успешно: {ok_total} · "
          f"ошибок: {len(rep.errors)} · предупреждений: {len(rep.warnings)}\n")

    for page, items in per_page.items():
        errs = [i for i in items if i["level"] == "error"]
        warns = [i for i in items if i["level"] == "warn"]
        status = "FAIL" if errs else ("WARN" if warns else " OK ")
        print(f"[{status}] {page}")
        for item in errs + warns:
            print(f"        {item['level']:5s} {item['check']:16s} {item['message']}")
        if args.verbose:
            for item in items:
                if item["level"] == "ok":
                    print(f"        ok    {item['check']}")
    print()
    if rep.errors:
        print("Аудит не пройден: исправьте ошибки выше.")
        return 1
    print("Аудит пройден: критичных проблем поисковой и социальной оптимизации нет.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
