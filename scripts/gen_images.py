# -*- coding: utf-8 -*-
"""Sovereign Tower 配图生成：Seedream 文生图，手绘宫廷手账统一风格，16:9."""
import os, re, json, time, urllib.request, base64, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets" / "images"
ASSETS.mkdir(parents=True, exist_ok=True)

env = open("/Users/azu/Documents/跨境电商AI系统/.env", encoding="utf-8").read()
m = re.search(r"^ARK_API_KEY=(.+)$", env, re.M)
if not m:
    sys.exit("ARK_API_KEY not found")
API_KEY = m.group(1).strip().strip('"').strip("'").strip()

ENDPOINT = "https://ark.cn-beijing.volces.com/api/v3/images/generations"
MODEL = "doubao-seedream-5-0-pro-260628"

# 「君主的圆桌手账」统一风格：手绘宫廷 + 羊皮纸 + 暖色 + 圆桌骑士
STYLE = ("hand-painted storybook key art in a warm medieval court ledger style, parchment paper texture with "
         "sepia and brass-gold tones, rounded table of knights, candlelight, intricate hand-drawn linework, "
         "watercolor washes in terracotta and olive, cozy atmosphere, high detail, no text, no watermark, no logos, "
         "16:9 widescreen")

PROMPTS = {
  "hero": "A majestic round table in a candlelit tower hall, silhouettes of knights seated around it, a glowing crown on the table, tall windows showing a kingdom at dusk, " + STYLE,
  "how-to-play": "A new sovereign sitting on a throne receiving court petitions, courtiers with scrolls and a map of the kingdom, morning audience scene, " + STYLE,
  "knights": "A gallery of medieval knight portraits hanging on a parchment wall, each in a different crest color, round table shields beneath, " + STYLE,
  "secret-knights": "A mysterious hooded knight in shadow holding a lantern, hidden doorway behind a tapestry, secret recruitment mood, " + STYLE,
  "romance": "A knight offering a bouquet to a stone statue lady in a moonlit tower garden, roses and soft candlelight, romance mood, " + STYLE,
  "endings": "A winding path from a tower to five different castle endings in the distance, dawn light, branching destiny, " + STYLE,
  "recipes": "A rustic wooden kitchen table with six medieval dishes: galette, toasted sandwich, garlic bread, crêpe, shortbread and a taco, recipe cards, " + STYLE,
  "quest-mechanics": "A quest assignment desk with parchment quest orders, scales of justice, knight token pieces and a sand timer, " + STYLE,
  "achievements": "A wall of golden brass achievement medals and ribbons in a castle study, a knight polishing them, trophy mood, " + STYLE,
}

def call(prompt, retries=3):
    body = json.dumps({"model": MODEL, "prompt": prompt, "size": "1600x900",
                       "response_format": "url", "watermark": False}).encode()
    for i in range(retries):
        try:
            req = urllib.request.Request(ENDPOINT, data=body, method="POST", headers={
                "Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=180) as r:
                data = json.loads(r.read().decode())
            items = data.get("data") or []
            if items:
                u = items[0].get("url")
                if u: return u
                b = items[0].get("b64_json")
                if b: return "data:image/jpeg;base64," + b
        except Exception as e:
            print(f"  attempt {i+1} failed: {e}")
            time.sleep(8 * (i + 1))
    return None

def download(url, dest):
    if url.startswith("data:"):
        b64 = url.split(",", 1)[1]
        (ASSETS / dest).write_bytes(base64.b64decode(b64))
        return
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        (ASSETS / dest).write_bytes(r.read())

def main():
    names = sys.argv[1:] or list(PROMPTS.keys())
    for name in names:
        if name not in PROMPTS:
            print(f"跳过未知: {name}"); continue
        dest = f"{name}.jpg"
        if (ASSETS / dest).exists():
            print(f"已存在: {dest}"); continue
        print(f"生成 {name} …")
        url = call(PROMPTS[name])
        if url:
            download(url, dest)
            print(f"  ✅ {dest}")
        else:
            print(f"  ❌ {name} 失败")

if __name__ == "__main__":
    main()
