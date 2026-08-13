# TEST_PLAN — Как доказываем корректность

> **RU:** L1-уровень проверки (растёт до TEST_CASES на L2). Каждый пункт — это
> наблюдаемый, повторяемый тест. Привязан к CR1–CR5 из PRD и плану.

## §0 Структура HTML

- **T1 — 14 секций.** `index.html` содержит ровно 14 блоков брифа.
  Тест: `grep -c 'id="(hero|pains|solution|services|details|segments|tariffs|process|about|guarantees|cases|reviews|faq|contacts)"' index.html` → 14.
- **T2 — один H1.** На странице ровно один `<h1>`.
  Тест: `grep -o '<h1' index.html | wc -l` → 1.
- **T3 — порядок заголовков.** `h1 → h2 → h3` без скачков (нет `h1` сразу после `h3`).
  Тест: `meta_audit.py` секция `headings:order` зелёная.

## §1 Дизайн-токены и контраст

- **T4 — токены.** Все цвета объявлены в `:root`, вне токенов нет raw-hex.
  Тест: `meta_audit.py` секция `tokens:raw-hex` зелёная (exit 0).
- **T5 — контраст WCAG.** Текст/фон ≥ 4.5:1.
  Тест: `meta_audit.py` секция `contrast:wcag` зелёная.

## §2 Метаданные и SEO

- **T6 — meta_audit.** `python3 meta_audit.py --html index.html --css css/main.css css/tokens.css` → exit 0.
- **T7 — JSON-LD.** В `<head>` валидный `ProfessionalService` + `FAQPage`.
  Тест: извлечь `<script type="application/ld+json">`, прогнать через JSON-валидатор; оба типа присутствуют.
- **T8 — robots/sitemap.** `robots.txt` и `sitemap.xml` существуют в корне.
  Тест: `ls robots.txt sitemap.xml` → оба на месте; `grep 'Sitemap' robots.txt` не пуст.

## §3 Аудит производительности

- **T9 — Lighthouse mobile.** `node audit.js --mobile --threshold 90` → exit 0, все категории ≥ 90.
- **T10 — Lighthouse desktop.** `node audit.js --desktop --threshold 90` → exit 0, все категории ≥ 90.
- Отчёты сохраняются в `.audit/lh-mobile.json`, `.audit/lh-desktop.json`, `.audit/meta.json`.

## §4 Ссылки и интерактив

- **T11 — якоря.** Каждый пункт меню ведёт к существующему `id` на странице.
  Тест: выборка `href="#..."` из меню; каждый `id` найден в `index.html`.
- **T12 — форма заявки.** Контактная форма формирует `mailto:zh_nadi@mail.ru?subject=...`.
  Тест: в `js/main.js` или `index.html` присутствует `mailto:zh_nadi@mail.ru` с темой.
- **T13 — FAQ аккордеон.** Блок FAQ раскрывается/скрывается по клику.
  Тест: в `js/main.js` есть обработчик переключения видимости FAQ-элементов.

## §5 Графика

- **T14 — изображения.** Файлы в `assets/img/` существуют и подключены.
  Тест: `ls assets/img/` → avatar-1..3.png (128×128), office-*.jpg (≥800×600), og-*.png (1200×630);
  каждый `src` в `index.html` указывает на существующий локальный файл (ноль внешних URL).

## Матрица покрытия

| Area | Test | Green? |
|------|------|:------:|
| Структура | T1–T3 | проверяется meta_audit + grep |
| Токены/контраст | T4–T5 | meta_audit exit 0 |
| SEO | T6–T8 | meta_audit + ls |
| Производительность | T9–T10 | Lighthouse ≥ 90 |
| Ссылки/интерактив | T11–T13 | grep по исходникам |
| Графика | T14 | ls + размеры |

> **Rule:** критерий без теста = не критерий. Каждый пункт выше привязан к CR из PRD.
