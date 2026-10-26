# DESIGN SYSTEM — НЕО КОНСАЛТИНГ

## Design Soul

### 1. COLOR — Палитра, которая говорит

**Основная палитра**:
- **Primary**: #2E5E4E (fir-green) — доверие, стабильность, профессионализм
- **Secondary**: #1A1A2E (deep navy) — серьёзность, глубина
- **Accent**: #E8B931 (gold) — теплота, ценность, человечность

**Фон**:
- **Light**: #F8F7F4 (warm white) — чистота, воздух
- **Dark**: #0F0F1A (midnight) — для контрастных слайдов

**Текст**:
- **Primary**: #1A1A2E (deep navy) — основной текст
- **Secondary**: #4A5568 (gray) — подписи, вторичный текст
- **Inverse**: #F8F7F4 (warm white) — на тёмном фоне

**Семантика**:
- **Success**: #2E5E4E (fir-green) — положительные результаты
- **Warning**: #E8B931 (gold) — внимание, важные моменты
- **Error**: #C53030 (red) — ошибки, штрафы

**Почему эта палитра**:
- Fir-green = природа, стабильность, рост (не «корпоративный синий»)
- Gold = человечность, ценность (не «холодный серый»)
- Deep navy = серьёзность без агрессии

---

### 2. TYPOGRAPHY — Иерархия, которая ведёт

**Шрифт**: Inter (или System Font Stack)

**7 уровней**:

| Уровень | Размер | Вес | Роль |
|---------|--------|-----|------|
| **L1: Title** | 48-64px | Black | Захватить. Это название фильма. |
| **L2: Chapter** | 36-48px | Bold | Напомнить, где мы. Это название акта. |
| **L3: Slide Title** | 28-36px | Semibold | Главная мысль слайда. Это приговор. |
| **L4: Key Stat** | 48-72px | Black | Шокировать числом. Это кульминация. |
| **L5: Body** | 18-24px | Regular | Объяснить. Не перегрузить. |
| **L6: Caption** | 14-16px | Light | Уточнить. Для тех, кто хочет подробностей. |
| **L7: Footnote** | 10-12px | Light | Дать ссылку. Для тех, кто проверяет. |

**Правила**:
- Интерлиньяж: 1.4 для заголовков, 1.6 для текста
- Максимум 3 уровня на одном слайде
- Key Stat = всегда отдельный элемент

---

### 3. SPACING — Ритм, который дышит

**Базовый модуль**: 8px

**Отступы**:
- **Small**: 8px — между элементами внутри карточки
- **Medium**: 16px — между карточками
- **Large**: 32px — между секциями
- **XL**: 64px — между главными блоками

**Правило воздуха**:
- между идеями = время для осмысления
- На каждом слайде минимум 20% свободного пространства
- Никогда не заполнять экран полностью

---

### 4. SHAPE — Форма, которая характеризует

**Основные формы**:
- **Карточки**: скругление 12px — человечность, мягкость
- **Кнопки**: скругление 8px — точность, решимость
- **Иконки**: Lucide Icons, line style, strokeWidth 1.5-2 — чистота, современность

**Почему Lucide Icons**:
- MIT лицензия — бесплатно для коммерческого использования
- 1400+ иконок — покрывают любые потребности
- Consistent line style — единый визуальный язык
- SVG формат — масштабируются без потери качества
- Не зависят от шрифтов — работают везде

**Почему inline SVG (не emoji, не icon fonts)**:
- Контроль над strokeWidth и размерами
- Возможность стилизовать через CSS (currentColor)
- Не ломаются при отсутствии шрифтов
- Лучшая доступность (aria-label)

**Почему скруглённые**:
- Мягкие формы = человечность, доверие
- Острые = точность, но могут быть агрессивными
- 12px = баланс между мягкостью и серьёзностью

---

### 5. DEPTH — Слои, которые создают мир

**Уровни**:
- **Front**: тень 0 4px 12px rgba(0,0,0,0.1) — активные элементы
- **Middle**: тень 0 2px 8px rgba(0,0,0,0.08) — карточки
- **Back**: тень 0 1px 4px rgba(0,0,0,0.05) — фоновые элементы

**Принцип**:
- передний план = действие
- фон = контекст
- Глубина создаёт иерархию

---

### 6. COMPONENTS — Элементы, которые повторяются

**Иконки**:
- **Набор**: Lucide Icons (MIT, 1400+ иконок)
- **Стиль**: Line icons, strokeWidth 1.5-2
- **Размер**: 48px (service cards), 20px (inline), 16px (navigation)
- **Цвет**: наследует от родителя (currentColor)
- **Формат**: Inline SVG (не emoji, не font icons)

**Карточка**:
```
background: white
border-radius: 12px
padding: 24px
shadow: 0 2px 8px rgba(0,0,0,0.08)
```

**Метрика**:
```
Число: L4 (48-72px, Black)
Подпись: L6 (14-16px, Light)
Отступ: 16px между числом и подписью
```

**Иконка**:
```
Размер: 48px
Стиль: line, 2px stroke
Цвет: Primary (#2E5E4E)
```

**Кнопка**:
```
background: Primary
color: white
padding: 12px 24px
border-radius: 8px
hover: darkens 10%
```

---

### 7. MOTION — Движение, которое рассказывает

**Типы анимаций**:
- **Появление**: opacity 0 → 1, duration 0.6s, ease-out
- **Сдвиг**: translateY(20px) → 0, duration 0.6s, ease-out
- **Пауза между элементами**: 0.2s

**Правила**:
- появление = рождение идеи
- исчезновение = завершение мысли
- Анимация должна быть незаметной — она помогает, не раздражает

**Задержки**:
- Заголовок: 0s
- Текст: 0.2s
- Метрика: 0.4s
- Иконка: 0.6s

---

## Composition Grammar

**Используемые типы слайдов**:

| Слайд | Тип | Описание |
|-------|-----|----------|
| 1. Hero | Hero Slide | Одна мысль на весь экран |
| 2. Problem | Metrics Slide | Три ключевых числа |
| 3. Complication | Split Slide | Лево/право сравнение |
| 4. Question | Statement Slide | Крупный текст, воздух |
| 5. Answer | Hero Slide | Три аргумента |
| 6. Proof | Comparison Slide | Три案例 «до/после» |
| 7. Why Us | Statement Slide | Факты + философия |
| 8. Services | List Slide | Пять карточек |
| 9. Pricing | Table Slide | Три колонки |
| 10. Process | Timeline Slide | Пять шагов |
| 11. CTA | Statement Slide | Контакты |
| 12. One More Thing | Statement Slide | Философия |

---

## Uniqueness Gate

**Проверка каждого слайда**:

- [ ] Есть ли здесь что-то, чего НЕ было бы в типичной бухгалтерской презентации?
- [ ] Если убрать логотип, будет ли понятно, ЧЬЯ это презентация?
- [ ] Есть ли здесь «момент для скриншота» — слайд, который захотят сохранить?
- [ ] Если бы этот слайд показали без контекста, вызовет ли он эмоцию?
- [ ] Соответствует ли этот слайд Design Soul или выглядит как шаблон?

**Прохождение**: 5/5 = «да» = слайд готов. Меньше 5 = переделать.

### Проверка иконок
- [ ] Все иконки — inline SVG из Lucide Icons (не emoji, не font icons)
- [ ] Размер иконок соответствует контексту (48px для карточек, 20px для inline)
- [ ] Иконки стилизованы через CSS (currentColor, stroke-width)
- [ ] Иконки имеют aria-label для доступности

---

## Палитра для кода

```css
:root {
  /* Colors */
  --color-primary: #2E5E4E;
  --color-secondary: #1A1A2E;
  --color-accent: #E8B931;
  --color-bg-light: #F8F7F4;
  --color-bg-dark: #0F0F1A;
  --color-text-primary: #1A1A2E;
  --color-text-secondary: #4A5568;
  --color-text-inverse: #F8F7F4;
  --color-success: #2E5E4E;
  --color-warning: #E8B931;
  --color-error: #C53030;
  
  /* Typography */
  --font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-size-l1: clamp(48px, 6vw, 64px);
  --font-size-l2: clamp(36px, 4vw, 48px);
  --font-size-l3: clamp(28px, 3vw, 36px);
  --font-size-l4: clamp(48px, 6vw, 72px);
  --font-size-l5: clamp(18px, 2vw, 24px);
  --font-size-l6: clamp(14px, 1.5vw, 16px);
  --font-size-l7: clamp(10px, 1vw, 12px);
  
  /* Spacing */
  --space-xs: 8px;
  --space-sm: 16px;
  --space-md: 24px;
  --space-lg: 32px;
  --space-xl: 64px;
  
  /* Shadows */
  --shadow-front: 0 4px 12px rgba(0,0,0,0.1);
  --shadow-middle: 0 2px 8px rgba(0,0,0,0.08);
  --shadow-back: 0 1px 4px rgba(0,0,0,0.05);
  
  /* Border Radius */
  --radius-card: 12px;
  --radius-button: 8px;
  
  /* Transitions */
  --transition-default: 0.6s ease-out;
  --transition-fast: 0.3s ease-out;
}
```
