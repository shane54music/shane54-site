#!/usr/bin/env python3
"""Epizód-előkészítő: MP3-mappából kiolvassa a címet, hosszt és a beágyazott borítót.

Használat:
    pip install mutagen pillow
    python3 make_episodes.py <mp3-mappa> <internet-archive-azonosító>

Kimenet: site_src/episodes.json és site_src/ep/001.jpg ...
Sorrend: fájlnév szerint növekvő (a lejátszó a legújabbat mutatja elöl, ha kell, fordítsd: --reverse).
"""
import sys, os, json, io, glob
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from PIL import Image

args = [a for a in sys.argv[1:] if not a.startswith("--")]
if len(args) < 2:
    sys.exit(__doc__)
folder, ia = args[0], args[1]
files = sorted(glob.glob(os.path.join(folder, "*.mp3")))
if "--reverse" in sys.argv:
    files.reverse()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site_src")
os.makedirs(os.path.join(out, "ep"), exist_ok=True)
eps = []
for i, f in enumerate(files, 1):
    m = MP3(f)
    try:
        t = ID3(f)
    except Exception:
        t = {}
    title = str(t["TIT2"]) if "TIT2" in t else os.path.splitext(os.path.basename(f))[0]
    sub = str(t["TPE1"]) if "TPE1" in t else ""
    if "TDRC" in t:
        sub = (sub + " · " if sub else "") + str(t["TDRC"])
    art = ""
    pics = [v for k, v in t.items() if k.startswith("APIC")] if t else []
    if pics:
        im = Image.open(io.BytesIO(pics[0].data)).convert("RGB")
        im.thumbnail((400, 400))
        art = f"ep/{i:03d}.jpg"
        im.save(os.path.join(out, art), quality=82, optimize=True)
    eps.append({"title": title, "sub": sub, "file": os.path.basename(f),
                "dur": round(m.info.length), "art": art})
    print(i, title, "| borító:", bool(art))
json.dump({"ia": ia, "episodes": eps}, open(os.path.join(out, "episodes.json"), "w"),
          ensure_ascii=False, indent=1)
print("Kész:", len(eps), "epizód ->", out)
