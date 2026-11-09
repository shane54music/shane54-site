#!/usr/bin/env python3
"""Shane 54 website builder (phone-first, HU/EN).
python3 build_site.py  ->  dist/   (upload/push dist/ to the host; relative links, works under any path)
Edit the text in CONTENT below, add images to site_src/img/.
"""
import shutil, html
from pathlib import Path

ROOT = Path(__file__).parent
SRC, OUT = ROOT / "site_src", ROOT / "dist"
LANGS = ["hu", "en"]
SECTIONS = ["art", "plugins", "music", "animation"]
ACCENT = {"art": "#ff8fb1", "plugins": "#ffc21a", "music": "#5ad1ff", "animation": "#ff8a3d"}
TILE = {"art": ("p01.jpg", "50% 55%"), "plugins": ("delay_ui.jpg", "12% 50%"),
        "music": ("dj.jpg", "50% 75%"), "animation": ("p08.jpg", "50% 50%")}
SPOTIFY = "2ITbqEgyp32vL3BxEFmQ1V"
DISCOGS = "https://www.discogs.com/artist/18440-Shane-54"

T = {  # UI texts
    "art": {"hu": "ART", "en": "ART"}, "plugins": {"hu": "PLUGINS", "en": "PLUGINS"},
    "music": {"hu": "MUSIC", "en": "MUSIC"}, "animation": {"hu": "ANIMATION", "en": "ANIMATION"},
    "sub_art": {"hu": "110 festmény", "en": "110 paintings"},
    "sub_plugins": {"hu": "Space Cat Delay · Berlin School · Reverb", "en": "Space Cat Delay · Berlin School · Reverb"},
    "sub_music": {"hu": "Számok · mixek · podcast", "en": "Tracks · mixes · podcast"},
    "sub_animation": {"hu": "Zenei videók, animátorként", "en": "Music videos, as an animator"},
    "bio": {"hu": "BIO", "en": "BIO"}, "gallery": {"hu": "GALÉRIA", "en": "GALLERY"},
    "delay": {"hu": "DELAY", "en": "DELAY"}, "disco": {"hu": "DISZKOGRÁFIA", "en": "DISCOGRAPHY"},
    "id": {"hu": "ID", "en": "ID"}, "videos": {"hu": "MUSIC VIDEOS", "en": "MUSIC VIDEOS"},
    "discogs_full": {"hu": "Teljes lista a Discogson →", "en": "Full list on Discogs →"},
    "open_yt": {"hu": "Megnyitás a YouTube-on", "en": "Open on YouTube"},
    "back": {"hu": "← MUSIC", "en": "← MUSIC"},
}

CONTENT = {
    "art_bio": {
        "hu": "A festés ugyanabból a helyből jön, mint a zene. Eddig 110 körüli kép gyűlt össze, nagyrészt macskák. Az egyik macskafej-festményemből lett a Space Cat Delay logója is.",
        "en": "Painting comes from the same place as the music. About 110 pieces so far, mostly cats. One of my cat-head paintings also became the face of the Space Cat Delay."},
    "plugins_bio": {
        "hu": "Karakteres effektek és hangszerek, amiket elsősorban magamnak építek. A Space Cat Delay a Korg Monotron Delay önoszcilláló, zajos világából indult: nem tiszta delay, hanem hangulatgyár. A Berlin School és a Space Cat Reverb készülőben van.",
        "en": "Characterful effects and instruments, built first of all for myself. Space Cat Delay grew out of the self-oscillating, noisy world of the Korg Monotron Delay: not a clean delay but an atmosphere machine. Berlin School and Space Cat Reverb are on the way."},
    "music_bio": {
        "hu": "Trance és progresszív: saját számok, mixek és élő szettek. A producer és a színpad ugyanaz az ember, rendezvényeket is szervezek.",
        "en": "Trance and progressive: my own tracks, mixes and live sets. The producer and the stage are the same person, and I organise events too."},
    "anim_bio": {
        "hu": "Animátorként zenei videókat is készítek: ezek közül válogatás.",
        "en": "As an animator I also make music videos. A selection of them below."},
    "id_bio": {
        "hu": "Az International Departures a podcastom volt. Évekkel ezelőtt véget ért, az archívumot később újra elérhetővé teszem itt.",
        "en": "International Departures was my podcast. It ended years ago; I will make the archive available here again."},
    "id_soon": {"hu": "Az archívum hamarosan feltöltődik.", "en": "The archive is coming soon."},
    "more_plugins": {"hu": "TOVÁBBI PLUGINEK", "en": "MORE PLUGINS"},
    "coming": {"hu": "Készülőben", "en": "In development"},
    "delay_tag": {"hu": "Atmospheric Echo Machine", "en": "Atmospheric Echo Machine"},
    "delay_btn": {"hu": "LETÖLTÉS: HAMAROSAN", "en": "DOWNLOAD: COMING SOON"},
    "delay_fmt": {"hu": "VST3 · AU · macOS", "en": "VST3 · AU · macOS"},
}

PAINTINGS = [("p06", "Wood-collage cat"), ("p03", "Black cat, red ears"), ("p01", "Upside-down cat"),
             ("p07", "Cat eyes"), ("p02", "Grey tabby"), ("p04", "Two happy cats"),
             ("p05", "Two cats, sunglasses"), ("p08", "Two cats at the bar"),
             ("p09", "Blue geometric cat"), ("p10", "Fat blue striped cat")]

VIDEOS = [("RMMwct1Lm44", "Panic Attack", "Shane 54 x Alex Sonata & TheRio"),
          ("LJda5fIwFnw", "Personal Jesus", "Cubicore feat Shane 54"),
          ("5Si-w321k68", "Tiltott Szerelem", "Császár Előd x Lotfi Begi feat Nika"),
          ("YNprCkN3OY8", "Kócos", "Zséda"),
          ("9UwBUl_kPkE", "Az Első És Utolsó", "New Level Empire x Curtis"),
          ("7aUA37jTRuo", "Startup", "Honeybeast")]

MYON = [("2016", "Round We Go", "Myon & Shane 54 x Haley", "", "SINGLE"),
        ("2015", "Wicked Game", "", "Ride Recordings", "SINGLE"),
        ("2014", "Under Your Cloud", "Myon & Shane 54 + Late Night Alumni", "Ride Recordings", "SINGLE"),
        ("2014", "If I Fall (Remixes)", "Cole Plante feat. Myon & Shane 54 & Ruby O'Dell", "Hollywood Records", "EP"),
        ("2014", "Summer Of Love", "Myon & Shane 54 + Kyler England", "Ride Recordings", "SINGLE"),
        ("2013", "Strangers", "Seven Lions with Myon & Shane 54 feat. Tove Lo", "Casablanca", "SINGLE"),
        ("2013", "In Search Of Sunrise 11: Las Vegas", "Richard Durand with Myon & Shane 54", "Songbird", "MIX"),
        ("2013", "Lie To Me", "Cole Plante with Myon & Shane 54 feat. Koko Laroo", "Teknicole", "SINGLE"),
        ("2013", "Lights", "Myon & Shane 54 with Aruna", "Ride Recordings", "SINGLE"),
        ("2013", "Outshine", "Myon & Shane 54 with Natalie Peris", "Ride Recordings", "SINGLE"),
        ("2013", "Hurricane", "Myon & Shane 54 with Amy Pearson", "Ride Recordings", "SINGLE"),
        ("2013", "Éjjel-Nappal Budapest", "Myon & Shane 54 feat. Tóth Gabi", "Ride Recordings", "SINGLE"),
        ("2012", "International Departures, Vol. 2 - Summer Of Love", "Myon & Shane 54", "Armada Digital", "COMP"),
        ("2011", "Futuristic", "Myon & Shane 54", "Armind", "SINGLE"),
        ("2011", "International Departures", "Myon & Shane 54", "Armind", "SINGLE"),
        ("2010", "International Departures Soundtracks", "Myon & Shane 54", "Armada Digital", "COMP"),
        ("2010", "Ibiza Sunrise", "Myon & Shane 54 feat. Labworks", "Armind", "SINGLE"),
        ("2009", "Helpless", "Myon & Shane 54 feat. Aruna", "S107 Recordings", "SINGLE"),
        ("2009", "All Night Rock And Roll", "Myon & Shane 54", "Jigsaw Digital", "SINGLE"),
        ("2008", "Not A Lot Left / The Beach", "Myon & Shane 54", "Anjunabeats", "SINGLE"),
        ("2008", "Trapped", "Myon & Shane 54", "In Trance We Trust", "SINGLE"),
        ("2008", "Vampire", "Myon & Shane 54 feat. Carrie Skipper", "Armind", "SINGLE")]

SOLO = [("2007", "1000 Lullabies", "", "Shah-Music Digital", "DIGITAL"),
        ("2006", "Laptop DJ", "", "EMI", "ALBUM"),
        ("2006", "Altass El", "Shane 54 feat. Mester Tamás", "EMI", "PROMO"),
        ("2005", "Kippenvelmeter", "Shane 54 vs Abel Ramos", "DTF Spain", "SINGLE"),
        ("2005", "Futuristic", "Van Eyden & Hampshire feat. Shane 54", "Flux Delux", "SINGLE"),
        ("2004", "VV3", "", "M-RTL Rt.", "SINGLE"),
        ("2004", "My Way", "", "Boring Records", "ALBUM"),
        ("2004", "Back From Your Past", "Misja Helsloot feat. Shane 54", "First Second Records", "SINGLE"),
        ("2003", "69 Remixes", "DJ Junior & Shane 54 feat. Michelle Wild", "", "PROMO"),
        ("2002", "Souvenir De Chine", "", "Afterglow Records", "SINGLE"),
        ("2002", "Equinoxe 4", "", "DTF Recordings", "SINGLE")]

DISCO = [("MYON & SHANE 54 · 2008–2015", "https://www.discogs.com/artist/1239503-Myon-Shane-54", MYON),
         ("SHANE 54 · 2002–2007", DISCOGS, SOLO)]

CSS = """
:root{--bg:#111;--fg:#fff;--mut:#bbb}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font-family:'Inter',Arial,sans-serif;-webkit-text-size-adjust:100%}
a{color:inherit;text-decoration:none}
img{max-width:100%}
.wrap{max-width:560px;margin:0 auto}
.logo{display:flex;align-items:center;gap:8px;min-height:44px}
.logo b{font-family:'Bowlby One',sans-serif;font-weight:400;font-size:24px;line-height:1}
.logo i{font-family:'Bowlby One',sans-serif;font-style:normal;font-size:22px;line-height:1;background:#ffc21a;color:#111;padding:4px 8px 3px;border-radius:8px;transform:rotate(-4deg);display:inline-block}
.top{position:sticky;top:0;z-index:10;background:#111}
.top header{display:flex;align-items:center;justify-content:space-between;padding:8px 20px 4px;min-height:56px}
.lang{font-size:13px;font-weight:700;min-height:44px;display:flex;align-items:center;padding:0 4px}
.strip{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:4px;padding:0 4px 4px}
.strip a{position:relative;height:72px;overflow:hidden;border:3px solid transparent;background:#222}
.strip a.on{border-color:var(--ac)}
.strip img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.strip span{position:absolute;left:0;right:0;bottom:0;padding:14px 4px 4px;background:linear-gradient(to top,rgba(0,0,0,.75),rgba(0,0,0,0));font-size:12px;font-weight:700;letter-spacing:.04em;text-align:center}
.sub{display:flex;gap:6px;padding:4px 8px 8px;background:#111}
.sub a{flex:1;min-width:0;min-height:44px;display:flex;align-items:center;justify-content:center;text-align:center;padding:0 4px;font-size:12px;font-weight:700;letter-spacing:.04em;border-radius:999px;border:2px solid var(--ac);color:var(--ac)}
.sub a.on{background:var(--ac);color:#111}
h1.t{margin:0 0 16px;font-family:'Bowlby One',sans-serif;font-weight:400;font-size:48px;line-height:1.05;color:var(--ac);-webkit-text-stroke:3px #000;paint-order:stroke fill}
section{scroll-margin-top:200px}
.pad{padding:32px 20px 8px}
.bio{margin:0;font-size:17px;line-height:1.55;color:#e6e6e6}
footer{padding:32px 20px 40px;font-size:13px;color:var(--mut);display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}
/* hub */
.hub{display:flex;flex-direction:column;height:100dvh;min-height:640px}
.hub header{display:flex;align-items:center;justify-content:space-between;padding:8px 20px;min-height:56px;flex:none}
.panel{position:relative;flex:1;min-height:120px;overflow:hidden;margin-bottom:4px;background:#222;display:block}
.panel img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.panel .sh{position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.65),rgba(0,0,0,0) 58%)}
.panel .tx{position:absolute;left:16px;right:16px;bottom:12px;display:flex;justify-content:space-between;align-items:flex-end;gap:10px}
.panel small{display:block;font-size:12px;font-weight:700;letter-spacing:.14em;line-height:1.2}
.panel h2{margin:0;font-family:'Bowlby One',sans-serif;font-weight:400;font-size:clamp(34px,9vw,52px);line-height:1.05;color:#fff;-webkit-text-stroke:3px #111;paint-order:stroke fill}
.panel p{margin:0;font-size:13px}
.panel .go{width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:700;color:#111;flex:none}
/* gallery */
.gal{columns:2;column-gap:8px;padding:16px 8px 8px}
.gal a{display:block;margin-bottom:8px;break-inside:avoid}
.gal img{display:block;width:100%;height:auto;background:#222}
.sig{font-family:'Permanent Marker',cursive;color:#bbb;text-align:center;padding:16px 0 8px;font-size:20px}
/* plugin panel */
.plug{margin:16px 12px 0;border:6px solid #1c2333;border-radius:20px;overflow:hidden;background:#171c28}
.plug .st{display:flex;height:10px}
.plug .head{padding:16px 16px 4px}
.plug .head img{display:block;height:auto}
.plug .shot{display:block;width:100%;height:auto;margin-top:12px}
.btn{display:flex;align-items:center;justify-content:center;min-height:56px;border-radius:999px;font-weight:700;font-size:15px;text-align:center}
.plug .actions{padding:16px;display:grid;gap:8px}
.rowc{display:flex;align-items:center;gap:16px;border:2px solid #1c2333;border-radius:16px;padding:14px;margin-bottom:10px;min-height:88px}
.rowc .sw{width:72px;height:72px;border-radius:12px;flex:none}
/* music */
.sp iframe{display:block;width:100%;height:352px;border:0;border-radius:14px}
.disc{padding:8px 20px 0}
.disc .r{display:flex;gap:12px;align-items:center;padding:12px 0;border-top:1px solid #2a2a2a;min-height:56px}
.disc .y{font-size:13px;color:#5ad1ff;font-weight:700;width:40px;flex:none}
.disc .n{flex:1;min-width:0}
.disc .n b{display:block;font-size:15px;line-height:1.3}
.disc .n s{display:block;font-size:12px;color:#bbb;text-decoration:none}
.tag{font-size:11px;font-weight:700;letter-spacing:.08em;border:1.5px solid #5ad1ff;color:#5ad1ff;border-radius:999px;padding:3px 8px;flex:none}
.idc{border:2px solid #5ad1ff;border-radius:14px;padding:18px 16px;display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:88px}
.idc b{font-family:'Bowlby One',sans-serif;font-weight:400;font-size:22px;line-height:1.15;color:#5ad1ff}
/* videos */
.vid{display:block;margin-bottom:28px}
.vid .th{position:relative;aspect-ratio:16/9;background:#333;overflow:hidden;cursor:pointer}
.vid .th img,.vid .th iframe{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;border:0}
.vid .pl{position:absolute;left:50%;top:50%;width:64px;height:64px;margin:-32px 0 0 -32px;border-radius:50%;background:#111;display:flex;align-items:center;justify-content:center;border:0;padding:0}
.vid .pl:after{content:"";margin-left:5px;border-left:20px solid #fff;border-top:12px solid transparent;border-bottom:12px solid transparent}
.vid .m{padding:10px 20px 0}
.vid .m b{display:block;font-size:17px}
.vid .m span{display:block;font-size:14px;color:#bbb}
"""

JS = """
document.addEventListener('click',function(e){
  var t=e.target.closest('[data-yt]'); if(!t) return;
  e.preventDefault();
  var f=document.createElement('iframe');
  f.src='https://www.youtube-nocookie.com/embed/'+t.getAttribute('data-yt')+'?autoplay=1&rel=0';
  f.allow='autoplay; encrypted-media; fullscreen; picture-in-picture';
  f.allowFullscreen=true; f.title='video';
  t.innerHTML=''; t.removeAttribute('data-yt'); t.appendChild(f);
});
"""

HEAD = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Bowlby+One&family=Inter:wght@400;700&family=Permanent+Marker&display=swap" rel="stylesheet">')


def e(s):
    return html.escape(str(s), quote=True)


def page(lang, rel, title, body, accent="#ffc21a", up=0):
    """rel = path of page relative to lang root, e.g. 'art/'. up = depth below dist root."""
    root = "../" * up
    other = "en" if lang == "hu" else "hu"
    # the language switcher goes to the same page in the other language
    sw = f'{root}{other}/{rel}'
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="Shane 54: art, plugins, music, animation.">
<meta property="og:title" content="{e(title)}"><meta property="og:image" content="{root}assets/img/dj.jpg">
<link rel="icon" href="{root}assets/img/favicon.png">
{HEAD}
<link rel="stylesheet" href="{root}assets/style.css">
</head><body style="--ac:{accent}">
{body.replace('@ROOT@', root).replace('@LANG@', lang).replace('@SW@', sw)}
<script src="{root}assets/site.js"></script>
</body></html>"""


def top(lang, active, subs, up):
    """Sticky header with the 4-section strip and the sub-menu."""
    root = "../" * up
    tiles = ""
    for s in SECTIONS:
        img, pos = TILE[s]
        on = ' class="on"' if s == active else ""
        st = f' style="--ac:{ACCENT[s]}"'
        tiles += (f'<a href="@ROOT@@LANG@/{s}/"{on}{st}><img src="@ROOT@assets/img/{img}" alt="" style="object-position:{pos}">'
                  f'<span>{T[s][lang]}</span></a>')
    subhtml = ""
    for i, (label, href) in enumerate(subs):
        subhtml += f'<a href="{href}"{" class=on" if i == 0 else ""}>{label}</a>'
    return f"""<div class="top"><header>
<a class="logo" href="@ROOT@@LANG@/"><b>SHANE</b><i>54</i></a><a class="lang" href="@SW@">{'EN' if lang == 'hu' else 'HU'}</a></header>
<nav class="strip">{tiles}</nav>
<nav class="sub">{subhtml}</nav></div>"""


def foot():
    return ('<footer><span>© Shane 54</span>'
            f'<span><a href="https://open.spotify.com/artist/{SPOTIFY}">Spotify</a> · <a href="{DISCOGS}">Discogs</a></span></footer>')


def build_hub(lang):
    panels = ""
    for n, s in enumerate(SECTIONS, 1):
        img, pos = TILE[s]
        posd = {"art": "50% 55%", "plugins": "50% 20%", "music": "50% 70%", "animation": "50% 50%"}[s]
        panels += (f'<a class="panel" href="{s}/"><img src="../assets/img/{img}" alt="" style="object-position:{posd}">'
                   f'<div class="sh"></div><div class="tx"><div><small>0{n}</small><h2>{T[s][lang]}</h2><p>{e(T["sub_" + s][lang])}</p></div>'
                   f'<span class="go" style="background:{ACCENT[s]}">→</span></div></a>')
    body = (f'<div class="hub"><header><a class="logo" href="./"><b>SHANE</b><i>54</i></a>'
            f'<a class="lang" href="@SW@">{"EN" if lang == "hu" else "HU"}</a></header>{panels}</div>')
    return page(lang, "", "Shane 54", body, up=1)


def build_art(lang):
    subs = [(T["bio"][lang], "#bio"), (T["gallery"][lang], "#gallery")]
    gal = "".join(f'<a href="@ROOT@assets/img/{p}.jpg"><img loading="lazy" src="@ROOT@assets/img/{p}.jpg" alt="{e(alt)}"></a>' for p, alt in PAINTINGS)
    body = (top(lang, "art", subs, 2) +
            f'<section id="bio" class="pad"><h1 class="t">ART</h1><p class="bio">{e(CONTENT["art_bio"][lang])}</p></section>'
            f'<section id="gallery"><div class="gal">{gal}</div><div class="sig">–SHANE 54–</div></section>' + foot())
    return page(lang, "art/", "Art — Shane 54", body, ACCENT["art"], up=2)


def build_plugins(lang):
    subs = [(T["bio"][lang], "#bio"), (T["delay"][lang], "#delay")]
    body = (top(lang, "plugins", subs, 2) +
            f'<section id="bio" class="pad"><h1 class="t">PLUGINS</h1><p class="bio">{e(CONTENT["plugins_bio"][lang])}</p></section>'
            '<section id="delay" style="padding-top:16px"><div class="plug"><div class="st"><i style="flex:3;background:#ff8a3d"></i><i style="flex:2;background:#e4572e"></i><i style="flex:1;background:#2e86e4"></i></div>'
            '<div class="head"><img src="@ROOT@assets/img/spacecat_only.png" alt="Space Cat" style="width:86%">'
            '<img src="@ROOT@assets/img/delay_logo.png" alt="Delay" style="width:86%;margin-top:14px"></div>'
            f'<div class="head" style="padding-top:0;color:#b8c0d4;font-size:14px">{CONTENT["delay_tag"][lang]}</div>'
            '<img class="shot" src="@ROOT@assets/img/delay_ui.jpg" alt="Space Cat Delay">'
            f'<div class="actions"><span class="btn" style="background:#fff;color:#111;opacity:.55">{CONTENT["delay_btn"][lang]}</span>'
            f'<div style="text-align:center;font-size:13px;color:#b8c0d4">{CONTENT["delay_fmt"][lang]}</div></div></div></section>'
            f'<section class="pad" style="padding-top:28px"><div style="font-weight:700;font-size:20px;letter-spacing:.06em;padding-bottom:12px">{CONTENT["more_plugins"][lang]}</div>'
            f'<div class="rowc"><div class="sw" style="background:#7a3fe4"></div><div><b style="font-size:17px">BERLIN SCHOOL</b><div style="font-size:13px;color:#b8c0d4">{CONTENT["coming"][lang]} · VST3 · AU</div></div></div>'
            f'<div class="rowc"><div class="sw" style="background:#2e86e4"></div><div><b style="font-size:17px">SPACE CAT REVERB</b><div style="font-size:13px;color:#b8c0d4">{CONTENT["coming"][lang]} · VST3 · AU</div></div></div></section>'
            + foot())
    return page(lang, "plugins/", "Plugins — Shane 54", body, ACCENT["plugins"], up=2)


def build_music(lang):
    subs = [(T["bio"][lang], "#bio"), (T["disco"][lang], "#disco"), (T["id"][lang], "#id")]
    rows = ""
    for head, link, items in DISCO:
        rows += f'<div style="font-size:12px;font-weight:700;letter-spacing:.14em;color:#bbb;padding:28px 0 8px">{head}</div>'
        for y, t, c, l, k in items:
            sub = " · ".join(x for x in (c, l) if x)
            rows += f'<div class="r"><span class="y">{y}</span><span class="n"><b>{e(t)}</b><s>{e(sub)}</s></span><span class="tag">{k}</span></div>'
        rows += f'<a class="btn" style="border:2px solid #5ad1ff;margin-top:12px" href="{link}">Discogs →</a>'
    body = (top(lang, "music", subs, 2) +
            '<section id="disco" class="pad sp" style="padding-top:20px">'
            f'<iframe src="https://open.spotify.com/embed/artist/{SPOTIFY}" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy" title="Spotify"></iframe></section>'
            f'<section id="bio" class="pad" style="padding-top:24px"><h1 class="t">MUSIC</h1><p class="bio">{e(CONTENT["music_bio"][lang])}</p></section>'
            f'<div class="disc">{rows}</div>'
            f'<section id="id" class="pad"><a class="idc" href="id/"><b>INTERNATIONAL<br>DEPARTURES</b><span style="font-size:22px">→</span></a></section>'
            + foot())
    return page(lang, "music/", "Music — Shane 54", body, ACCENT["music"], up=2)


def build_id(lang):
    subs = [(T["bio"][lang], "../#bio"), (T["disco"][lang], "../#disco"), (T["id"][lang], "#")]
    subs_html = top(lang, "music", subs, 3)
    subs_html = subs_html.replace('<a href="#">ID</a>', '<a href="#" class="on">ID</a>').replace('<a href="../#bio" class=on>', '<a href="../#bio">')
    body = (subs_html +
            f'<section class="pad"><a href="../" style="display:flex;align-items:center;min-height:44px;font-size:14px;font-weight:700;color:#5ad1ff">{T["back"][lang]}</a>'
            f'<h1 class="t" style="font-size:38px;margin-top:8px">INTERNATIONAL DEPARTURES</h1><p class="bio">{e(CONTENT["id_bio"][lang])}</p>'
            f'<p class="bio" style="margin-top:24px;color:#bbb">{e(CONTENT["id_soon"][lang])}</p></section>' + foot())
    return page(lang, "music/id/", "International Departures — Shane 54", body, ACCENT["music"], up=3)


def build_animation(lang):
    subs = [(T["bio"][lang], "#bio"), (T["videos"][lang], "#videos")]
    vids = ""
    for vid, title, artist in VIDEOS:
        vids += (f'<div class="vid"><div class="th" data-yt="{vid}"><img loading="lazy" src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="">'
                 f'<button class="pl" aria-label="Play"></button></div>'
                 f'<div class="m"><b>{e(title)}</b><span>{e(artist)} · <a href="https://youtu.be/{vid}" style="text-decoration:underline">YouTube</a></span></div></div>')
    body = (top(lang, "animation", subs, 2) +
            f'<section id="bio" class="pad"><h1 class="t">ANIMATION</h1><p class="bio">{e(CONTENT["anim_bio"][lang])}</p></section>'
            f'<section id="videos" style="padding-top:24px">{vids}</section>' + foot())
    return page(lang, "animation/", "Animation — Shane 54", body, ACCENT["animation"], up=2)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets" / "img").mkdir(parents=True)
    for f in (SRC / "img").iterdir():
        shutil.copy(f, OUT / "assets" / "img" / f.name)
    try:
        from PIL import Image
        Image.open(SRC / "img" / "p01.jpg").resize((64, 64)).save(OUT / "assets" / "img" / "favicon.png")
    except Exception:
        pass
    (OUT / "assets" / "style.css").write_text(CSS, "utf-8")
    (OUT / "assets" / "site.js").write_text(JS, "utf-8")
    (OUT / ".nojekyll").write_text("")
    (OUT / "index.html").write_text(
        '<!doctype html><meta charset="utf-8"><title>Shane 54</title><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<script>location.replace((navigator.language||"hu").slice(0,2)=="hu"?"hu/":"en/")</script>'
        '<noscript><meta http-equiv="refresh" content="0;url=hu/"></noscript><a href="hu/">Shane 54</a>', "utf-8")
    for lang in LANGS:
        for rel, fn in (("", build_hub), ("art", build_art), ("plugins", build_plugins), ("music", build_music),
                        ("music/id", build_id), ("animation", build_animation)):
            d = OUT / lang / rel
            d.mkdir(parents=True, exist_ok=True)
            (d / "index.html").write_text(fn(lang), "utf-8")
    print("built ->", OUT)


if __name__ == "__main__":
    main()
