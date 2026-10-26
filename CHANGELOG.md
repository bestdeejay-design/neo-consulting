# Changelog

Все заметные изменения проекта фиксируются в этом файле в формате
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Проект следует [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.4.1] — 2026-10-26

Внутренний аудит вёрстки и адаптива.

### Fixed

- Десктопная навигация: 8 пунктов не влезали в 960px — оставили 5, как в материалах.
- Мобильное меню главной: 18 ссылок → 9 рабочих.
- `.hero__facts`: на 320px три колонки сжимались в кашу — до 480px одна колонка.
- После перевода гайдов на токены `var(--s-3)` в инлайнах ничего не делал — алиасы + вычищены инлайн-стили.
- Неоформленные `.note` / `.solution` / `.price-cap` / `.card-head` в старых гайдах.
- `h2`/`h3` и FAQ на узком экране через `clamp`; `overflow-wrap` у ячеек таблиц.
- Safe-area у подвала и мобильного меню; skip-link; hover-lift только при `(hover: hover)`.
- 5 шагов процесса в ряд только от 1100px, иначе две колонки.

## [1.4.0] — 2026-10-26

Единая вёрстка материалов с лендингом, адаптив.

### Fixed

- Страницы-кластеры (в т.ч. АНО) собирались с вложенными `<style><style><style>`
  и отдельной «золото/navy» палитрой — визуальный разрыв с главной.
- Все 14 HTML в `materials/` переведены на `tokens.css` + `main.css` + `article.css`:
  общая шапка, меню, подвал, таблицы с горизонтальным скроллом, FAQ, таймлайн.
- Мобильные правки лендинга: скрыт `brand__sub` до 400px, кнопки CTA на всю ширину,
  сетка карточек `auto-fit`, таблицы от 520px внутри `.table-wrap`.

### Added

- `css/article.css`, `js/article.js` — компоненты статей без raw hex.
- `404.html` на той же системе токенов.

## [1.3.0] — 2026-10-26

Четыре коммерческие страницы-кластера: зарплата, регистрация, АНО, ОСНО.

### Added

- `materials/zarplata-i-kadry.html` — зарплатный участок (1 741 слово): состав,
  сроки 2026, кадры, риски, передача без остановки выплат, FAQPage.
- `materials/registraciya-i-zakrytie.html` — регистрация и закрытие ИП/ООО
  (1 599 слов): выбор формы, документы, ОКВЭД и режим, ликвидация, отчётность.
- `materials/avtonomnaya-nekommercheskaya-organizaciya.html` — АНО (1 561 слово):
  налоги, целевые поступления, Минюст, ошибки учёта, FAQPage.
- `materials/osno.html` — общая система (1 594 слова): НДС, прибыль, сравнение
  с УСН, переход между режимами, FAQPage.
- OG-карточки 1200×630 для четырёх страниц.

### Changed

- Главная: в `#services` и `#details` добавлены учёт на ОСНО и учёт АНО
  со ссылками на разборы; в `#audience` — карточки «ИП и ООО на ОСНО» и «АНО»;
  в `#guides` 9 карточек; в JSON-LD `hasOfferCatalog` — два новых Offer;
  FAQ и тарифная сноска: ОСНО и АНО считаются отдельно, без выдуманной цены.
- Хаб материалов: 13 карточек, `hasPart` дополнен.
- `sitemap.xml` — 15 URL, `materials/feed.xml` — 13 материалов.
- `scripts/seo_audit.py` и `scripts/make_og.py` знают новые страницы.

## [1.2.0] — 2026-10-26

Две коммерческие страницы-кластера по итогам SEO-аудита.

### Added

- `materials/smena-buhgaltera.html` — «Как сменить бухгалтера и передать учёт без
  штрафов» (1 827 слов): таблица ответственности со ссылками на 402-ФЗ, ТК РФ и НК РФ,
  пять шагов передачи, чек-лист из 10 позиций, сроки и риски, FAQ из 5 вопросов
  (`FAQPage`), CTA.
- `materials/shtatny-buhgalter-ili-autsorsing.html` — «Штатный бухгалтер или
  аутсорсинг» (1 515 слов): расчёт полной стоимости специалиста в штате, сравнение
  состава услуг, 7 критериев выбора, честные ограничения аутсорсинга, FAQ.
- `scripts/make_og.py` — генератор OG-карточек 1200×630 в фирменном стиле
  (`assets/img/og/og-smena-buhgaltera.jpg`, `og-shtatny-buhgalter-ili-autsorsing.jpg`).
- Стили FAQ-аккордеона и выноски «короткий ответ» для статей.

### Changed

- Главная: в секции `#guides` теперь 5 карточек, включая обе новые страницы.
- Хаб материалов: 9 карточек, `hasPart` дополнен двумя материалами.
- Четыре статьи (`nds-usn-2026`, `ip-vznosy-2026`, `calendar-2026`, `usn-object`)
  получили блок «Смотрите также» со ссылками на новые страницы.
- `sitemap.xml` — 11 URL, `materials/feed.xml` — 9 материалов.
- `scripts/seo_audit.py`: 199 проверок — добавлены новые страницы в обязательный список
  и проверка контактных/юридических данных (`telephone`, `postalCode`, `openingHoursSpecification`,
  `sameAs`, ИНН/ОГРН) как предупреждения.

### Quality

- `python3 scripts/seo_audit.py`: 199 проверок, 0 ошибок, 5 предупреждений — все про
  отсутствующие данные компании (телефон, индекс, часы работы, `sameAs`, ИНН/ОГРН).
- `docs/SEO_INPUTS.md` — заполняемый чек-лист: данные, доступы, решения, материалы.
- `html-validate`: 0 ошибок на всех 12 HTML-файлах.

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