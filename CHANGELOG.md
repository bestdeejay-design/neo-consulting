# Changelog

Все заметные изменения проекта фиксируются в этом файле в формате
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Проект следует [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-08-14

### Added

- Статический лендинг ООО «НЕО КОНСАЛТИНГ» (бухгалтерский аутсорсинг, СПб):
  14 секций, семантический HTML, единственный `<h1>`, иерархия заголовков по WCAG.
- Дизайн-токены в `css/tokens.css` (`:root`), mobile-first адаптив (640/960px),
  меню-бургер, FAQ-аккордеон на нативных `<details>/<summary>`, таблица тарифов.
- SEO-слой: canonical, Open Graph/Twitter (1200×630), JSON-LD
  (`ProfessionalService` + `FAQPage`), `robots.txt`, `sitemap.xml`, favicon.
- Только локальные изображения (`assets/img/`), ноль внешних запросов.
- Документация L1 (`docs/`): VISION, PRD, ROADMAP, TEST_PLAN, DECISIONS + `content.md`.
- GitHub Pages: `https://bestdeejay-design.github.io/neo-consulting/`.

### Quality

- Lighthouse: mobile **100/100/100/100**, desktop **91/100/100/100**.
- meta_audit: 17/18 (одно ложное срабатывание, описано в `.audit/meta-notes.md`).