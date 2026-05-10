import requests
import json
import time
import re

def parse_json(res):
    text = res.content.decode("utf-8-sig", errors="ignore")
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', text)
    return json.loads(text)

def fetch_all(lang_code):
    index_res = requests.get(f"http://www.hisnmuslim.com/api/{lang_code}/husn_{lang_code}.json")
    chapters  = list(parse_json(index_res).values())[0]
    print(f"[{lang_code}] Found {len(chapters)} categories")
    result = []
    for i, chapter in enumerate(chapters):
        chapter_id     = chapter["ID"]
        title          = chapter["TITLE"]
        audio_url      = chapter.get("AUDIO_URL", "")
        audio_filename = audio_url.split("/")[-1].replace(".mp3", "") if audio_url else ""
        try:
            azkar_res  = requests.get(chapter["TEXT"])
            azkar_data = list(parse_json(azkar_res).values())[0]
            array = []
            for j, zikr in enumerate(azkar_data, 1):
                zikr_id = zikr["ID"]
                if lang_code == "ar":
                    text = zikr.get("ARABIC_TEXT", "")
                else:
                    text = zikr.get("TRANSLATED_TEXT", "") or zikr.get("ARABIC_TEXT", "")
                array.append({
                    "id":              j,
                    "text":            text,
                    "transliteration": None,
                    "count":           zikr.get("REPEAT", 1),
                    "audio":           f"/audio/{zikr_id}.mp3",
                    "filename":        str(zikr_id)
                })
            result.append({
                "id":       chapter_id,
                "category": title,
                "audio":    f"/audio/{audio_filename}.mp3" if audio_filename else "",
                "filename": audio_filename,
                "array":    array
            })
            print(f"  [{i+1}/{len(chapters)}] {title}: {len(array)} azkar")
            time.sleep(0.2)
        except Exception as e:
            print(f"  ERROR on {title}: {e}")
    out_file = f"data/{lang_code}.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\nSaved {out_file} — {len(result)} categories\n")

fetch_all("ar")
fetch_all("en")