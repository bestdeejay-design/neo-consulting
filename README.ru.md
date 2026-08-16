<div align="center">

<img src="assets/header.svg" alt="neo-consulting — НЕО КОНСАЛТИНГ" width="100%">

**🌐 Версии:** [English](README.md) · [Русский](README.ru.md) · [Сайт](https://bestdeejay-design.github.io/neo-consulting/) · [Презентация](https://bestdeejay-design.github.io/neo-consulting/presentation/)

</div>

# НЕО КОНСАЛТИНГ — лендинг бухгалтерского аутсорсинга

Статический лендинг для **ООО «НЕО КОНСАЛТИНГ»** — бухгалтерские, налоговые и
юридические услуги для ИП и ООО на УСН в Санкт-Петербурге.

Собран на чистом HTML/CSS/JS без сборщиков и **без внешних запросов** — все шрифты,
иконки, изображения и метаданные локальные.

## Статус проверок

| Проверка | Результат |
|---|---|
| Lighthouse mobile | **100 / 100 / 100 / 100** |
| Lighthouse desktop | **91 / 100 / 100 / 100** (порог 90) |
| meta_audit | 17/18 (одно известное ложное срабатывание) |
| Контраст WCAG AA | все пары текст/фон ≥ 4.5:1 |
| Raw hex вне дизайн-токенов | 0 |

## Живой сайт

- **Сайт:** [bestdeejay-design.github.io/neo-consulting](https://bestdeejay-design.github.io/neo-consulting/)
- **Презентация:** [bestdeejay-design.github.io/neo-consulting/presentation](https://bestdeejay-design.github.io/neo-consulting/presentation/)
- **Материалы:** [bestdeejay-design.github.io/neo-consulting/materials](https://bestdeejay-design.github.io/neo-consulting/materials/)

## Быстрый старт

```bash
# открыть напрямую
open index.html

# или локальный сервер
python3 -m http.server 8377
```

## Возможности

- **16 секций лендинга** (`hero`, `problems`, `solution`, `services`, `details`,
  `audience`, `pricing`, `process`, `about`, `team`, `gallery`, `guarantees`, `cases`,
  `reviews`, `faq`, `contacts`) с якорной навигацией
- **Ротация фото**: 12 локальных фото 4:3 перемешиваются по 8 позициям `data-slot`
  при каждой загрузке страницы (hero берётся из приоритетного пула, дубли в пределах
  страницы исключены, последний hero запоминается в `localStorage`, без JS работает
  дефолтная раскладка)
- **Семантический HTML**: единственный `<h1>`, иерархия заголовков по WCAG,
  FAQ-аккордеон на нативных `<details>/<summary>`, таблица тарифов с горизонтальным
  скроллом на мобильных
- **Дизайн-токены**: все цвета объявлены один раз в `css/tokens.css` (`:root`),
  ноль raw-hex вне токенов; сдержанный пихтово-зелёный акцент `#2E5E4E`
- **Доступность**: контраст 4.5:1, состояния `:focus-visible`, тап-зоны от 44px,
  `scroll-padding-top` для фиксированной шапки, ARIA-метки
- **SEO-слой**: canonical, Open Graph / Twitter-карточки (1200×630), JSON-LD
  `ProfessionalService` + `FAQPage`, `robots.txt`, `sitemap.xml`, favicon
- **Только локальные изображения**: сгенерированные аватарки, фото офиса, OG-картинка —
  без CDN
- **Адаптив**: mobile-first, брейкпоинты 640px и 960px, меню-бургер
- **Продающая презентация**: самодостаточный интерактивный дека из 12 слайдов (`presentation/`) — заметки спикера, таймер, навигация с клавиатуры
- **Библиотека материалов**: 7 SEO-готовых гайдов (налоговый календарь, автоматизация 1С, ЭТрН, НДС/УСН, взносы ИП, объект УСН, амнистия) со своими OG-картинками и якорной навигацией

## Структура репозитория

```
.
├── index.html              # лендинг (16 секций, JSON-LD, OG/Twitter)
├── presentation/
│   └── index.html          # интерактивная презентация (12 слайдов, самодостаточная)
├── materials/
│   ├── index.html          # библиотека материалов (7 гайдов)
│   ├── 1c-automation-guide.html
│   ├── etrn-guide.html
│   ├── nds-usn-2026.html
│   ├── calendar-2026.html
│   ├── ip-vznosy-2026.html
│   ├── usn-object.html
│   └── amnistia.html
├── css/
│   ├── tokens.css          # дизайн-токены (кастомные свойства :root)
│   └── main.css            # стили (mobile-first)
├── js/
│   ├── main.js             # меню, текущий год, закрытие по Escape/resize
│   └── photos.js           # ротация фото по позициям data-slot
├── assets/
│   ├── img/                # аватарки, фото hero/офиса, OG-картинки, favicon
│   │   ├── og/             # OG-превью гайдов (1200×630)
│   │   └── photos/         # пул ротации: photo-*.webp (4:3, 12 файлов)
│   ├── header.svg          # анимированная шапка README (SMIL)
│   └── footer.svg          # анимированный подвал README (SMIL)
├── docs/
│   ├── content.md          # тексты всех 16 секций
│   ├── VISION.md           # продуктовая документация (L1)
│   ├── PRD.md
│   ├── ROADMAP.md
│   ├── TEST_PLAN.md
│   ├── DECISIONS.md
│   └── plans/              # план разработки
├── .github/
│   ├── ISSUE_TEMPLATE/     # формы issue (баг/фича)
│   ├── pull_request_template.md
│   └── workflows/
│       └── ci.yml          # CI: проверки h1/секций/raw-hex/SEO-меты
├── CHANGELOG.md            # история релизов
├── LICENSE                 # MIT
├── CODE_OF_CONDUCT.md      # Contributor Covenant 2.1
├── CONTRIBUTING.md
├── SECURITY.md
├── SUPPORT.md
├── robots.txt
└── sitemap.xml
```

## Документация

Продуктовая документация (L1) — в [`docs/`](docs/): VISION, PRD, ROADMAP,
TEST_PLAN и DECISIONS. Тексты всех 16 секций — в [`docs/content.md`](docs/content.md).

---

<div align="center">

<img src="assets/footer.svg" alt="bestdeejay-design — neo-consulting" width="100%">

</div>