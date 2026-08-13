# Plan: Лендинг ООО «НЕО КОНСАЛТИНГ» — полный цикл (контент, дизайн, код, SEO, репозиторий)

> Дата: 2026-08-13
> Статус: `approved`

## Goal

Статический одностраничный сайт-лендинг бухгалтерского аутсорсинга для ООО «НЕО
КОНСАЛТИНГ» (Санкт-Петербург) с 14 блоками по брифу заказчика, полной
документацией (L1), SEO-комплектом, тестовой графикой и оформленным GitHub-репозиторием
с GitHub Pages.

**Acceptance criteria (проверяемо):**
- [ ] CR1: `index.html` содержит все 14 блоков брифа (hero, боли, решение, услуги, детали, кому подходит, тарифы, как работаем, о компании, гарантии, кейсы, отзывы, FAQ, контакты)
- [ ] CR2: `frontend-perfection`: `meta_audit.py` exit 0; `audit.js --mobile` и `audit.js --desktop` → все категории ≥ 90 (порог 90, т.к. статический сайт без CDN; отчёт фиксирует это)
- [ ] CR3: SEO-комплект на месте: title/description/OG/JSON-LD (ProfessionalService + FAQPage) в `index.html`, `robots.txt`, `sitemap.xml`
- [ ] CR4: тестовые изображения сгенерированы в `assets/img/` и подключены (аватары отзывов, фото офиса/команды, OG-картинка 1200×630)
- [ ] CR5: GitHub-репозиторий `bestdeejay-design/neo-consulting` создан, сайт запушен, Pages включён, README.md+README.ru.md+LICENSE+CONTRIBUTING+SECURITY+CODE_OF_CONDUCT на месте, description и topics заданы

## Constraints

- Статический сайт: только HTML/CSS/JS без сборщиков и зависимостей (для лендинга допустимо; Lighthouse прогоняется через локальный `python3 -m http.server`)
- Весь контент — строго по брифу заказчика (название, директор, ОКВЭД, УТП, тон «мы/вам»)
- В итоговых артефактах не остаётся незавершённых мест: каждый файл доводится до конечного состояния в рамках своего шага
- Изображения — только локальные файлы `assets/img/` (ноль внешних URL)
- Не коммитить без явного одобрения пользователя на финальном шаге (после показа результата)

## Steps

### Step 1: Документация проекта (docs-system, L1)
- Files: `docs/VISION.md`, `docs/PRD.md`, `docs/ROADMAP.md`, `docs/TEST_PLAN.md`, `docs/DECISIONS.md`
- Produces: 5 документов, описывающих продукт («почему», «что», «этапы», «как проверяем», «решения»)
- Consumes: бриф заказчика (текст задачи)
- Action: написать документацию по шаблонам docs-system, L1-уровень (VISION+PRD+ROADMAP+TEST_PLAN+DECISIONS вместо полного набора L2)
- Verification: все 5 файлов существуют, PRD содержит критерии приёмки, TEST_PLAN ссылается на CR2
- [ ] done

### Step 2: Контент 14 блоков
- Files: `docs/content.md`
- Produces: полные тексты всех 14 блоков (hero, боли, решение, услуги, детали услуг, сегменты, тарифы с таблицей, этапы, о компании, гарантии, кейсы, отзывы, FAQ, контакты)
- Consumes: бриф заказчика (14-блочная структура, УТП, тон)
- Action: делегировать копирайтеру (скилл удалённых текстов не нужен — пишет по брифу); тексты на русском, тон «мы/вам», без сложных терминов
- Verification: `docs/content.md` содержит все 14 секций по нумерации брифа, тарифы — таблица
- [ ] done

### Step 3: Скелет сайта + дизайн-токены
- Files: `index.html`, `css/main.css`, `css/tokens.css`, `js/main.js`
- Produces: каркас страницы с 14 секциями по `docs/content.md`
- Consumes: `docs/content.md` (Step 2)
- Action: делегировать visual-engineering: design-taste фаза (Design Read → токены → uniqueness gate → реализация); дизайн-токены в `:root`, ноль raw-hex вне токенов; семантика (header/main/section/footer), один H1
- Verification: `python3 .../meta_audit.py --html index.html --css css/main.css css/tokens.css` — секции `tokens:raw-hex`, `headings:*` зелёные
- [ ] done

### Step 4: Тестовые изображения
- Files: `assets/img/avatar-1.png`…`avatar-3.png`, `assets/img/office-*.jpg`, `assets/img/og-2026-08-13.png`
- Produces: аватарки для 3 отзывов (ui-avatars), 2–3 фото (офис/работа), OG-картинка 1200×630 (crop-safe, контент в центральной зоне ~640px)
- Consumes: структура сайта (Step 3) — пути в `assets/img/`
- Action: запустить `scripts/test-graphics.py` из скилла test-graphics; OG генерируется после финальной вёрстки через headless-скриншот hero-зоны лендинга
- Verification: все файлы существуют, размеры корректны (avatar 128×128, фото 800×600+, OG 1200×630)
- [ ] done

### Step 5: SEO-комплект
- Files: `index.html` (head), `robots.txt`, `sitemap.xml`
- Produces: title ≤ 60, description ≤ 160, canonical, OG (1200×630 + width/height), Twitter card, JSON-LD (ProfessionalService + FAQPage), robots.txt (allow all + sitemap-ссылка), sitemap.xml
- Consumes: `docs/content.md` (заголовки/FAQ для JSON-LD), `assets/img/og-*.png` (Step 4)
- Action: по seo-toolkit (seo-meta, seo-schema, seo-crawl); включить ссылку на sitemap в robots.txt
- Verification: `meta_audit.py` — все `meta:*` и `meta:json-ld` зелёные
- [ ] done

### Step 6: Финальный аудит frontend-perfection
- Files: `lh-mobile.json`, `lh-desktop.json`, `meta.json` (отчёты — в `.audit/`)
- Produces: отчёт с результатами до/после
- Consumes: финальный `index.html` + CSS (Steps 3–5)
- Action: `python3 -m http.server 8377` + `node <skill>/scripts/audit.js --mobile/--desktop` + `meta_audit.py`; фиксы по audit id до зелёного (порог категорий ≥ 90; ниже — документировать причину)
- Verification: оба Lighthouse-прогона exit 0 при `--threshold 90`, meta_audit exit 0
- [ ] done

### Step 7: GitHub-репозиторий + Pages
- Files: `./.git` (локальный), удалённый репозиторий `bestdeejay-design/neo-consulting` (создаётся через `gh repo create`)
- Produces: репо создано, ветка main, сайт запушен, Pages включён (branch main / root)
- Consumes: все файлы проекта
- Action: `gh repo create neo-consulting --public --source . --push`; `gh api repos/.../pages -X POST` с source main/root (или через `gh api` PUT)
- Verification: `gh repo view bestdeejay-design/neo-consulting` → репо существует; URL Pages отвечает 200 после деплоя
- [ ] done

### Step 8: Оформление репозитория (github-repo-hygiene)
- Files: `README.md`, `README.ru.md`, `LICENSE` (MIT, владелец bestdeejay-design, 2026), `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `assets/header.svg`, `assets/footer.svg`, `.github/ISSUE_TEMPLATE/*.yml`, `.github/pull_request_template.md`
- Produces: community health 100%, README EN+RU с local SVG header/footer, description + topics (через `gh`)
- Consumes: Step 7 (репо), название/описание проекта
- Action: `python3 scripts/generate_assets.py` (пресет default, COLD/WARM из палитры лендинга) + `validate_svg.py`; README по чек-листу скилла (без AI-slop); `gh repo edit --description` и `gh api -X PUT topics`
- Verification: `python3 scripts/validate_repo.py neo-consulting` → все 16 пунктов зелёные (допустимо: social preview через UI — документировать, если недоступен через API)
- [ ] done

## Interfaces

- Consumes → Produces:
  - `Step1.docs` → `Step2` (PRD фиксирует требования к контенту)
  - `Step2.content.md` → `Step3` (тексты в секции)
  - `Step3.index.html` → `Step4` (пути к картинкам), `Step5` (head), `Step6` (аудит)
  - `Step4.og.png` → `Step5` (og:image)
  - `Step6.отчёты` → `Step7` (финальное состояние коммитится)
  - `Step8` независим от верстки, зависит от Step7

## Verification (полная)

- [ ] `python3 scripts/plan_validator.py docs/plans/neo-consulting-landing-2026-08-13.md` → ✅
- [ ] CR1: 14 секций в `index.html` (проверка grep по id секций)
- [ ] CR2: Lighthouse mobile+desktop ≥ 90, meta_audit exit 0
- [ ] CR3: robots.txt + sitemap.xml + JSON-LD присутствуют (grep)
- [ ] CR4: файлы `assets/img/` существуют (ls)
- [ ] CR5: `gh repo view` + `validate_repo.py` → зелёный
- [ ] Ревью: code-review скилл перед финальным коммитом