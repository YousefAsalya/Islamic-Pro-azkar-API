<div align="center">

# 🕌 Islamic Pro — Azkar API

**[English](#english) | [العربية](#arabic)**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Languages](https://img.shields.io/badge/Languages-3_available-blue.svg)](#languages)
[![Categories](https://img.shields.io/badge/Categories-132-orange.svg)](#)
[![Adhkar](https://img.shields.io/badge/Adhkar-185-purple.svg)](#)

</div>

---

<a name="english"></a>
## 🇬🇧 English

### What is this?

An open-source structured JSON dataset of **Hisn Al-Muslim** (Fortress of the Muslim) adhkar by Sheikh Sa'eed Al-Qahtani — with multilingual support, repeat counts, and local audio files.

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

### 📁 Project Structure

```
Islamic-Pro-azkar-API/
├── data/
│   ├── ar.json             ← Arabic source data
│   ├── en.json             ← English (complete)
│   └── tr.json             ← Turkish (complete)
├── audio/                  ← 267 MP3 audio files
│   ├── 1.mp3
│   ├── 2.mp3
│   └── ar_7esn_AlMoslem_by_Doors_028.mp3 ...
├── LICENSE
└── README.md
```

---

### 📖 Data Structure

Each language file follows the same structure:

```json
[
  {
    "id": 1,
    "category": "Words of remembrance for morning and evening",
    "audio": "/audio/ar_7esn_AlMoslem_by_Doors_028.mp3",
    "filename": "ar_7esn_AlMoslem_by_Doors_028",
    "array": [
      {
        "id": 1,
        "text": "Allah - there is no deity except Him, the Ever-Living...",
        "transliteration": "Recite Ayat-Al-Kursiy (Al-Baqarah :255)",
        "count": 1,
        "audio": "/audio/75.mp3",
        "filename": "75"
      }
    ]
  }
]
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
const ar = require('./data/ar.json');
const en = require('./data/en.json');

const morning = en.find(cat => cat.id === 1);

const text      = morning.array[0].text;
const count     = morning.array[0].count;
const audioFile = morning.array[0].audio;
```

**Flutter / Dart**
```dart
final String json = await rootBundle.loadString('assets/data/ar.json');
final List   data = jsonDecode(json);
final category    = data[0];
final text        = category['array'][0]['text'];
final count       = category['array'][0]['count'];
final audio       = category['array'][0]['audio'];
```

**React Native**
```js
import adhkar from './data/en.json';

adhkar.forEach(category => {
  console.log(category.category);
  category.array.forEach(dhikr => {
    console.log(dhikr.text, '×', dhikr.count);
  });
});
```

---

### 🤝 Contributing

Want to add a language? Open a PR with a new `data/<lang>.json` following the same structure as `en.json`.

**Steps:**
1. Fork this repo
2. Create `data/<lang-code>.json` following the same structure
3. Review the translations carefully
4. Open a Pull Request

---

### 🔗 Sources

- Hisn Al-Muslim — Sheikh Sa'eed Al-Qahtani
- Audio recitation — Hamad Al-Durayhim
- [hisnmuslim.com](https://hisnmuslim.com)

---

### 👨‍💻 Author

**Yousef I. M. Asalya** — Senior Flutter Engineer & Co-Founder at [North Plus Studio](https://northplusstudio.com)

Istanbul, Turkey 🇹🇷 · [eng.yousef.asalya@gmail.com](mailto:eng.yousef.asalya@gmail.com)

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
| 🤲 الأذكار | 185 ذكر ودعاء |
| 🌍 اللغات | العربية ✅ · الإنجليزية ✅ · التركية ✅ · 12 لغة قريباً |
| 🔢 حقل `count` | عدد التكرار لكل ذكر |
| 🔊 الصوت | 267 ملف MP3 محلي في مجلد `/audio` |
| 🆓 الترخيص | MIT — مجاني لأي استخدام |

---

### 🌍 اللغات المدعومة

| الكود | اللغة | الحالة |
|-------|-------|--------|
| `ar` | العربية | ✅ مكتمل |
| `en` | English | ✅ مكتمل |
| `tr` | Türkçe | ✅ مكتمل |
| `bn` | বাংলা | 🔜 قريباً |
| `bs` | Bosanski | 🔜 قريباً |
| `es` | Español | 🔜 قريباً |
| `fa` | فارسی | 🔜 قريباً |
| `ha` | Hausa | 🔜 قريباً |
| `hi` | हिन्दी | 🔜 قريباً |
| `id` | Indonesia | 🔜 قريباً |
| `pt` | Português | 🔜 قريباً |
| `so` | Soomaali | 🔜 قريباً |
| `sw` | Kiswahili | 🔜 قريباً |
| `th` | ไทย | 🔜 قريباً |
| `zh` | 中文 | 🔜 قريباً |

---

### 📁 هيكل المشروع

```
Islamic-Pro-azkar-API/
├── data/
│   ├── ar.json             ← المصدر العربي
│   ├── en.json             ← الإنجليزية (مكتملة)
│   └── tr.json             ← التركية (مكتملة)
├── audio/                  ← 267 ملف MP3
│   ├── 1.mp3
│   └── ar_7esn_AlMoslem_by_Doors_028.mp3 ...
├── LICENSE
└── README.md
```

---

### 📖 هيكل البيانات

```json
[
  {
    "id": 1,
    "category": "أذكار الصباح والمساء",
    "audio": "/audio/ar_7esn_AlMoslem_by_Doors_028.mp3",
    "filename": "ar_7esn_AlMoslem_by_Doors_028",
    "array": [
      {
        "id": 1,
        "text": "أَعُوذُ بِاللَّهِ مِنَ الشَّيطَانِ الرَّجِيمِ...",
        "transliteration": null,
        "count": 1,
        "audio": "/audio/75.mp3",
        "filename": "75"
      }
    ]
  }
]
```

#### أهمية حقل `count`

```
count: 1   → يُقرأ مرة واحدة
count: 3   → يُقرأ 3 مرات   → زر تكرار في الواجهة
count: 7   → دعاء الشفاء
count: 33  → تسبيح بعد الصلاة  → عداد نقرات
count: 100 → استغفار يومي    → شريط تقدم
```

---

### 🚀 مثال استخدام

**JavaScript**
```js
const ar = require('./data/ar.json');

const morning = ar.find(cat => cat.id === 1);
console.log(morning.category);          // أذكار الصباح والمساء
console.log(morning.array[0].text);     // نص الذكر
console.log(morning.array[0].count);    // عدد التكرار
console.log(morning.array[0].audio);    // /audio/75.mp3
```

**Flutter / Dart**
```dart
final String raw  = await rootBundle.loadString('assets/data/ar.json');
final List   data = jsonDecode(raw);
final text        = data[0]['array'][0]['text'];
final count       = data[0]['array'][0]['count'];
final audio       = data[0]['array'][0]['audio'];
```

---

### 🤝 المساهمة

نرحب بإضافة اللغات المتبقية! أنشئ ملف `data/<كود-اللغة>.json` بنفس هيكل `en.json` وأرسل Pull Request.

---

### 🔗 المصادر

- كتاب حصن المسلم — الشيخ سعيد بن علي بن وهف القحطاني
- القراءة الصوتية — المحاضر حمد الدريهم
- [hisnmuslim.com](https://hisnmuslim.com)

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
