<div align="center">

# 🕌 Islamic Pro — Azkar API

**[English](#english) | [العربية](#arabic)**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Languages](https://img.shields.io/badge/Languages-15-blue.svg)](#languages)
[![Categories](https://img.shields.io/badge/Categories-132-orange.svg)](#)
[![Adhkar](https://img.shields.io/badge/Adhkar-260+-purple.svg)](#)

</div>

---

<a name="english"></a>
## 🇬🇧 English

### What is this?

An open-source structured JSON dataset of **Hisn Al-Muslim** (Fortress of the Muslim) adhkar by Sheikh Sa'eed Al-Qahtani — with multilingual support, repeat counts, and audio links.

> Built to be the missing standard data source for Islamic apps.

---

### ✨ Features
 
| Feature | Details |
|---------|---------|
| 📚 Categories | 132 categories |
| 🤲 Adhkar | 185 individual adhkar |
| 🌍 Languages | Arabic ✅ · English ✅ · Turkish ✅ · 12 more coming soon |
| 🔢 `count` field | Repeat count for every dhikr |
| 🔊 Audio | 267 local MP3 files in `/audio` |
| 🆓 License | MIT — free for any use |
 
---
 
### 🌍 Supported Languages
 
| Code | Language | Status |
|------|----------|--------|
| `ar` | العربية | ✅ Complete |
| `en` | English | ✅ Complete |
| `tr` | Türkçe | ✅ Complete |
| `bn` | বাংলা | 🔜 Coming soon |
| `bs` | Bosanski | 🔜 Coming soon |
| `es` | Español | 🔜 Coming soon |
| `fa` | فارسی | 🔜 Coming soon |
| `ha` | Hausa | 🔜 Coming soon |
| `hi` | हिन्दी | 🔜 Coming soon |
| `id` | Indonesia | 🔜 Coming soon |
| `pt` | Português | 🔜 Coming soon |
| `so` | Soomaali | 🔜 Coming soon |
| `sw` | Kiswahili | 🔜 Coming soon |
| `th` | ไทย | 🔜 Coming soon |
| `zh` | 中文 | 🔜 Coming soon |
 
---


> **Why are some language fields `null`?**
> The structure is pre-built so contributors can fill it in easily.
> Run `node scripts/fetch-language.js <lang>` to auto-populate from the source API, then review and submit a PR.

---

### 📁 Project Structure

```
Islamic-Pro-azkar-API/
├── أذكار.json              ← Main file (all languages + all adhkar)
├── audio/                  ← MP3 audio files (267 files)
│   ├── 1.mp3
│   ├── 2.mp3
│   └── ar_7esn_AlMoslem_by_Doors_028.mp3 ...
├── data/
│   ├── ar_source.json      ← Arabic source data
│   └── en.json             ← English (after running fetch script)
├── scripts/
│   ├── build.py            ← Rebuild أذكار.json from source
│   └── fetch-language.js   ← Auto-populate a language from API
├── LICENSE
└── README.md
```

---

### 📖 Data Structure

```json
{
  "_project": "Islamic Pro - Azkar API",
  "_version": "1.0.0",
  "_languages": { "ar": {...}, "en": {...}, ... },
  "data": [
    {
      "id": 1,
      "category": {
        "ar": "أذكار الصباح والمساء",
        "en": "Words of remembrance for morning and evening",
        "bn": null
      },
      "audio": "/audio/ar_7esn_AlMoslem_by_Doors_028.mp3",
      "filename": "ar_7esn_AlMoslem_by_Doors_028",
      "array": [
        {
          "id": 1,
          "text": {
            "ar": "أَعُوذُ بِاللَّهِ مِنَ الشَّيطَانِ الرَّجِيمِ...",
            "en": "I seek refuge in Allah from the accursed devil...",
            "bn": null
          },
          "transliteration": "A'udhu billahi min ash-shaytanir rajeem...",
          "count": 1,
          "audio": "/audio/75.mp3",
          "filename": "75"
        }
      ]
    }
  ]
}
```

#### Why `count` matters

```
count: 1   → Recite once
count: 3   → Recite 3 times   → show repeat button in UI
count: 7   → Healing dua
count: 33  → Post-prayer tasbih  → show tap counter
count: 100 → Daily istighfar    → show progress tracker
```

---

### 🚀 Quick Usage

**JavaScript / Node.js**
```js
const data = require('./أذكار.json');

const morning = data.data.find(cat => cat.id === 1);

const arabicText  = morning.array[0].text.ar;
const englishText = morning.array[0].text.en;
const repeatTimes = morning.array[0].count;
const audioFile   = morning.array[0].audio;
```

**Flutter / Dart**
```dart
final String json = await rootBundle.loadString('assets/أذكار.json');
final data     = jsonDecode(json);
final category = data['data'][0];
final text     = category['array'][0]['text']['ar'];
final count    = category['array'][0]['count'];
final audio    = category['array'][0]['audio'];
```

**React Native**
```js
import adhkar from './أذكار.json';

const lang = 'en'; // or 'ar'
adhkar.data.forEach(category => {
  console.log(category.category[lang]);
  category.array.forEach(dhikr => {
    console.log(dhikr.text[lang], '×', dhikr.count);
  });
});
```

---

### 🔧 Scripts (for contributors)

Requirements: Python 3.8+ and Node.js 18+

```bash
# Fetch a language and auto-merge into أذكار.json
node scripts/fetch-language.js en
node scripts/fetch-language.js id es bn

# Fetch ALL languages at once
node scripts/fetch-language.js all

# Rebuild the main file from scratch
python3 scripts/build.py
```

---

### 🤝 Contributing

We especially need help with the 13 remaining languages!

**Steps:**
1. Fork this repo
2. Run `node scripts/fetch-language.js <lang-code>`
3. Review the translations carefully
4. Open a Pull Request

---

### 📄 License

**MIT** — Use freely in any project, commercial or otherwise.

---

<a name="arabic"></a>
## 🇸🇦 العربية

### ما هو هذا المشروع؟

مجموعة بيانات JSON مفتوحة المصدر لأذكار **حصن المسلم** للشيخ سعيد بن علي بن وهف القحطاني — مع دعم متعدد اللغات، وعداد التكرار، وملفات صوت محلية.

> الهدف أن يكون المصدر القياسي المفتوح لبيانات الأذكار لتطبيقات الهواتف والمواقع.

---

### ✨ المميزات

| الميزة | التفاصيل |
|--------|----------|
| 📚 الفئات | 132 فئة |
| 🤲 الأذكار | 260+ ذكر ودعاء |
| 🌍 اللغات | 15 لغة (AR ✅ EN ✅ + 13 جاهزة للمساهمة) |
| 🔢 حقل `count` | عدد التكرار لكل ذكر |
| 🔊 الصوت | ملفات MP3 محلية في مجلد `/audio` |
| 🆓 الترخيص | MIT — مجاني لأي استخدام |

---

### 🌍 اللغات المدعومة

| الكود | اللغة | الحالة |
|-------|-------|--------|
| `ar` | العربية | ✅ مكتمل |
| `en` | English | ✅ مكتمل |
| `bn` | বাংলা | 🤝 بحاجة مساهمة |
| `bs` | Bosanski | 🤝 بحاجة مساهمة |
| `es` | Español | 🤝 بحاجة مساهمة |
| `fa` | فارسی | 🤝 بحاجة مساهمة |
| `ha` | Hausa | 🤝 بحاجة مساهمة |
| `hi` | हिन्दी | 🤝 بحاجة مساهمة |
| `id` | Indonesia | 🤝 بحاجة مساهمة |
| `pt` | Português | 🤝 بحاجة مساهمة |
| `so` | Soomaali | 🤝 بحاجة مساهمة |
| `sw` | Kiswahili | 🤝 بحاجة مساهمة |
| `th` | ไทย | 🤝 بحاجة مساهمة |
| `yo` | Yoruba | 🤝 بحاجة مساهمة |
| `zh` | 中文 | 🤝 بحاجة مساهمة |

> **لماذا بعض اللغات `null`؟**
> الهيكل جاهز مسبقاً لتسهيل المساهمة. شغّل `node scripts/fetch-language.js <lang>` لجلبها تلقائياً ثم راجعها وأرسل Pull Request.

---

### 📁 هيكل المشروع

```
Islamic-Pro-azkar-API/
├── أذكار.json              ← الملف الرئيسي (كل اللغات + كل الأذكار)
├── audio/                  ← ملفات الصوت MP3 (267 ملف)
│   ├── 1.mp3
│   ├── 2.mp3
│   └── ar_7esn_AlMoslem_by_Doors_028.mp3 ...
├── data/
│   ├── ar_source.json      ← المصدر العربي الأصلي
│   └── en.json             ← الإنجليزية (بعد تشغيل السكريبت)
├── scripts/
│   ├── build.py            ← إعادة بناء أذكار.json
│   └── fetch-language.js   ← جلب لغة تلقائياً من API
├── LICENSE
└── README.md
```

---

### 📖 هيكل البيانات

```json
{
  "id": 1,
  "category": {
    "ar": "أذكار الصباح والمساء",
    "en": "Words of remembrance for morning and evening",
    "bn": null
  },
  "audio": "/audio/ar_7esn_AlMoslem_by_Doors_028.mp3",
  "array": [
    {
      "id": 1,
      "text": {
        "ar": "أَعُوذُ بِاللَّهِ...",
        "en": "I seek refuge in Allah...",
        "bn": null
      },
      "count": 1,
      "audio": "/audio/75.mp3"
    }
  ]
}
```

#### أهمية حقل `count`

```
count: 1   → يُقرأ مرة واحدة
count: 3   → يُقرأ 3 مرات   → زر تكرار في الواجهة
count: 7   → دعاء الشفاء
count: 33  → تسبيح بعد الصلاة  → عداد
count: 100 → استغفار يومي    → تتبع التقدم
```

---

### 🔧 السكريبتات (للمطورين والمساهمين)

المتطلبات: Python 3.8+ و Node.js 18+

```bash
# جلب لغة ودمجها في أذكار.json
node scripts/fetch-language.js en
node scripts/fetch-language.js id es bn

# جلب جميع اللغات دفعة واحدة
node scripts/fetch-language.js all

# إعادة بناء الملف الرئيسي من الصفر
python3 scripts/build.py
```

---

### 🤝 المساهمة

نرحب بالمساهمات، خاصة ترجمة الـ 13 لغة المتبقية!

**الخطوات:**
1. افعل Fork للمستودع
2. شغّل `node scripts/fetch-language.js <كود-اللغة>`
3. راجع الترجمات للتأكد من صحتها
4. أرسل Pull Request

---

### 🔗 المصادر

- كتاب حصن المسلم — الشيخ سعيد بن علي بن وهف القحطاني
- القراءة الصوتية — المحاضر حمد الدريهم
- الموقع الأصلي — [hisnmuslim.com](https://hisnmuslim.com)

---

### 👨‍💻 المطوّر
 
**يوسف عسلية**  | Flutter Engineer | Co-founder @ North Plus Studio. 
إسطنبول، تركيا 🇹🇷 · [eng.yousef.asalya@gmail.com](mailto:eng.yousef.asalya@gmail.com)
 
```dart
class YousefAsalya {
  final String role     = "Senior Flutter Engineer & Co-Founder";
  final String studio   = "North Plus Studio — northplusstudio.com";
  final String degree   = "MSc Cybersecurity — Yıldız Teknik Üniversitesi";
  List<String> skills   = [
    "Flutter / Dart",
    "Cybersecurity & Penetration Testing",
    "AI Integration",
    "Clean Architecture",
  ];
}
```
 
---

### 📄 الترخيص

**MIT** — استخدم الملفات كيفما شئت، تجارياً أو مجاناً.

---

<div align="center">

*اللَّهُمَّ إِنِّي أَسْأَلُكَ عِلْماً نَافِعاً، وَرِزْقاً طَيِّباً، وَعَمَلاً مُتَقَبَّلاً*

⭐ Star this repo if it helped you!

</div>
