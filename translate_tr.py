import json
import time
from deep_translator import GoogleTranslator

def translate_text(text):
    if not text or len(text.strip()) == 0:
        return text
    try:
        translated = GoogleTranslator(source='en', target='tr').translate(text[:4500])
        time.sleep(0.3)
        return translated
    except Exception as e:
        print(f"  Error: {e}")
        return text

with open("data/en.json", "r", encoding="utf-8") as f:
    data = json.load(f)

result = []
for i, category in enumerate(data):
    print(f"[{i+1}/{len(data)}] {category['category']}")
    tr_category = category.copy()
    tr_category["category"] = translate_text(category["category"])
    tr_array = []
    for zikr in category["array"]:
        tr_zikr = zikr.copy()
        tr_zikr["text"] = translate_text(zikr["text"])
        tr_array.append(tr_zikr)
    tr_category["array"] = tr_array
    result.append(tr_category)
    with open("data/tr.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

print("Done!")