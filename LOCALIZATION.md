# 🌍 Localization Guide

> "Language should not limit who can benefit from consciousness-first technology. Making our projects multilingual is an act of radical inclusion."

This document provides guidance for internationalization (i18n) and localization (l10n) across Luminous Dynamics projects.

---

## 🎯 Localization Philosophy

### Why Localization Matters

**English-only excludes billions:**
- Only ~400M native English speakers worldwide
- ~1.5B total English speakers (including second language)
- ~6B people speak other languages
- **English-only = serving <25% of humanity**

**Localization is accessibility:**
- Language barriers are real barriers
- Cultural context matters for understanding
- Local adaptation increases adoption
- Respects linguistic diversity

### Core Principles

1. **Internationalize from the Start**
   - Design for translation upfront
   - Don't hard-code strings
   - Avoid cultural assumptions
   - Plan for text expansion/contraction

2. **Community-Driven Translation**
   - Native speakers translate
   - Community reviews for quality
   - Credit translators generously
   - Support with tools and guidance

3. **Cultural Respect**
   - Not just word-for-word translation
   - Adapt idioms and metaphors
   - Respect local norms
   - Consult native speakers

4. **Progressive Localization**
   - Start with highest-impact content
   - Critical docs first, then nice-to-haves
   - Quality over quantity
   - Maintain actively used translations

---

## 🔤 Internationalization (i18n)

### Building for Multiple Languages

**What is i18n?**
Designing software so it CAN be localized without code changes.

### 1. Extract Strings

**❌ Bad (Hard-coded):**
```javascript
const message = "Welcome to Mycelix Protocol";
```

**✅ Good (Extractable):**
```javascript
const message = t('welcome.message'); // Looks up translation
```

### 2. Use i18n Libraries

**JavaScript/React:**
```javascript
import { useTranslation } from 'react-i18n';

function Welcome() {
  const { t } = useTranslation();
  
  return <h1>{t('welcome.title')}</h1>;
}
```

**Python:**
```python
from gettext import gettext as _

def greet_user(name):
    return _("Hello, {name}!").format(name=name)
```

**Rust:**
```rust
use fluent::{FluentBundle, FluentResource};

let message = bundle.get_message("welcome").unwrap();
```

### 3. Handle Pluralization

**Different languages have different plural rules:**

**English:** 1 item, 2+ items  
**Polish:** 1 item, 2-4 items, 5+ items  
**Arabic:** 0, 1, 2, 3-10, 11-99, 100+ items

**✅ Use plural-aware functions:**
```javascript
// English
t('item_count', { count: n })
// → count: 0: "No items"
// → count: 1: "1 item"
// → count: 2: "2 items"

// Library handles plural forms per language
```

### 4. Format Dates and Numbers

**Dates:**
```javascript
// ❌ Bad
const date = "01/15/2025"; // US format, confusing elsewhere

// ✅ Good
const date = new Intl.DateTimeFormat(locale).format(new Date());
// → US: "1/15/2025"
// → UK: "15/1/2025"
// → ISO: "2025-01-15"
```

**Numbers:**
```javascript
// ❌ Bad
const number = "1,234.56"; // US format

// ✅ Good
const number = new Intl.NumberFormat(locale).format(1234.56);
// → US: "1,234.56"
// → DE: "1.234,56"
// → IN: "1,234.56"
```

**Currency:**
```javascript
const price = new Intl.NumberFormat(locale, {
  style: 'currency',
  currency: 'USD'
}).format(42.50);
// → US: "$42.50"
// → DE: "42,50 $"
// → JP: "$42.50"
```

### 5. Support RTL Languages

**Right-to-Left (Arabic, Hebrew, etc.):**

```css
/* Use logical properties */
margin-inline-start: 10px; /* Adapts to text direction */
padding-inline-end: 20px;

/* Not physical properties */
/* margin-left, margin-right (fixed direction) */
```

```html
<html dir="rtl" lang="ar">
  <!-- Content flows right-to-left -->
</html>
```

### 6. Avoid Concatenation

**❌ Bad (Breaks in some languages):**
```javascript
const msg = "Welcome, " + username + "! You have " + count + " messages.";
// Word order varies by language!
```

**✅ Good (Placeholders):**
```javascript
const msg = t('welcome.message', { username, count });
// Translation file can reorder: "{count} messages pour {username}"
```

---

## 🌐 Localization (l10n)

### Translation Workflow

**1. Extract Strings**
```bash
# Extract translatable strings from code
npm run extract-i18n
# Creates: locales/en/messages.json
```

**2. Send for Translation**
- Upload to translation platform (Crowdin, Weblate, Transifex)
- Or share JSON files with translators
- Provide context for each string

**3. Review Translations**
- Native speakers review
- Check for accuracy and tone
- Test in actual UI

**4. Import Translations**
```bash
# Download completed translations
npm run import-i18n
# Creates: locales/es/messages.json, locales/fr/messages.json, etc.
```

**5. Deploy**
- Language selector in UI
- Auto-detect browser language
- Remember user preference

### Translation File Format

**en/messages.json:**
```json
{
  "welcome": {
    "title": "Welcome to Mycelix",
    "subtitle": "Byzantine-resistant federated learning",
    "cta": "Get Started"
  },
  "errors": {
    "network": "Network connection failed. Please check your internet.",
    "auth": "Authentication failed. Please sign in again."
  },
  "item_count": {
    "zero": "No items",
    "one": "{count} item",
    "other": "{count} items"
  }
}
```

**es/messages.json:**
```json
{
  "welcome": {
    "title": "Bienvenido a Mycelix",
    "subtitle": "Aprendizaje federado resistente a Bizantino",
    "cta": "Comenzar"
  },
  "errors": {
    "network": "Falló la conexión de red. Por favor, verifica tu internet.",
    "auth": "Falló la autenticación. Por favor, inicia sesión nuevamente."
  },
  "item_count": {
    "zero": "No hay elementos",
    "one": "{count} elemento",
    "other": "{count} elementos"
  }
}
```

---

## 🎨 Cultural Considerations

### Beyond Words

**1. Colors**
- Red: Danger (West), Celebration (China), Purity (India)
- White: Purity (West), Mourning (East Asia)
- Choose culturally neutral colors or provide themes

**2. Icons and Imagery**
- Hand gestures vary (thumbs up offensive in some cultures)
- Animals have different connotations
- Religious symbols: be very careful
- Use universal icons when possible

**3. Dates and Time**
- Start of week: Sunday (US), Monday (Europe), Saturday (Middle East)
- Calendar systems: Gregorian, Islamic, Hebrew, Chinese
- 12-hour vs 24-hour time

**4. Names**
- Not all names have "first" and "last"
- Some cultures: family name first
- Single names common in some regions
- Don't assume name structure

**5. Text Direction**
- LTR: English, Spanish, French, etc.
- RTL: Arabic, Hebrew, Persian
- Vertical: Traditional Japanese, Chinese

---

## 📝 Documentation Localization

### Priority Order

**1. Critical Docs (Translate First):**
- README.md
- GETTING_STARTED.md
- Installation guides
- Basic tutorials

**2. Important Docs:**
- API documentation
- FAQ.md
- CODE_OF_CONDUCT.md
- CONTRIBUTING.md

**3. Nice to Have:**
- Advanced guides
- Blog posts
- Marketing materials

### Translation Management

**Structure:**
```
docs/
├── en/              # English (source)
│   ├── README.md
│   ├── guide.md
│   └── api.md
├── es/              # Spanish
│   ├── README.md
│   ├── guide.md
│   └── api.md
├── zh/              # Chinese
│   ├── README.md
│   ├── guide.md
│   └── api.md
└── translations.yml # Track translation status
```

**Status Tracking (translations.yml):**
```yaml
languages:
  es:
    name: "Español"
    progress: 85%
    maintainers:
      - "@maria"
    last_updated: "2025-01-10"
  
  zh:
    name: "中文"
    progress: 60%
    maintainers:
      - "@zhang"
    last_updated: "2024-12-15"
```

---

## 👥 Community Translation Programs

### Recruiting Translators

**Where to Find Translators:**
- Existing community members
- Post in community forums
- Translation platforms (Crowdin community)
- University language departments
- Local meetups in target regions

**What to Offer:**
- Credit in CONTRIBUTORS.md
- Localization team role
- Swag/recognition
- Reference letter
- Small stipend (if budget allows)

### Translator Guidelines

**Provide to Translators:**

```markdown
# Translation Guidelines

## Tone and Style

- **Friendly but professional** - We're welcoming, not overly casual
- **Clear over clever** - Accuracy over wordplay
- **Consciousness-first** - Maintain our values in translation

## Technical Terms

**Don't translate (keep English):**
- Product names: Mycelix, Terra Atlas
- Technical terms: API, HTTP, database
- Abbreviations: i18n, l10n, ERC

**Do translate:**
- UI labels: "Submit", "Cancel", "Settings"
- Error messages
- Help text
- Documentation prose

## When Unsure

- Ask in #translation-questions
- Check existing translations in similar projects
- Consult with native speakers
- Default to clarity

## Review Process

1. Submit translation
2. Native speaker reviews
3. Incorporate feedback
4. Merge when approved

Thank you for helping make our projects accessible to [Language] speakers! 💚
```

### Translation Platforms

**Crowdin (Recommended):**
- Free for open source
- Good context for translators
- Translation memory
- Community voting

**Weblate:**
- Free and open source
- Git integration
- Quality checks

**Transifex:**
- Professional features
- Free tier for open source
- API access

---

## 🛠️ Tools and Resources

### i18n Libraries

**JavaScript/React:**
- `react-i18next` - Most popular
- `FormatJS` - Full-featured
- `LinguiJS` - Developer-friendly

**Python:**
- `gettext` - Standard library
- `Babel` - Enhanced i18n
- `Flask-Babel` - For Flask apps

**Rust:**
- `fluent` - Modern localization
- `gettext` - Traditional approach

### Translation Tools

**For Code:**
- `i18next-scanner` - Extract strings
- `babel-plugin-react-intl` - Extract from React

**For Docs:**
- `Crowdin CLI` - Sync docs
- `Transifex CLI` - Upload/download
- `mdbook-i18n` - Multilingual Rust book

### Testing

**Check Translations:**
```javascript
// Automated checks
- Missing translations (keys in source but not in target)
- Extra translations (keys in target but not in source)
- Placeholder consistency ({username} exists in both)
- HTML tag consistency (<strong> tags match)
```

**Visual Testing:**
- Screenshot comparisons
- Manual QA in each language
- RTL layout testing
- Text overflow (German is ~30% longer than English)

---

## 📊 Prioritizing Languages

### Usage Data

**Analyze Your Users:**
```sql
SELECT language, COUNT(*) as users
FROM user_preferences
GROUP BY language
ORDER BY users DESC;
```

### Global Reach

**High-Impact Languages (by speakers):**
1. English (1.5B total)
2. Mandarin Chinese (1.1B)
3. Hindi (600M)
4. Spanish (550M)
5. French (280M)
6. Arabic (280M)
7. Bengali (265M)
8. Russian (260M)
9. Portuguese (265M)
10. Indonesian (200M)

**Tech Community Languages:**
- English (universal)
- Chinese (huge tech community)
- Spanish (Latin America)
- Russian (strong dev community)
- German (Europe)
- Japanese (tech-forward)

### Start Small

**Recommended Progression:**
1. **English** (source language)
2. **Spanish** (widely spoken, Latin America growth)
3. **Mandarin Chinese** (huge market, strong tech community)
4. **French** (Africa, Europe)
5. **Then based on your community needs**

---

## 💚 Consciousness-First Localization

### Values in Translation

**ERC Principles Must Translate:**
- Sacred reciprocity
- Consciousness-first technology
- Meta-Principle of Infinite Love

**Work With Translators:**
- Explain philosophy
- Provide context
- Allow creative adaptation
- Some concepts don't translate literally

**Example:**
```
"Sacred reciprocity" (English)
→ Not just "reciprocidad sagrada" (Spanish)
→ Maybe "reciprocidad consciente" or "intercambio sagrado"
→ Depends on cultural context
→ Ask native speakers!
```

---

## 📚 Related Resources

- **[ACCESSIBILITY.md](./ACCESSIBILITY.md)** - Accessibility includes language
- **[STYLE_GUIDE.md](./STYLE_GUIDE.md)** - Writing standards
- **[CONTRIBUTING.md](./CONTRIBUTING.md)** - Translation contributions
- **[EVENTS.md](./EVENTS.md)** - Multilingual events

---

## 💬 Localization Questions?

- **Want to translate**: #translation Discord channel
- **Technical questions**: GitHub Discussions
- **Suggest new language**: Open issue

---

**Last Updated**: 2025-01-14
**Maintained by**: Localization Working Group

---

> "Every language we support is a door we open. Every translation is an invitation. May our technology speak the languages of the world." 💚🌍
