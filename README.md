<div align="center">

<img src="assets/header.svg" alt="neo-consulting — НЕО КОНСАЛТИНГ" width="100%">

**🌐 Versions:** [English](README.md) · [Русский](README.ru.md) · [Website](https://bestdeejay-design.github.io/neo-consulting/) · [Presentation](https://bestdeejay-design.github.io/neo-consulting/presentation/)

# НЕО КОНСАЛТИНГ — Accounting Outsourcing Landing

Static landing page for **ООО «НЕО КОНСАЛТИНГ»**, an accounting, tax and legal
outsourcing company in Saint Petersburg (ИП / ООО on simplified taxation, УСН).

Built as plain HTML/CSS/JS with zero build tools and **zero external requests** —
all fonts, icons, images and metadata are local-first.

## Audit status

| Check | Result |
|---|---|
| Lighthouse mobile | **100 / 100 / 100 / 100** |
| Lighthouse desktop | **91 / 100 / 100 / 100** (threshold 90) |
| meta_audit | 17/18 passed (1 false positive documented in `.audit/meta-notes.md`) |
| WCAG AA contrast | all text/text-background pairs ≥ 4.5:1 |
| Raw hex outside design tokens | 0 |

## Live site

- **Website:** [bestdeejay-design.github.io/neo-consulting](https://bestdeejay-design.github.io/neo-consulting/)
- **Sales presentation:** [bestdeejay-design.github.io/neo-consulting/presentation](https://bestdeejay-design.github.io/neo-consulting/presentation/)

## Quick start

```bash
# open directly
open index.html

# or serve locally
python3 -m http.server 8377
```

## Features

- **16 landing sections** (`hero`, `problems`, `solution`, `services`, `details`,
  `audience`, `pricing`, `process`, `about`, `team`, `gallery`, `guarantees`, `cases`,
  `reviews`, `faq`, `contacts`) with anchor navigation
- **Photo rotation**: 8 local 4:3 photos shuffled across 8 `data-slot` positions on
  every page load (hero draws from a priority pool, duplicates within a page are
  excluded, the last hero is remembered in `localStorage`, graceful fallback to
  default `src` without JS)
- **Semantic HTML**: single `<h1>`, WCAG heading hierarchy, native `<details>/<summary>`
  FAQ accordion, table tariffs with mobile horizontal scroll
- **Design tokens**: all colors declared once in `css/tokens.css` (`:root`), zero raw
  hex outside the token block; restrained fir-green accent `#2E5E4E`
- **Accessibility**: 4.5:1 contrast, `:focus-visible` states, 44px+ tap targets,
  `scroll-padding-top` for the sticky header, ARIA labels
- **SEO layer**: canonical, Open Graph / Twitter cards (1200×630), JSON-LD
  `ProfessionalService` + `FAQPage`, `robots.txt`, `sitemap.xml`, favicon
- **Local images only**: generated avatars, office photos, OG image — no CDN
- **Responsive**: mobile-first, breakpoints at 640px and 960px, hamburger menu
- **Sales presentation**: self-contained 12-slide interactive deck (`presentation/`) — speaker notes, timer, keyboard navigation

## Repository structure

```
.
├── index.html              # landing page (16 sections, JSON-LD, OG/Twitter)
├── presentation/
│   └── index.html          # interactive sales presentation (12 slides, self-contained)
├── css/
│   ├── tokens.css          # design tokens (:root custom properties)
│   └── main.css            # styles (mobile-first)
├── js/
│   ├── main.js             # menu toggle, current year, escape/resize close
│   └── photos.js           # photo rotation across data-slot positions
├── assets/
│   ├── img/                # avatars, og-image, favicon
│   │   └── photos/         # rotation pool: photo-01..09.webp (4:3)
│   ├── header.svg          # animated README header (SMIL)
│   └── footer.svg          # animated README footer (SMIL)
├── docs/
│   ├── content.md          # copy for all 14 blocks
│   ├── VISION.md           # product docs (L1)
│   ├── PRD.md
│   ├── ROADMAP.md
│   ├── TEST_PLAN.md
│   ├── DECISIONS.md
│   └── plans/              # build plan
├── robots.txt
├── sitemap.xml
└── .github/                # issue templates, PR template
```

## Documentation

Product documentation (L1) lives in [`docs/`](docs/): VISION, PRD, ROADMAP,
TEST_PLAN and DECISIONS. All 14 blocks of copy are in [`docs/content.md`](docs/content.md).

---

<img src="assets/footer.svg" alt="bestdeejay-design — neo-consulting" width="100%">

</div>