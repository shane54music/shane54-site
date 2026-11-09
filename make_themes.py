"""Generates the style-preview themes (site_src/themes/*.css). Each theme is a pure CSS override on top of assets/style.css."""
from pathlib import Path
OUT = Path(__file__).parent / "site_src" / "themes"

def font(fam): return "https://fonts.googleapis.com/css2?family=" + fam + "&display=swap"

BASE = """@import url('%(imp)s');
:root{--bg:%(bg)s;--fg:%(fg)s;--mut:%(mut)s;--line:%(line)s;--card:%(card)s;--hl:%(hl)s}
body{font-family:%(body)s;background:var(--bg);color:var(--fg);%(bodyx)s}
.top,.sub{background:%(top)s}
.top{%(topx)s}
.logo b,.logo i,.panel h2,h1.t,.club h2,.disc .dt,.idc b{font-family:%(disp)s;%(dispx)s}
.logo i{background:%(logoi)s;color:%(logoic)s;border-radius:%(r8)s;transform:%(logorot)s}
.lang{color:var(--fg)}
.bio{color:%(bio)s;%(biox)s}
h1.t{color:%(h1c)s;-webkit-text-stroke:%(stroke)s;%(h1x)s}
.panel h2{-webkit-text-stroke:%(pstroke)s;color:%(pc)s;%(h2x)s}
.panel .sh{background:%(panelsh)s}
.panel{margin-bottom:%(pgap)s;%(panelx)s}
.panel .go{border-radius:%(go)s}
.strip a{border-radius:%(r8)s;background:var(--card)}
.strip span{font-family:%(body)s}
.sub a{border-color:var(--line);color:var(--fg);border-radius:%(pill)s;%(subx)s}
.sub a.on{background:var(--ac);color:%(onc)s;border-color:var(--ac)}
.exh .r,.dg,.disc .r,.sh-tr,.sh-list,.eplist,.ep{border-color:var(--line)}
.exh .d,.disc .y,.sh-tr i{color:var(--hl)}
.disc .dt,.disc .dh,.dg summary em,.dg summary::after,.tag,.idc b{color:var(--hl)}
.disc .dh,.disc .n s,.ep .t s,.ep .d,.dk-t s,.sh-sub,.pl-times,.vid .m span,.sig{color:var(--mut)}
.dg summary em,.tag,.idc{border-color:var(--hl)}
.idc{border-radius:%(r14)s;%(idcx)s}
.dg summary,.sub a,.clubbtn,.club button{letter-spacing:%(ls)s}
.plug{border-color:var(--line);background:var(--card);border-radius:%(r20)s;%(plugx)s}
.rowc{border-color:var(--line);border-radius:%(r16)s;background:%(rowbg)s}
.btn{border-radius:%(pill)s}
.sp iframe,.vid .th,.gal img{border-radius:%(r14)s}
#dock,#sheet{background:%(dockbg)s;color:var(--fg)}
#dock{border-top-color:var(--hl)}
.dk-info,.ep,.sh-tr button{color:var(--fg)}
.dk-prog{background:var(--line)}.dk-prog i{background:var(--hl)}
.ib{color:var(--fg)}.ib.main,.dk-play{background:var(--hl);color:%(onhl)s}
.sh-head small,.sh-tr summary,.sh-spd{color:var(--hl);border-color:var(--hl)}
.ep.on{background:%(epon)s;box-shadow:inset 3px 0 0 var(--hl)}.ep.pl .t b{color:var(--hl)}
.vid .pl{background:%(playbg)s}
.clubbtn{background:%(clubbg)s;color:%(clubfg)s;border-color:%(clubbg)s}
.club{background:%(clubbg)s;color:%(clubfg)s;%(clubx)s}
.club input[type=email]{border-color:%(clubfg)s;border-radius:%(r8)s}
.club button{background:%(clubfg)s;color:%(clubbg)s;border-color:%(clubfg)s;border-radius:%(r8)s}
.cs-x{color:%(clubfg)s}
footer{color:var(--mut)}
%(extra)s
"""

D = dict(imp="", bg="#111", fg="#fff", mut="#bbb", line="#2a2a2a", card="#171717", hl="#5ad1ff",
 body="'Inter',Arial,sans-serif", bodyx="", top="#111", topx="", disp="'Bowlby One',sans-serif", dispx="",
 logoi="#ffc21a", logoic="#111", r8="8px", logorot="rotate(-4deg)", bio="#e6e6e6", biox="",
 h1c="var(--ac)", stroke="3px #000", h1x="", pstroke="3px #111", pc="#fff", h2x="", panelsh="linear-gradient(to top,rgba(0,0,0,.65),rgba(0,0,0,0) 58%)",
 pgap="4px", panelx="", go="50%", subx="", onc="#111", r14="14px", r16="16px", r20="20px", idcx="", ls=".08em", plugx="",
 rowbg="transparent", pill="999px", dockbg="#0b0b0b", onhl="#111", epon="#10222a", playbg="#111",
 clubbg="#ffc21a", clubfg="#111", clubx="", extra="")

T = {}

# ---------- SUPERSLICK 1: Obsidian (dark glass, neon gradient) ----------
T["slick-obsidian"] = dict(imp=font("Manrope:wght@300;400;600;800"), bg="#07080c", card="#0e1118", line="rgba(255,255,255,.09)", hl="#7cf3ff", mut="#8b93a7",
 body="'Manrope',sans-serif", disp="'Manrope',sans-serif", dispx="font-weight:800;letter-spacing:-.03em", top="rgba(7,8,12,.72)", topx="backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);border-bottom:1px solid rgba(255,255,255,.07)",
 logoi="linear-gradient(135deg,#7cf3ff,#a78bfa)", logoic="#07080c", logorot="none", r8="10px", stroke="0 transparent", pstroke="0 transparent",
 h1x="font-weight:800;letter-spacing:-.04em;font-size:54px;background:linear-gradient(120deg,var(--ac),#fff 70%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent",
 h2x="font-weight:800;letter-spacing:-.04em", panelsh="linear-gradient(to top,rgba(7,8,12,.92),rgba(7,8,12,0) 70%)", pgap="6px", panelx="border-radius:22px;margin:0 8px 8px;box-shadow:0 0 0 1px rgba(255,255,255,.08),0 20px 50px -20px #000",
 r14="22px", r20="26px", dockbg="rgba(14,17,24,.8)", onhl="#07080c", epon="rgba(124,243,255,.08)", playbg="rgba(255,255,255,.14)", clubbg="linear-gradient(135deg,#7cf3ff,#a78bfa)", clubfg="#07080c", ls=".02em",
 plugx="box-shadow:0 30px 80px -30px rgba(124,243,255,.25)", bio="#c7ccda",
 extra=".hub header{background:transparent}.panel .go{background:rgba(255,255,255,.92)!important;backdrop-filter:blur(10px)}#dock{backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}.sub a.on{box-shadow:0 0 24px -4px var(--ac)}.panel small{color:#7cf3ff;letter-spacing:.3em}")

# ---------- SUPERSLICK 2: Chrome (light, glossy, soft) ----------
T["slick-chrome"] = dict(imp=font("Space+Grotesk:wght@400;500;700"), bg="#eef0f4", fg="#10131a", mut="#5d6575", card="#ffffff", line="#d9dde6", hl="#3b5bff",
 body="'Space Grotesk',sans-serif", disp="'Space Grotesk',sans-serif", dispx="font-weight:700;letter-spacing:-.04em", top="rgba(238,240,244,.82)", topx="backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px)",
 logoi="#10131a", logoic="#fff", logorot="none", r8="12px", bio="#2b3140", stroke="0 transparent", pstroke="0 transparent", h1c="#10131a",
 h1x="letter-spacing:-.05em;font-size:56px", h2x="letter-spacing:-.04em;text-shadow:0 2px 24px rgba(0,0,0,.4)", panelsh="linear-gradient(to top,rgba(10,14,30,.7),rgba(10,14,30,0) 60%)",
 pgap="10px", panelx="border-radius:26px;margin:0 10px 10px;box-shadow:0 18px 40px -18px rgba(20,30,60,.45)", go="16px", r14="22px", r16="20px", r20="28px", dockbg="rgba(255,255,255,.92)", onhl="#fff", epon="#e6ebff", playbg="rgba(255,255,255,.9)",
 clubbg="#10131a", clubfg="#fff", ls=".01em", rowbg="#fff", plugx="box-shadow:0 24px 60px -28px rgba(20,30,60,.5)",
 extra=".logo i{box-shadow:0 6px 16px -6px rgba(0,0,0,.5)}.vid .pl:after{border-left-color:#10131a}.sub a{background:#fff;border-color:#e1e5ee}.sub a.on{box-shadow:0 8px 20px -8px var(--ac)}.strip a{box-shadow:0 8px 20px -10px rgba(0,0,0,.4)}.club h2{letter-spacing:-.05em}.panel .go{background:#fff!important;box-shadow:0 8px 20px -6px rgba(0,0,0,.4)}.dg summary em{background:#e6ebff}.ep.on{background:#e6ebff}")

# ---------- CONSERVATIVE 1: Ledger (navy, cream, serif) ----------
T["conservative-ledger"] = dict(imp=font("Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Source+Sans+3:wght@400;600"), bg="#0f1b2d", fg="#f4efe3", mut="#aab4c4", card="#14243a", line="#2c3d57", hl="#d9b66b",
 body="'Source Sans 3',sans-serif", disp="'Libre Baskerville',serif", dispx="font-weight:700;letter-spacing:0", top="#0f1b2d", logoi="#d9b66b", logoic="#0f1b2d", logorot="none", r8="2px", bio="#e4e0d4", biox="font-family:'Libre Baskerville',serif;font-size:16px;line-height:1.7",
 stroke="0 transparent", pstroke="0 transparent", h1c="#f4efe3", h1x="font-size:40px;border-bottom:1px solid #d9b66b;padding-bottom:12px", h2x="font-size:clamp(28px,7.5vw,40px)", panelsh="linear-gradient(to top,rgba(15,27,45,.9),rgba(15,27,45,.1) 65%)",
 pgap="2px", go="2px", r14="2px", r16="2px", r20="2px", pill="2px", dockbg="#0b1422", onhl="#0f1b2d", epon="#1a2d49", playbg="#0f1b2d", clubbg="#f4efe3", clubfg="#0f1b2d", ls=".12em", onc="#0f1b2d",
 extra=".sub a{text-transform:uppercase;font-size:11px}.logo b,.logo i{font-size:21px}.panel small{color:#d9b66b}.panel .go{background:#d9b66b!important}.plug{border-width:1px}.club h2{font-size:clamp(28px,8vw,44px)}.disc .dt{font-size:20px}.club{border-top:4px double #0f1b2d}")

# ---------- CONSERVATIVE 2: Gallery (white paper, black, classic) ----------
T["conservative-gallery"] = dict(imp=font("Cormorant+Garamond:ital,wght@0,500;0,700;1,500&family=Lato:wght@400;700"), bg="#faf8f4", fg="#1b1b1b", mut="#6b665d", card="#f1ede5", line="#d8d2c6", hl="#7a1f2b",
 body="'Lato',sans-serif", disp="'Cormorant Garamond',serif", dispx="font-weight:700;letter-spacing:.01em", top="#faf8f4", logoi="#1b1b1b", logoic="#faf8f4", logorot="none", r8="0", bio="#2a2a2a", biox="font-family:'Cormorant Garamond',serif;font-size:21px;line-height:1.5",
 stroke="0 transparent", pstroke="0 transparent", h1c="#1b1b1b", h1x="font-size:54px;font-style:italic", h2x="font-size:clamp(38px,10vw,56px);text-shadow:0 1px 14px rgba(0,0,0,.5)", pgap="0", go="0", r14="0", r16="0", r20="0", pill="0", dockbg="#f1ede5", onhl="#faf8f4", epon="#ece6d9", playbg="rgba(255,255,255,.9)",
 clubbg="#1b1b1b", clubfg="#faf8f4", ls=".14em", onc="#faf8f4", panelsh="linear-gradient(to top,rgba(0,0,0,.6),rgba(0,0,0,0) 55%)", rowbg="#fff",
 extra=".sub a{text-transform:uppercase;font-size:11px;border-width:1px}.sub a.on{background:#1b1b1b;border-color:#1b1b1b}.vid .pl:after{border-left-color:#1b1b1b}.logo b{font-size:26px}.logo i{font-size:24px;font-style:normal}.plug{border-width:1px}.gal{gap:0}.gal img{box-shadow:0 0 0 8px #fff,0 0 0 9px #d8d2c6;margin:10px 0}.gal a{margin-bottom:14px}.panel .go{background:#fff!important}.club input[type=email]{background:#faf8f4}")

# ---------- FLASHY 1: Neon Rave ----------
T["flashy-neon"] = dict(imp=font("Bowlby+One&family=Rubik:wght@500;800"), bg="#05010d", fg="#fff", mut="#d9b8ff", card="#12052a", line="#ff2bd6", hl="#00f0ff", body="'Rubik',sans-serif",
 top="#05010d", topx="border-bottom:2px solid #ff2bd6;box-shadow:0 4px 30px -6px #ff2bd6", logoi="#ff2bd6", logoic="#fff", logorot="rotate(-6deg)", stroke="0 transparent", pstroke="0 transparent", h1c="var(--ac)",
 h1x="font-size:54px;text-shadow:0 0 6px var(--ac),0 0 24px var(--ac),0 0 50px #ff2bd6;text-transform:uppercase", h2x="text-transform:uppercase;text-shadow:0 0 10px #ff2bd6,0 0 30px #ff2bd6", panelsh="linear-gradient(to top,rgba(5,1,13,.85),rgba(80,0,120,.15) 70%)",
 pgap="6px", panelx="border:2px solid #00f0ff;box-shadow:0 0 18px #00f0ff55,inset 0 0 18px #00f0ff33", go="50%", dockbg="#05010d", onhl="#05010d", epon="#2a0a55", playbg="#ff2bd6", clubbg="#ffee00", clubfg="#05010d", ls=".1em", rowbg="#12052a", r14="6px",
 extra=".sub a{border-color:#ff2bd6;text-transform:uppercase;font-weight:800;box-shadow:0 0 12px #ff2bd655}.sub a.on{box-shadow:0 0 22px var(--ac)}.panel .go{background:#00f0ff!important;box-shadow:0 0 20px #00f0ff}.panel small{color:#00f0ff;text-shadow:0 0 8px #00f0ff}.disc .dt{text-shadow:0 0 14px #00f0ff}.club{transform:skewY(-2deg);margin:40px 0;padding-top:40px;padding-bottom:40px}.club>*{transform:skewY(2deg)}.strip a.on{box-shadow:0 0 16px var(--ac)}.plug{border-color:#ff2bd6;box-shadow:0 0 30px #ff2bd666}.logo b{text-shadow:0 0 12px #ff2bd6}")

# ---------- FLASHY 2: Pop Sticker ----------
T["flashy-pop"] = dict(imp=font("Bowlby+One&family=Fredoka:wght@500;700"), bg="#ffe14a", fg="#111", mut="#3a2f00", card="#fff", line="#111", hl="#ff3d81", body="'Fredoka',sans-serif",
 top="#ffe14a", topx="border-bottom:4px solid #111", logoi="#ff3d81", logoic="#fff", logorot="rotate(-5deg)", bio="#111", biox="font-weight:500;font-size:18px", stroke="3px #111", pstroke="4px #111", h1c="#fff",
 h1x="font-size:52px;text-shadow:5px 5px 0 #111", h2x="text-shadow:4px 4px 0 #111;transform:rotate(-2deg);transform-origin:left", panelsh="linear-gradient(to top,rgba(0,0,0,.45),rgba(0,0,0,0) 55%)", pgap="8px",
 panelx="border:4px solid #111;border-radius:22px;margin:0 8px 8px;box-shadow:6px 6px 0 #111", go="50%", r8="12px", r14="18px", r16="18px", r20="26px", dockbg="#fff", onhl="#fff", epon="#fff3b0", playbg="#ff3d81", clubbg="#27d3ff", clubfg="#111", ls=".04em", rowbg="#fff",
 extra=".sub a{background:#fff;border:3px solid #111;color:#111;box-shadow:3px 3px 0 #111}.sub a.on{box-shadow:3px 3px 0 #111;color:#111}.strip a{border:3px solid #111;border-radius:12px}.strip a.on{border-color:var(--ac);box-shadow:3px 3px 0 #111}.panel .go{background:#fff!important;border:3px solid #111;box-shadow:3px 3px 0 #111}.plug,.rowc,.idc{border:4px solid #111;box-shadow:6px 6px 0 #111;background:#fff}.dg summary em,.tag{background:#fff;border:2px solid #111;color:#111}.disc .y,.disc .dt,.disc .dh,.exh .d,.idc b{color:#111}.btn{border:3px solid #111;box-shadow:4px 4px 0 #111}.vid .th{border:4px solid #111;box-shadow:6px 6px 0 #111}.club{border-top:4px solid #111;border-bottom:4px solid #111}.club button{box-shadow:4px 4px 0 #111}.disc .dt{text-shadow:none}.logo b{font-size:24px}.sub a.on{background:#ff3d81;color:#fff}.dk-t s,.dg summary::after{color:#111}.sp iframe{border:4px solid #111;box-shadow:6px 6px 0 #111}.ep.on{background:#fff3b0}.exh .r,.dg,.disc .r{border-top-width:2px}")

# ---------- POMPOUS 1: Gold Baroque ----------
T["pompous-gold"] = dict(imp=font("Cinzel:wght@500;700;900&family=Playfair+Display:ital,wght@0,400;1,400&family=Cormorant+Garamond:wght@500"), bg="#0a0806", fg="#f3e6c4", mut="#b9a579", card="#16110a", line="#7a5f23", hl="#e8c15a",
 body="'Cormorant Garamond',serif", bodyx="font-size:18px", disp="'Cinzel',serif", dispx="font-weight:900;letter-spacing:.06em", top="#0a0806", topx="border-bottom:1px solid #e8c15a;box-shadow:0 1px 0 #0a0806,0 3px 0 #7a5f23",
 logoi="linear-gradient(180deg,#f6dc8f,#b88a2c)", logoic="#0a0806", logorot="none", r8="2px", bio="#eadcb5", biox="font-family:'Playfair Display',serif;font-size:17px;line-height:1.75;text-align:justify",
 stroke="0 transparent", pstroke="0 transparent", h1c="#e8c15a", h1x="font-size:38px;text-align:center;letter-spacing:.14em;text-transform:uppercase;text-shadow:0 2px 0 #000;border-top:1px solid #7a5f23;border-bottom:1px solid #7a5f23;padding:14px 0",
 h2x="font-size:clamp(26px,7vw,38px);letter-spacing:.14em;text-transform:uppercase;color:#f6dc8f;text-shadow:0 2px 12px #000", panelsh="linear-gradient(to top,rgba(10,8,6,.92),rgba(10,8,6,.1) 70%)", pgap="6px",
 panelx="border:1px solid #e8c15a;outline:1px solid #7a5f23;outline-offset:3px;margin:0 8px 8px", go="2px", r14="2px", r16="2px", r20="2px", pill="2px", dockbg="#0a0806", onhl="#0a0806", epon="#241a0a", playbg="#0a0806", clubbg="#e8c15a", clubfg="#0a0806", ls=".18em", onc="#0a0806",
 extra=".sub a{text-transform:uppercase;font-family:'Cinzel',serif;font-size:11px}.panel .go{background:linear-gradient(180deg,#f6dc8f,#b88a2c)!important;color:#0a0806}.panel small{color:#e8c15a;font-family:'Cinzel',serif;letter-spacing:.3em}.plug,.rowc,.idc{border:1px solid #e8c15a;outline:1px solid #7a5f23;outline-offset:3px}.club{border-top:6px double #0a0806;border-bottom:6px double #0a0806}.club h2{font-size:clamp(26px,8vw,40px);letter-spacing:.1em}.disc .dt{letter-spacing:.14em;font-size:20px}.sig{font-family:'Playfair Display',serif;font-style:italic}.logo b{font-size:20px;letter-spacing:.1em}.logo i{font-size:19px}.btn{border:1px solid #e8c15a}.gal img{border:1px solid #e8c15a;padding:4px;background:#16110a}.strip a.on{border-color:#e8c15a}")

# ---------- POMPOUS 2: Royal (burgundy, gold, italic serif) ----------
T["pompous-royal"] = dict(imp=font("Playfair+Display:ital,wght@0,700;0,900;1,500;1,700&family=Lora:wght@400;600"), bg="#2a0a1a", fg="#fbeed6", mut="#d3a9a0", card="#3a1226", line="#8a5a2b", hl="#f0c36b",
 body="'Lora',serif", disp="'Playfair Display',serif", dispx="font-weight:900;font-style:italic", top="#2a0a1a", topx="border-bottom:3px double #f0c36b", logoi="#f0c36b", logoic="#2a0a1a", logorot="rotate(-3deg)", r8="6px", bio="#f3e0c4", biox="line-height:1.75;font-size:17px",
 stroke="0 transparent", pstroke="0 transparent", h1c="#f0c36b", h1x="font-size:52px;text-shadow:3px 3px 0 #000", h2x="font-size:clamp(34px,9vw,50px);text-shadow:2px 3px 0 #000", panelsh="linear-gradient(to top,rgba(42,10,26,.92),rgba(42,10,26,.05) 65%)", pgap="8px",
 panelx="border:3px double #f0c36b;margin:0 8px 8px;border-radius:4px", go="50%", r14="8px", r16="8px", r20="14px", pill="999px", dockbg="#1d0711", onhl="#2a0a1a", epon="#4a1a34", playbg="#2a0a1a", clubbg="#f0c36b", clubfg="#2a0a1a", ls=".06em", onc="#2a0a1a",
 extra=".sub a{font-family:'Playfair Display',serif;font-style:italic;font-size:14px;letter-spacing:.02em}.panel .go{background:#f0c36b!important}.panel small{font-style:italic;letter-spacing:.2em}.plug,.rowc,.idc{border:3px double #f0c36b}.club{border-top:6px double #2a0a1a;border-bottom:6px double #2a0a1a}.club h2{font-style:italic}.disc .dt{font-style:italic;font-size:26px}.sig{font-family:'Playfair Display',serif;font-style:italic}.strip a{border-radius:4px}")

# ---------- HUMBLE 1: Paper ----------
T["humble-paper"] = dict(imp=font("Inter:wght@400;600"), bg="#ffffff", fg="#1a1a1a", mut="#737373", card="#f5f5f5", line="#e4e4e4", hl="#1a1a1a",
 disp="'Inter',sans-serif", dispx="font-weight:600;letter-spacing:-.01em", top="#fff", logoi="transparent", logoic="#1a1a1a", logorot="none", r8="0", bio="#333", biox="line-height:1.65",
 stroke="0 transparent", pstroke="0 transparent", h1c="#1a1a1a", h1x="font-size:28px;margin-bottom:12px", h2x="font-size:clamp(24px,6vw,30px);text-shadow:0 1px 10px rgba(0,0,0,.5)", panelsh="linear-gradient(to top,rgba(0,0,0,.55),rgba(0,0,0,0) 50%)",
 pgap="2px", go="0", r14="0", r16="0", r20="0", pill="0", dockbg="#fff", onhl="#fff", epon="#f2f2f2", playbg="rgba(255,255,255,.9)", clubbg="#f5f5f5", clubfg="#1a1a1a", ls="0", onc="#fff", rowbg="#fff",
 extra=".logo b{font-size:18px}.logo i{font-size:18px;padding:0;font-family:'Inter';font-weight:600}.sub a{border:0;border-bottom:2px solid transparent;font-weight:600;font-size:13px;justify-content:flex-start;letter-spacing:0}.sub a.on{background:none;color:#1a1a1a;border-bottom-color:#1a1a1a}.strip{gap:2px}.strip span{font-weight:600}.panel .go{background:#fff!important;width:36px;height:36px;font-size:18px}.panel small{font-weight:400;letter-spacing:.06em}.plug{border:1px solid #e4e4e4;background:#fff}.rowc{border-width:1px}.idc{border-width:1px}.club{border-top:1px solid #e4e4e4}.club h2{font-size:26px;letter-spacing:-.01em}.club input[type=email]{border:1px solid #ccc;background:#fff}.club button{background:#1a1a1a;color:#fff}.disc .dt{font-size:18px}.vid .pl:after{border-left-color:#1a1a1a}.dg summary em,.tag{border:0;background:#f0f0f0;color:#555}.btn{border:1px solid #1a1a1a}")

# ---------- HUMBLE 2: Mono ----------
T["humble-mono"] = dict(imp=font("IBM+Plex+Mono:wght@400;500;600"), bg="#e9e9e6", fg="#1c1c1c", mut="#6b6b66", card="#f2f2ef", line="#c9c9c3", hl="#c2410c",
 body="'IBM Plex Mono',monospace", bodyx="font-size:15px", disp="'IBM Plex Mono',monospace", dispx="font-weight:600;letter-spacing:-.02em", top="#e9e9e6", logoi="transparent", logoic="#1c1c1c", logorot="none", r8="0", bio="#2a2a28", biox="font-size:15px;line-height:1.7",
 stroke="0 transparent", pstroke="0 transparent", h1c="#1c1c1c", h1x="font-size:26px;margin-bottom:10px", h2x="font-size:clamp(22px,6vw,28px);text-shadow:0 1px 8px rgba(0,0,0,.6)", panelsh="linear-gradient(to top,rgba(0,0,0,.6),rgba(0,0,0,0) 50%)",
 pgap="1px", go="0", r14="0", r16="0", r20="0", pill="0", dockbg="#f2f2ef", onhl="#fff", epon="#e0e0da", playbg="rgba(255,255,255,.9)", clubbg="#1c1c1c", clubfg="#e9e9e6", ls="0", onc="#fff", rowbg="#f2f2ef",
 extra=".logo b{font-size:17px}.logo i{font-size:17px;padding:0;font-family:'IBM Plex Mono';font-weight:600}.logo i:before{content:'/'}.sub a{border:1px solid #c9c9c3;font-weight:500;font-size:12px;text-transform:lowercase}.sub a.on{background:#1c1c1c;color:#e9e9e6;border-color:#1c1c1c}.strip a{border:1px solid #c9c9c3}.strip span{font-weight:500;text-transform:lowercase}.panel .go{background:#e9e9e6!important;width:34px;height:34px;font-size:16px}.panel small{font-weight:400;letter-spacing:0}.plug{border:1px solid #c9c9c3}.rowc,.idc{border-width:1px}.club h2{font-size:24px;letter-spacing:-.02em}.club input[type=email]{border:1px solid #1c1c1c;background:#e9e9e6;color:#1c1c1c}.club button{background:#e9e9e6;color:#1c1c1c}.disc .dt{font-size:16px;color:#1c1c1c}.vid .pl:after{border-left-color:#1c1c1c}.dg summary em,.tag{border:1px solid #c2410c}.btn{border:1px solid #1c1c1c}.exh .d,.disc .y{color:#c2410c}.gal img{border:1px solid #c9c9c3}")

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f in OUT.glob("*.css"): f.unlink()
    for name, v in T.items():
        d = {**D, **v}
        (OUT / f"{name}.css").write_text(BASE % d)
    print(len(T), "themes")
