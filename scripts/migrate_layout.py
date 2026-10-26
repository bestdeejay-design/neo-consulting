#!/usr/bin/env python3
"""Переводит страницы materials/ на общую вёрстку лендинга (tokens + main + article)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAT = ROOT / "materials"

CSS_LINKS = """<link rel="stylesheet" href="../css/tokens.css">
<link rel="stylesheet" href="../css/main.css">
<link rel="stylesheet" href="../css/article.css">
"""

HEADER = """<header class="site-header">
  <div class="container site-header__inner">
    <a class="brand" href="../" aria-label="НЕО КОНСАЛТИНГ — на главную">
      <span class="brand__mark" aria-hidden="true">НК</span>
      <span>НЕО КОНСАЛТИНГ<span class="brand__sub">бухгалтерский аутсорсинг, СПб</span></span>
    </a>
    <nav class="nav" aria-label="Основная навигация">
      <ul class="nav__list">
        <li><a class="nav__link" href="../#services">Услуги</a></li>
        <li><a class="nav__link" href="../#pricing">Тарифы</a></li>
        <li><a class="nav__link" href="./"{current}>Материалы</a></li>
        <li><a class="nav__link" href="../#about">О компании</a></li>
        <li><a class="nav__link" href="../#contacts">Контакты</a></li>
      </ul>
    </nav>
    <a class="header-phone" href="tel:+79216400234">+7 921 640-02-34</a>
    <button class="nav-toggle" type="button" id="navToggle" aria-label="Открыть меню" aria-expanded="false" aria-controls="mobileNav">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<nav class="mobile-nav" id="mobileNav" aria-label="Мобильная навигация">
  <ul class="mobile-nav__list">
    <li><a class="mobile-nav__link" href="../">Главная</a></li>
    <li><a class="mobile-nav__link" href="../#services">Услуги</a></li>
    <li><a class="mobile-nav__link" href="../#pricing">Тарифы</a></li>
    <li><a class="mobile-nav__link" href="../#audience">Кому подходит</a></li>
    <li><a class="mobile-nav__link" href="../#about">О компании</a></li>
    <li><a class="mobile-nav__link" href="../#cases">Кейсы</a></li>
    <li><a class="mobile-nav__link" href="./"{current}>Материалы</a></li>
    <li><a class="mobile-nav__link" href="../#faq">Вопросы</a></li>
    <li><a class="mobile-nav__link" href="tel:+79216400234">+7 921 640-02-34</a></li>
    <li><a class="mobile-nav__link" href="../#contacts">Контакты</a></li>
  </ul>
</nav>
"""

FOOTER = """
<footer class="site-footer">
  <div class="container footer__grid">
    <div>
      <p class="footer__brand">ООО «НЕО КОНСАЛТИНГ»</p>
      <ul class="footer__nav">
        <li><a href="../#services">Услуги</a></li>
        <li><a href="../#pricing">Тарифы</a></li>
        <li><a href="../#about">О компании</a></li>
        <li><a href="./">Материалы</a></li>
        <li><a href="../#contacts">Контакты</a></li>
      </ul>
      <p class="footer__meta">© <span id="year">2026</span> ООО «НЕО КОНСАЛТИНГ». Санкт-Петербург.</p>
    </div>
    <p class="footer__meta">Email: <a href="mailto:zh_nadi@mail.ru">zh_nadi@mail.ru</a></p>
  </div>
</footer>

<button class="back-to-top" type="button" id="backToTop" aria-label="Наверх" title="Наверх">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m18 15-6-6-6 6"/></svg>
</button>

<script src="../js/main.js"></script>
<script src="../js/article.js"></script>
</body>
</html>
"""


def migrate(path: Path) -> None:
    html = path.read_text(encoding="utf-8")
    is_hub = path.name == "index.html"
    current = ' aria-current="page"' if is_hub else ""

    # схлопываем вложенные <style> и вырезаем блок
    html = re.sub(r"(?:<style>\s*)+.*?</style>", "", html, count=1, flags=re.S)
    # если остались хвосты
    html = re.sub(r"<style>.*?</style>", "", html, flags=re.S)

    if 'href="../css/tokens.css"' not in html:
        html = html.replace("</head>", CSS_LINKS + "</head>", 1)

    # шапка + мобильное меню
    html = re.sub(
        r"<header class=\"site-header\">.*?</header>\s*<nav class=\"mobile-nav\".*?</nav>",
        HEADER.format(current=current).strip(),
        html,
        count=1,
        flags=re.S,
    )

    # подвал и старые скрипты
    html = re.sub(r"<footer class=\"site-footer\">.*$", FOOTER.lstrip(), html, count=1, flags=re.S)

    html = html.replace('<section class="hero"', '<section class="doc-hero"')
    html = html.replace('class="btn"', 'class="btn btn--primary"')
    html = html.replace("class=\"btn btn--primary btn--primary\"", "class=\"btn btn--primary\"")

    # убираем пустые строки после вырезанного style
    html = re.sub(r"\n{3,}", "\n\n", html)
    path.write_text(html, encoding="utf-8")
    print(f"ok {path.relative_to(ROOT)}")


def main() -> None:
    for p in sorted(MAT.glob("*.html")):
        migrate(p)


if __name__ == "__main__":
    main()
