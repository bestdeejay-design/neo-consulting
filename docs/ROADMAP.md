# ROADMAP — Дорожная карта

> **RU:** дорожная карта — что и когда выходит, с привязкой к PRD и плану.
> Каждый майлстоун отвечает «как поймём, что выкатили и что это важно?».

## Current state

Проект на старте. Утверждён план `docs/plans/neo-consulting-landing-2026-08-13.md`
(статус `approved`). Написана документация L1 (VISION, PRD, ROADMAP, TEST_PLAN,
DECISIONS). Дальше — контент, вёрстка, графика, SEO, аудит, публикация.

## Milestones / phases

### M1 — Контент 14 блоков · target: `2026-08-13`
- **Goal:** готовые тексты всех 14 блоков на русском, тон «мы/вам».
- **Features:** `docs/content.md` со всеми секциями по нумерации брифа.
- **Proof:** `docs/content.md` содержит 14 секций, тарифы — таблица.
- **Status:** 📋

### M2 — Дизайн и вёрстка · target: `2026-08-13`
- **Goal:** каркас `index.html` с 14 секциями, токены в `:root`, семантика.
- **Features:** `index.html`, `css/main.css`, `css/tokens.css`, `js/main.js`.
- **Proof:** `meta_audit.py` — секции `tokens:raw-hex`, `headings:*` зелёные.
- **Status:** 📋

### M3 — Графика · target: `2026-08-13`
- **Goal:** тестовые изображения локально в `assets/img/`.
- **Features:** аватары отзывов, фото офиса/команды, OG 1200×630.
- **Proof:** файлы существуют, размеры корректны (avatar 128×128, фото 800×600+, OG 1200×630).
- **Status:** 📋

### M4 — SEO-комплект · target: `2026-08-13`
- **Goal:** метаданные, JSON-LD, robots, sitemap на месте.
- **Features:** title/description/OG/Twitter, `ProfessionalService`+`FAQPage`, `robots.txt`, `sitemap.xml`.
- **Proof:** `meta_audit.py` — все `meta:*` и `meta:json-ld` зелёные.
- **Status:** 📋

### M5 — Аудит (frontend-perfection) · target: `2026-08-13`
- **Goal:** Lighthouse mobile+desktop ≥ 90, meta_audit exit 0.
- **Features:** `lh-mobile.json`, `lh-desktop.json`, `meta.json` в `.audit/`.
- **Proof:** оба Lighthouse-прогона exit 0 при `--threshold 90`, meta_audit exit 0.
- **Status:** 📋

### M6 — Публикация (GitHub Pages) · target: `2026-08-13`
- **Goal:** сайт живёт на Pages по URL репозитория.
- **Features:** репо `bestdeejay-design/neo-consulting`, ветка main, Pages branch main/root.
- **Proof:** `gh repo view` → репо существует; URL Pages отвечает 200.
- **Status:** 📋

### M7 — Оформление репозитория · target: `2026-08-13`
- **Goal:** community health 100%, README EN+RU, лицензия MIT.
- **Features:** README.md, README.ru.md, LICENSE, CONTRIBUTING, SECURITY, CODE_OF_CONDUCT, SVG header/footer, шаблоны issue/PR, description+topics.
- **Proof:** `validate_repo.py` → все пункты зелёные.
- **Status:** 📋

## Now / Next / Later

| Now | Next | Later |
|-----|------|-------|
| M1 (контент) | M2 (вёрстка) | M7 (гигиена репо) |

## Dependencies & risks

| Risk | Impact | Mitigation | Owner |
|------|--------|------------|-------|
| OG-картинка требует финальной вёрстки | Med | генерируется после M2 скриншотом hero | dev |
| Pages недоступен через API | Low | включить через `gh api`, документировать | dev |
| Lighthouse ниже 90 на mobile | Med | фиксы по audit id до зелёного | dev |

## Review cadence

- **Cadence:** разовый прогон по плану (один релиз).
- **Participants:** заказчик (best), исполнитель.
- **Inputs:** CR1–CR5 из PRD, отчёты `.audit/`.
