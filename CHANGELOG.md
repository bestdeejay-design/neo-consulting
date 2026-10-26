# Changelog

Все заметные изменения проекта фиксируются в этом файле в формате
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Проект следует [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] — 2026-10-26

SEO-аудит и расширение поисковой и социальной оптимизации.

### Added

- `scripts/seo_audit.py` — воспроизводимый аудит (162 проверки): title/description,
  canonical, robots, OG/Twitter, JSON-LD, alt и размеры изображений, отсутствие
  внешних подресурсов, битые и неканоничные ссылки, полнота sitemap, RSS.
- `docs/SEO_AUDIT_2026-10-26.md` — отчёт аудита, варианты расширения, блокеры
  и план на 30/90 дней.
- Секция `#guides` на главной («Разборы») — внутренние ссылки на ключевые материалы.
- `materials/feed.xml` — RSS-фид на 7 материалов; `rel="alternate"` на всех страницах.
- `404.html` — страница ошибки без индексации, со ссылками на разделы.
- Блок «Поделиться» (Telegram, ВКонтакте, WhatsApp) в каждом материале.
- Видимая строка «Опубликовано / Обновлено / Автор» в материалах (E-E-A-T).

### Changed

- Title главной и 8 страниц переписаны под длину 57–70 символов, description — 148–160.
- JSON-LD: `Organization` (полный узел, `AccountingService` + `ProfessionalService`,
  `hasOfferCatalog`), `WebSite`, `Blog`, `articleSection`, `keywords`,
  `isAccessibleForFree`, `isPartOf`; автор материала — `Person` с `worksFor → #org`.
- `sitemap.xml`: 9 URL с `lastmod` 2026-10-26 и image-разметкой; `presentation/` исключена.
- `robots.txt`: пояснение про подпуть `github.io`, `Clean-param`, `Sitemap`.
- 168 внутренних ссылок `/index.html` заменены на `/` (канонизация).
- Страницы материалов больше не грузят Google Fonts: системные стеки из `css/tokens.css`.
- `presentation/index.html`: `noindex, follow`, canonical, description, OG/Twitter,
  `PresentationDigitalDocument`.
- `div[role=region]` → нативные `<aside>`, `aria-label` только на валидных элементах,
  `type="button"` у всех кнопок; `html-validate`: 23 ошибки → 0.

### Quality

- `python3 scripts/seo_audit.py`: 162 проверки, 0 ошибок, 0 предупреждений.
- `html-validate`: 0 ошибок (остались 3 предупреждения о пропуске уровня заголовка
  в служебной презентации).
- CI расширен: SEO-аудит + единственный `<h1>` на каждой странице, наличие
  `404.html` и RSS, валидность XML.

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