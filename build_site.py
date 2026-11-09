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
SECTIONS = ["art", "software", "music", "animation"]
ACCENT = {"art": "#ff8fb1", "software": "#ffc21a", "music": "#5ad1ff", "animation": "#ff8a3d"}
TILE = {"art": ("p01.jpg", "50% 55%"), "software": ("delay_ui.jpg", "12% 50%"),
        "music": ("dj.jpg", "50% 75%"), "animation": ("p08.jpg", "50% 50%")}
SPOTIFY = "2ITbqEgyp32vL3BxEFmQ1V"
DISCOGS = "https://www.discogs.com/artist/18440-Shane-54"

T = {  # UI texts
    "art": {"hu": "ART", "en": "ART"}, "software": {"hu": "SOFTWARE", "en": "SOFTWARE"},
    "music": {"hu": "MUSIC", "en": "MUSIC"}, "animation": {"hu": "ANIMATION", "en": "ANIMATION"},
    "sub_art": {"hu": "110 festmény", "en": "110 paintings"},
    "sub_software": {"hu": "Space Cat Delay · Berlin School · Reverb", "en": "Space Cat Delay · Berlin School · Reverb"},
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
        "hu": [
            "Shane 54 igazi sokoldalú ember.",
            "A popénekesi múltja és a 90-es évek slágerei miatt, amiket a mai napig mindenhol játszanak, nyugodtan állíthatjuk, hogy ő Magyarország egyik legismertebb képzőművésze. (Oké, elsősorban a zenéjéről ismert, de azért az utcán a mai napig felismerik, ami a festők többségénél ritkább dolog.)",
            "A legelső képalkotó MI-rendszerek megjelenésével 2022-ben belecsöppent ebbe a technológiába és a végtelen lehetőségeibe. Amit technikában nélkülözött, azt a látásmódjával pótolta.",
            "Furcsa módon addig soha semmi köze nem volt a művészethez, különösebben nem is érdekelte. De az MI-képek készítése valahogy megnyitott benne valamit, ami messzebbre vitte, mint bárki – ő maga is – gondolta volna.",
            "2022 végén két macska „festmény”-renderje, amint egy szintipop zenekart alakítanak, egyik napról a másikra mindent megváltoztatott. Amikor kitette az Instagramra, berobbant: ez jelezte, hogy a macskaművészet olyan út, amit érdemes bejárni.",
            "Amikor „festményszerű tárgyait” – a nyomatokat átfestette, hogy egyediek legyenek – bemutatta a művészeti közösségnek egy hatalmas budapesti művészeti vásáron, gyorsan megváltozott a megítélés. Azok a macskák egyértelműen slágerek lettek, a következő lépés pedig az volt, hogy hagyományos módon is megfesse őket. Ecsetet és vásznat fogott, rengeteg festés-oktatóvideót nézett meg a YouTube-on (ma is nézi), és soha nem nézett vissza. A víziója megmutatta, merre tart: csak azt kellett kitalálnia, hogyan vigye vászonra az ötleteit. Elég sajátos munkamódszer, de valahogy működött. A közönség sokkal jobban szerette a kézzel festett műveit, mint az MI-„festményeket”, pedig azok is úgy fogytak, mint a cukor.",
            "Egy évvel később, 2025-ben megrendezte első önálló kiállítását Magyarország egyik legnagyobb galéria- és aukciósházában. A hely teljesen megtelt rajongókkal, akik láthatóan élvezték a Shane által teremtett színes macskavilágot.",
            "Azóta a híres macskafestmények mellett egy nagy magyar divatmárkával működött együtt, így a macskái az ország összes üzletébe eljutottak. Az elmúlt hónapokban Lóránt Ervin „Hervé” szobrászbarátjával dolgozik: több projekten is azon vannak, hogy a művészetét lehozzák a falról, és valódi terekbe vigyék."],
        "en": [
            "Shane 54 is truly a man of many trades.",
            "Because of his pop singer background, and 90s mega hit singles getting played everywhere to this very day we can safely say he is one of the most well known fine artists of Hungary. (Ok, he’s known mainly for his musical output, but hey, people still recognise him on the street which is a less common feat with most painters)",
            "With the arrival of the very early image creating AI systems, in 2022 he found himself immersed into this technology and its endless possibilities. What he was lacking in technique, he made up with a vision.",
            "Oddly enough, up to that point he never had anything to do with art, he wasn’t particularly interested in it. But somehow creating AI images opened up something, that took him way further than anyone - including himself - would have thought.",
            "Late 2022 a “painting” render of two cats posing as a synth pop band changed everything overnight. When he posted it on his instagram, it blew up, suggesting cat art is an avenue worth discovering.",
            "As his “painting looking objects” - he painted over the prints to make them unique - were introduced to the art community at a huge art fair in Budapest, perception changed up real fast. Those cats were clearly a hit, and the next step was to make them the traditional way. He grabbed brushes and canvases, watched TONS of painting tutorials on Youtube (he still does) and he never looked back. His vision made sure he knows where he’s headed: he only needed to know how to put the ideas on canvas, a rather peculiar way of working, but somehow it did work. The public loved his handmade art much more than his AI “paintings”, even though those were selling like hotcakes.",
            "A year later he had his first solo exhibition at one of the biggest gallery/auction houses in Hungary in 2025. The place was completely filled with fans who clearly enjoyed the world Shane created with his colorful cats.",
            "Since then besides those famous cat paintings, he collaborated with a large Hungarian fashion brand to bring his cats into their stores all over the country. The past few months spent collaborating with Ervin “Hervé” Lóránt, a sculptor friend: they are working on several projects to take his art off the wall and bring it into real spaces."]},
    "exh_title": {"hu": "KIÁLLÍTÁSOK", "en": "EXHIBITIONS"},
    "plugins_bio": {
        "hu": "Karakteres effektek és hangszerek, amiket elsősorban magamnak építek. A Space Cat Delay a Korg Monotron Delay önoszcilláló, zajos világából indult: nem tiszta delay, hanem hangulatgyár. A Berlin School és a Space Cat Reverb készülőben van.",
        "en": "Characterful effects and instruments, built first of all for myself. Space Cat Delay grew out of the self-oscillating, noisy world of the Korg Monotron Delay: not a clean delay but an atmosphere machine. Berlin School and Space Cat Reverb are on the way."},
    "music_bio": {
        "hu": [
            "1973-ban született Budapesten. Még gimnazista volt, amikor popzenekarának első albuma megjelent, így húsz éves kora előtt már ismert közszereplő lett. A fiúegyüttes, amelynek frontembere volt, félmillió lemezt adott el, és néhány korai dala beépült a magyar popkultúrába.",
            "A 90-es évek után elindult a DJ-karrierje, ami hihetetlen magasságokba repítette: ő az egyetlen magyar előadó, akinek RIAA aranylemeze van az Egyesült Államokban, és az egyetlen, aki valaha az első helyre került a Billboard Dance listán Magyarországról. A Myon & Shane 54 DJ/producer duó egyik feleként három éven át egymás után szerepelt a világ legjobb 100 DJ-je között a zeneipar bibliájának számító brit Mixmag listáján.",
            "Zenei producerként és remixerként dolgozott többek között Lana Del Reyjel, Jessie J-vel, Tiëstóval, Armin van Buurennel, az Above & Beyonddal és még sok más előadóval."],
        "en": [
            "Born in Budapest Hungary in 1973, he was still in high school when his pop band’s first album was released - he was a well known public figure before turning 20. The boyband he fronted sold half a million records, and some of those early songs cemented themselves into Hungarian pop culture.",
            "After the 90s, he began his dj career, which took him to unbelievable heights: he’s the only Hungarian artist with an RIAA certified Gold Record in the USA, also he’s the only one to ever topped the Billboard Dance Charts from his native country. For 3 years in a row as one half dj/producer duo Myon & Shane 54 he was named in the Top 100 international djs of the world, by music industry bible Mixmag UK.",
            "As a music producer / remixer he worked with the likes of Lana Del Rey, Jessie J, Tiesto, Armin Van Buuren, Above & Beyond and many many more."]},
    "anim_bio": {
        "hu": "Animátorként zenei videókat is készítek: ezek közül válogatás.",
        "en": "As an animator I also make music videos. A selection of them below."},
    "id_bio": {
        "hu": "Az International Departures a podcastom volt. Évekkel ezelőtt véget ért, az archívumot később újra elérhetővé teszem itt.",
        "en": "International Departures was my podcast. It ended years ago; I will make the archive available here again."},
    "id_soon": {"hu": "Az archívum hamarosan feltöltődik.", "en": "The archive is coming soon."},
    "more_plugins": {"hu": "TOVÁBBI SZOFTVEREK", "en": "MORE SOFTWARE"},
    "coming": {"hu": "Készülőben", "en": "In development"},
    "delay_tag": {"hu": "Atmospheric Echo Machine", "en": "Atmospheric Echo Machine"},
    "delay_btn": {"hu": "LETÖLTÉS: HAMAROSAN", "en": "DOWNLOAD: COMING SOON"},
    "delay_fmt": {"hu": "VST3 · AU · macOS", "en": "VST3 · AU · macOS"},
}

EXHIBITIONS = [("2023", {"hu": "március", "en": "March"}, "Art & Antique Fair, Budapest, Hungary"),
               ("2023", {"hu": "szeptember", "en": "September"}, "Jókai 7, Mindszentkalla, Hungary"),
               ("2023", {"hu": "november", "en": "November"}, "Fashion Street, Budapest"),
               ("2024", {"hu": "március", "en": "March"}, "Art & Antique Fair, Budapest, Hungary"),
               ("2024", {"hu": "június", "en": "June"}, "Fishing On Orfű, Orfű, Hungary"),
               ("2024", {"hu": "július", "en": "July"}, "Füred Art Week, Balatonfüred, Hungary"),
               ("2024", {"hu": "augusztus", "en": "August"}, "STRAND Festival, Zamárdi, Hungary"),
               ("2025", {"hu": "március", "en": "March"}, "Art & Antique Fair, Budapest, Hungary"),
               ("2025", {"hu": "június", "en": "June"}, "Solo Exhibition – Bodo Gallery, Budapest, Hungary"),
               ("2025", {"hu": "július", "en": "July"}, "Füred Art Week, Balatonfüred, Hungary"),
               ("2025", {"hu": "december", "en": "December"}, "Szentendre Art Week, Szentendre, Hungary"),
               ("2026", {"hu": "február", "en": "February"}, "Art & Antique Fair, Budapest, Hungary")]

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

MYON = [("2016", "Round We Go", "Myon & Shane 54 x Haley", "Ride Recordings", "SINGLE"),
        ("2016", "Round We Go (Remixes)", "Myon & Shane 54 x Haley", "Ride Recordings", "SINGLE"),
        ("2015", "Wicked Game", "", "Ride Recordings", "SINGLE"),
        ("2013", "Take Me Back (Myon & Shane 54 Edit)", "Fatum", "Ride Recordings", "REMIX"),
        ("2010", "Come Around Again (Myon & Shane 54 Monster Mix)", "Signum feat. Anita Kelsey", "", "REMIX"),
        ("2010", "Washout (Myon & Shane 54 Remix)", "Bissen & The Crossover", "", "REMIX"),
        ("2010", "The White Room (Myon & Shane 54 Refill)", "Andy Moor, Whiteroom, Adam White", "", "REMIX"),
        ("2010", "That Day (Myon & Shane 54 Club Mix)", "Dresden & Johnston feat. Nadia Ali & Mikael Johnston", "", "REMIX"),
        ("2011", "All Around You", "Cosmic Gate with Myon & Shane 54 and Aruna", "Black Hole Recordings", "SINGLE"),
        ("2014", "Summer Of Love (Remixes)", "Myon & Shane 54 + Kyler England", "Ride Recordings", "SINGLE"),
        ("2013", "Outshine (Remixes)", "Myon & Shane 54 with Natalie Peris", "Ride Recordings", "SINGLE"),
        ("2014", "Hurricane (Remixes)", "Myon & Shane 54 with Amy Pearson", "Ride Recordings", "SINGLE"),
        ("2014", "Under Your Cloud", "Myon & Shane 54 + Late Night Alumni", "Ride Recordings", "SINGLE"),
        ("2014", "If I Fall", "Cole Plante with Myon & Shane 54", "Hollywood Records", "SINGLE"),
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
        ("2008", "Vampire", "Myon & Shane 54 feat. Carrie Skipper", "Armind", "SINGLE"),
        ("2011", "Without Warning (Myon & Shane 54 Monster Mix)", "Exostate", "Enhanced Recordings", "REMIX"),
        ("2011", "Connection (Myon & Shane 54 Monsterless Mix)", "Susana", "Armada Digital", "REMIX"),
        ("2010", "Irresistible (Myon & Shane 54 Vocal Mix)", "Nervo feat. Ollie James", "Zouk Recordings", "REMIX"),
        ("2010", "Triangle (Myon & Shane 54 Classic Mix)", "Nadia Ali", "Smile In Bed", "REMIX"),
        ("2010", "I'm In Love (Myon & Shane 54 Vocal Mix)", "Compact Disco", "Mathouse Records", "REMIX"),
        ("2010", "Im Reaching (Myon & Shane 54 Remix)", "Will Dukster feat. Solncè", "Infra Progressive", "REMIX"),
        ("2009", "Last One Out (Myon & Shane 54 Remix)", "Gabriel Lukosz feat. Rachele Warner", "Lange Recordings", "REMIX"),
        ("2009", "Disconnected (Myon & Shane 54 Vocal Mix)", "Michael Angelo feat. Jenry R", "High Light Records", "REMIX"),
        ("2009", "How Does It Feel (Myon & Shane 54 Vocal Mix)", "Adiva feat. Vicky Fee", "Coldharbour Recordings", "REMIX"),
        ("2009", "Under Your Spell (Myon & Shane 54 Monster Mix)", "Cosmic Gate feat. Aruna", "Black Hole Recordings", "REMIX"),
        ("2009", "Right Here Right Now (Myon & Shane 54 Remix)", "BWO", "Bonnier Music", "REMIX"),
        ("2009", "Faces (Myon & Shane 54 Monster Mix)", "Andy Moor & Ashley Wallbridge", "AVA Recordings", "REMIX"),
        ("2009", "Change Your Mind (Myon & Shane 54 Remix)", "Sunlounger feat. Kyler England", "Magic Island Records", "REMIX"),
        ("2008", "Barcelona (Shane 54 & Myon Retrofuturism Edit)", "BWO", "Capitol Records", "REMIX"),
        ("2013", "Never Rain Down Again (Myon & Shane 54 Dash Up)", "Dash Berlin", "Armada Digital", "REMIX"),
        ("2012", "Love Rain Down (Myon & Shane 54 Summer Of Love Mix)", "Markus Schulz feat. Seri", "Coldharbour Recordings", "REMIX"),
        ("2011", "A Million Stars (Myon & Shane 54 Summer Of Love Mix)", "BT feat. Kirsty Hawkshaw", "Black Hole Recordings", "REMIX"),
        ("2011", "Drowning (Myon & Shane 54 Classic Mix)", "Armin van Buuren feat. Laura V", "Armind", "REMIX"),
        ("2010", "Seven Days And One Week (Myon & Shane 54 Remix)", "Matt Cassar pres. Most Wanted", "Hard On Recordings", "REMIX"),
        ("2010", "One Night In Ibiza (Myon & Shane 54 Remix)", "LTN", "Alter Ego Records", "REMIX"),
        ("2010", "Loneliness (Myon & Shane 54 Remix)", "Tomcraft", "Kosmo Records", "REMIX"),
        ("2009", "Brave (Myon & Shane 54 Monster Mix)", "First State feat. Sarah Howells", "Magik Muzik", "REMIX"),
        ("2009", "Never Say Never (Myon & Shane 54 Remix)", "Armin van Buuren feat. Jacqueline Govaert", "Armind", "REMIX"),
        ("2008", "Out Of The Sky (Myon & Shane 54 Black Army Remix)", "Lange feat. Sarah Howells", "Black Hole Recordings", "REMIX"),
        ("2008", "So Much More (Myon & Shane 54 Remix)", "Andy Moor & Carrie Skipper", "AVA Recordings", "REMIX"),
        ("2008", "Fake Awake (Myon & Shane 54 Remix)", "Andy Moor", "Anjunabeats", "REMIX"),
        ("2011", "Promises (Myon & Shane 54 Summer Of Love Remix)", "Andain", "Black Hole Recordings", "REMIX"),
        ("2011", "Original Sin (Myon & Shane 54 Club Redemption)", "Hybrid", "Distinct'ive Records", "REMIX"),
        ("2011", "Inside 11B (Myon & Shane 54 Summer Of Love Remix)", "LTN", "Morrison Recordings", "REMIX"),
        ("2009", "Just Listen (Myon & Shane 54 Remix)", "Above & Beyond Presents OceanLab", "Anjunabeats", "REMIX"),
        ("2011", "Every Little Beat (Myon & Shane 54 Summer Of Love Mix)", "Above & Beyond feat. Richard Bedford", "Anjunabeats", "REMIX"),
        ("2011", "Sea Lo Que Sea Será (Myon & Shane 54 Summer Of Love Remix)", "Above & Beyond feat. Miguel Bosé", "Anjunabeats", "REMIX"),
        ("2010", "Close To The Stars (Myon & Shane 54 Remix)", "Fabio XB feat. Yves De Lacroix", "S107 Recordings", "REMIX"),
        ("2010", "Let Go (Nic Chagall Remix) (Myon & Shane 54 Refill)", "Aruna with Mark Eteson", "Anjunabeats", "REMIX"),
        ("2009", "Eliana (Myon & Shane 54 Monster Mix)", "Khaz & Boris M.D.", "Coldharbour Recordings", "REMIX"),
        ("2009", "Anatolian Emotions (Myon & Shane 54 Remix)", "Faruk Sabanci & Nurettin Colak", "Arisa Audio", "REMIX"),
        ("2008", "Secret Garden (Myon & Shane 54 Black Army Remix)", "Esmaye", "Black Hole Recordings", "REMIX"),
        ("2008", "Vela (Myon & Shane 54 Remix)", "Jaytech", "Anjunadeep", "REMIX"),
        ("2015", "Louder (Myon & Shane 54 Summer Of Love Remix)", "Paul van Dyk & Roger Shah feat. Daphne Khoo", "Ultra Records", "REMIX"),
        ("2015", "Peace Of Mind (Myon & Shane 54 Summer Of Love Mix)", "Above & Beyond feat. Zoë Johnston", "Anjunabeats", "REMIX"),
        ("2014", "Young & Beautiful (Myon & Shane 54 Summer Of Love Mix)", "Lana Del Rey", "Self-released", "REMIX"),
        ("2013", "Every Breath Is Like A Heartbeat (Myon & Shane 54 Summer Of Love Mix)", "Late Night Alumni", "Ultra Records", "REMIX"),
        ("2013", "Wings (Myon & Shane 54 Summer Of Love Remix)", "Tom Swoon feat. Taylr Renee", "Ultra Music", "REMIX"),
        ("2013", "Hurricane (Myon & Shane 54 In Search Of Sunrise Mix)", "Myon & Shane 54 with Amy Pearson", "Ride Recordings", "REMIX"),
        ("2013", "Outshine (Myon & Shane 54 In Search Of Sunrise Mix)", "Myon & Shane 54 with Natalie Peris", "Ride Recordings", "REMIX"),
        ("2013", "Hello (Myon & Shane 54 Monster Mix)", "Stafford Brothers feat. Lil Wayne & Christina Milian", "CHM", "REMIX"),
        ("2013", "Neon Lights (Cole Plante with Myon & Shane 54 Remix)", "Demi Lovato", "Hollywood Records", "REMIX"),
        ("2012", "Domino (Myon & Shane Vocal Mix)", "Jessie J", "Lava / Universal Republic", "REMIX"),
        ("2012", "Save The Day (Myon & Shane 54 Summer Of Love Mix)", "Aruna", "Black Hole Recordings", "REMIX"),
        ("2012", "Keep Your Secrets (Myon & Shane 54 Summer Of Love Mix)", "Andrew Bayer feat. Molly Bancroft", "Anjunabeats", "REMIX"),
        ("2012", "Alchemy (Myon & Shane 54 Redemption Remix)", "Above & Beyond feat. Zoë Johnston", "Anjunabeats", "REMIX"),
        ("2012", "The Great Divide (Myon & Shane 54 Summer Of Love Mix)", "Velvetine", "Anjunabeats", "REMIX"),
        ("2012", "Our Love (Myon & Shane 54 Summer Of Love Remix)", "Stereo Palma feat. Craig David", "Ego Music", "REMIX"),
        ("2011", "Sinéad (Myon & Shane 54 Triplet Monster Mix)", "Within Temptation", "ZOUK Recordings", "REMIX"),
        ("2011", "Joshua (Myon & Shane 54 Summer Of Love Mix)", "The Japanese Popstars feat. Tom Smith", "Astralwerks", "REMIX"),
        ("2011", "Never Be The Same (Myon & Shane 54 Monster Mix)", "Signum feat. Julie Thompson", "Soundpiercing", "REMIX")]

SOLO = [("2007", "1000 Lullabies", "", "Shah-Music Digital", "SINGLE"),
        ("2006", "Laptop DJ", "", "EMI", "ALBUM"),
        ("2006", "Altass El", "Shane 54 feat. Mester Tamás", "EMI", "PROMO"),
        ("2005", "Kippenvelmeter", "Shane 54 vs Abel Ramos", "DTF Spain", "SINGLE"),
        ("2005", "Futuristic", "Van Eyden & Hampshire feat. Shane 54", "Flux Delux", "SINGLE"),
        ("2004", "VV3", "", "M-RTL Rt.", "SINGLE"),
        ("2004", "My Way", "", "Boring Records", "ALBUM"),
        ("2004", "Back From Your Past", "Misja Helsloot feat. Shane 54", "First Second Records", "SINGLE"),
        ("2003", "69 Remixes", "DJ Junior & Shane 54 feat. Michelle Wild", "", "PROMO"),
        ("2002", "Souvenir De Chine", "", "Afterglow Records", "SINGLE"),
        ("2002", "Equinoxe 4", "", "DTF Recordings", "SINGLE"),
        ("2007", "Lost & Found (Shane 54 vs. Orange Project Remix)", "Mr Sam", "Black Hole Recordings", "REMIX"),
        ("2006", "I Can (Shane 54 Laptop DJ Remix)", "Tatana", "Sirup", "REMIX"),
        ("2006", "És Mégis (Shane 54 Remix)", "Király Linda", "EMI", "REMIX"),
        ("2004", "Gamemaster (Shane 54 Remix)", "Matt Darey presents Lost Tribe", "Darey Products", "REMIX"),
        ("2004", "Titok (Shane 54's Airpanel Edit)", "Szűcs Judith", "SZJ Kiadó", "REMIX"),
        ("2004", "Csak Szeress Vagy Menj Tovább (Shane 54 Clubmix)", "Dukai Regina", "Magneoton", "REMIX"),
        ("2004", "Back From Your Past (S54 Remix)", "Misja Helsloot", "First Second Records", "REMIX"),
        ("2003", "Halló! (Shane 54 Radiomix)", "R-port", "BMG Hungary", "REMIX"),
        ("2003", "Jégbörtön (Shane 54 Radio Edit)", "Évi", "Idea Produkció", "REMIX"),
        ("2002", "Nem Jön Álom A Szememre (Shane 54 Remix)", "TNT", "Magneoton", "REMIX"),
        ("2002", "Érezd Velem (Shane 54's Airpanel Edit)", "Plastic", "Zebra", "REMIX"),
        ("2001", "I Love You (Shane 54 Remix)", "Cosmicman", "EMT Design", "REMIX"),
        ("2001", "Darabokban Hever A Szívem (Shane 54 Radio Mix)", "Bery", "EMI", "REMIX"),
        ("2001", "Miért (Shane 54 Mix)", "V-Tech", "EMI", "REMIX"),
        ("2005", "Rómeó és Júlia: Lehetsz Király (Remix)", "Mindhalálig Musical – Az Operettszínház Sztárjaival", "Pentaton", "REMIX"),
        ("2004", "Time Of Your Life (Shane 54 Pink Flood Remix)", "Paul Oakenfold feat. Perry Farrell", "Chrysalis Records", "REMIX"),
        ("2003", "All Of My Life (Shane 54's Airpanel Mix)", "Aluna", "", "REMIX"),
        ("2005", "Insecurity (Shane 54 Monster Mix)", "Pink Flood feat. Sun", "Beat This Records", "REMIX"),
        ("2004", "VV3 (Shane 54 Monster Mix)", "", "M-RTL Rt.", "REMIX"),
        ("2004", "No More Rain (Shane 54 Refill)", "Malte & Marc De Clarq presents MMDC", "Vandit Records", "REMIX"),
        ("2004", "All Of My Life (Shane 54's Pink Flood Remix)", "Aluna", "Tommy Boy Silver Label", "REMIX"),
        ("2003", "Believe In Me (Shane 54's Pink Flood Remix)", "Sun", "Yris", "REMIX"),
        ("2003", "Don't Think It (Feel It) (Shane 54 Remix)", "Lange feat. Leah", "Radikal Records", "REMIX"),
        ("2003", "Anomaly – Calling Your Name (Shane 54's Monster Mix)", "Libra presents Taylor", "Captivating Sounds", "REMIX"),
        ("2024", "Heist Film / Klondyke", "Andrewboy & Shane 54", "UV Noir", "SINGLE"),
        ("2022", "Kingdom (Remixes)", "Shane 54 feat. London Thor", "Enhanced Progressive", "SINGLE"),
        ("2022", "Kingdom", "Shane 54 feat. London Thor", "Enhanced Progressive", "SINGLE"),
        ("2021", "Panic Attack", "Shane 54 x Alex Sonata & TheRio", "Armind", "SINGLE"),
        ("2021", "Personal Jesus (Cubicore Deep Mix)", "Cubicore feat. Shane 54", "Armind", "SINGLE"),
        ("2020", "Personal Jesus (Cubicore Version)", "Cubicore feat. Shane 54", "Armind", "SINGLE"),
        ("2019", "Out of Time (Ghostdragon Remix)", "Shane 54 & Cubicore feat. Eric Lumière", "Nettwerk", "SINGLE"),
        ("2019", "Out of Time (Petey Mac Remix)", "Shane 54 & Cubicore feat. Eric Lumière", "Nettwerk", "SINGLE"),
        ("2018", "Out of Time", "Shane 54 & Cubicore feat. Eric Lumière", "Nettwerk", "SINGLE"),
        ("2018", "Budokan", "Cubicore & Shane 54", "Armind", "SINGLE"),
        ("2018", "Bacon & Pancakes", "Shane 54", "Zerothree", "EP"),
        ("2018", "Dark & Long (Dark Train)", "Shane 54", "Zerothree", "SINGLE"),
        ("2017", "Return To Love", "Shane 54 & Jonathan Mendelsohn", "Armind", "SINGLE"),
        ("2017", "Paradise (Remixes)", "Shane 54 feat. Jenny Jordan", "Nettwerk", "SINGLE"),
        ("2017", "First Time", "Shane 54", "Nettwerk", "SINGLE"),
        ("2016", "Paradise", "Shane 54 feat. Jenny Jordan", "Nettwerk", "SINGLE"),
        ("2019", "Delirium", "Shane 54 feat. Clara Sofie", "Garuda", "SINGLE"),
        ("2018", "Breathe (Shane 54 Remix)", "Capa feat. Clara Sofie", "Zerothree", "REMIX"),
        ("2017", "Closing In (Shane 54 Remix)", "tyDi & Christopher Tin feat. Dia Frampton", "Global Soundsystem Records", "REMIX"),
        ("—", "Futuristic (Shane 54 Remix)", "Woody Van Eyden & Chris Hampshire feat. Shane 54", "Discover Records", "REMIX"),
        ("2018", "Fosszíliák (Shane 54 & Märklin Remix)", "Zséda", "Magneoton", "REMIX"),
        ("2012", "I Can Feel Your Love (Shane 54 Monster Mix)", "Quadraphonic", "Armada Digital", "REMIX"),
        ("2004", "Scirocco (Shane54 Remix)", "Scirocco", "Fenology Records", "REMIX"),
        ("2003", "Outside (Shane 54's Pink Flood Remix)", "George Michael", "", "REMIX"),
        ("2003", "I'm A Slave 4 U (Shane 54's Pink Flood Remix)", "Britney Spears", "", "REMIX"),
        ("2002", "Music (Shane 54's Pink Flood Remix)", "Madonna", "White label", "REMIX"),
        ("2002", "Believe In Me (Shane 54's Pink Flood Remix)", "Lenny Kravitz", "White label", "REMIX"),
        ("2001", "Ibiza Sunrise (Pink Flood vs. Shane 54 Monster Mix)", "Labworks", "EMT Design", "REMIX")]

DISCO = [("MYON & SHANE 54 · 2008–2015", "https://www.discogs.com/artist/1239503-Myon-Shane-54", MYON),
         ("SHANE 54 · 2001–2022", DISCOGS, SOLO)]

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
.exh{padding:8px 20px 0}
.exh .r{display:flex;gap:14px;padding:12px 0;border-top:1px solid #2a2a2a;min-height:52px;align-items:baseline}
.exh .d{width:104px;flex:none;font-size:13px;font-weight:700;color:var(--ac)}
.exh .p{flex:1;font-size:15px;line-height:1.35}
.bio+.bio{margin-top:16px}
/* podcast: dock, sheet, list */
html.has-dock body{padding-bottom:68px}
html.has-dock .hub{height:calc(100dvh - 68px)}
html.sheet-open{overflow:hidden}
#dock{position:fixed;left:0;right:0;bottom:0;z-index:40;background:#0b0b0b;border-top:2px solid #5ad1ff;padding-bottom:env(safe-area-inset-bottom)}
#dock[hidden],#sheet[hidden]{display:none}
.dk-prog{height:3px;background:#2a2a2a;margin-top:-2px}.dk-prog i{display:block;height:100%;width:0;background:#5ad1ff}
.dk-row{display:flex;align-items:center;gap:4px;padding:6px 8px;height:62px;max-width:560px;margin:0 auto}
.dk-info{flex:1;min-width:0;display:flex;align-items:center;gap:10px;border:0;background:none;color:#fff;font:inherit;text-align:left;padding:0;cursor:pointer;height:50px}
.dk-art{width:48px;height:48px;border-radius:8px;object-fit:cover;background:#000;flex:none}
.dk-t{min-width:0}.dk-t b{display:block;font-size:14px;line-height:1.25;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.dk-t s{display:block;font-size:12px;color:#bbb;text-decoration:none;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ib{width:44px;height:44px;border:0;background:none;color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;flex:none;padding:0}
.ib.main,.dk-play{background:#5ad1ff;color:#111;border-radius:50%}
#sheet{position:fixed;inset:0;z-index:60;background:#0b0b0b;display:flex;flex-direction:column;padding-top:env(safe-area-inset-top);max-width:560px;margin:0 auto}
.sh-head{display:flex;align-items:center;justify-content:space-between;padding:2px 8px;flex:none}
.sh-head small{font-size:11px;font-weight:700;letter-spacing:.14em;color:#5ad1ff}
.sh-main{flex:none;padding:0 20px;display:flex;flex-direction:column;align-items:center}
.sh-art{width:min(44vw,180px);aspect-ratio:1;border-radius:10px;object-fit:cover;background:#000}
.sh-title{font-size:17px;font-weight:700;text-align:center;margin:10px 0 0;line-height:1.25}
.sh-sub{font-size:13px;color:#bbb;text-align:center;min-height:16px}
.pl-bar{-webkit-appearance:none;appearance:none;width:100%;height:36px;margin:4px 0 0;background:transparent;--p:0%}
.pl-bar::-webkit-slider-runnable-track{height:6px;border-radius:3px;background:linear-gradient(to right,#5ad1ff var(--p),#2a2a2a var(--p))}
.pl-bar::-moz-range-track{height:6px;border-radius:3px;background:#2a2a2a}
.pl-bar::-moz-range-progress{height:6px;border-radius:3px;background:#5ad1ff}
.pl-bar::-webkit-slider-thumb{-webkit-appearance:none;width:20px;height:20px;border-radius:50%;background:#fff;border:3px solid #5ad1ff;margin-top:-7px}
.pl-bar::-moz-range-thumb{width:14px;height:14px;border-radius:50%;background:#fff;border:3px solid #5ad1ff}
.pl-times{display:flex;justify-content:space-between;width:100%;font-size:12px;color:#bbb;margin-top:-4px}
.sh-ctl{display:flex;align-items:center;justify-content:center;gap:4px;margin:2px 0 6px}
.sh-ctl .main{width:56px;height:56px}
.sh-spd{width:48px;height:36px;border:2px solid #5ad1ff;border-radius:999px;background:none;color:#5ad1ff;font:inherit;font-weight:700;font-size:13px;margin-right:4px;cursor:pointer}
.sh-tr{flex:none;border-top:1px solid #2a2a2a;padding:0 12px}
.sh-tr summary{min-height:44px;display:flex;align-items:center;font-size:13px;font-weight:700;letter-spacing:.08em;color:#5ad1ff;cursor:pointer}
.sh-tr ol{list-style:none;margin:0 0 8px;padding:0;max-height:34vh;overflow:auto}
.sh-tr button{display:flex;gap:10px;width:100%;min-height:36px;align-items:baseline;text-align:left;background:none;border:0;color:#ddd;font:inherit;font-size:13px;line-height:1.3;padding:6px 0;cursor:pointer}
.sh-tr button:disabled{cursor:default;color:#999}
.sh-tr i{font-style:normal;color:#5ad1ff;min-width:44px;font-variant-numeric:tabular-nums}
.sh-list{flex:1;overflow:auto;border-top:1px solid #2a2a2a;-webkit-overflow-scrolling:touch;padding-bottom:env(safe-area-inset-bottom)}
.eplist{margin-top:8px;border-top:1px solid #2a2a2a}
.ep{display:flex;width:100%;align-items:center;gap:10px;min-height:56px;padding:6px 12px;border:0;border-bottom:1px solid #1f1f1f;background:transparent;color:#fff;text-align:left;font:inherit;cursor:pointer}
.ep img{width:44px;height:44px;border-radius:6px;object-fit:cover;flex:none;background:#000}
.ep .t{flex:1;min-width:0}.ep .t b{display:block;font-size:14px;line-height:1.3}.ep .t s{display:block;font-size:12px;color:#bbb;text-decoration:none}
.ep .d{font-size:12px;color:#bbb;flex:none}
.ep.on{background:#10222a;box-shadow:inset 3px 0 0 #5ad1ff}.ep.pl .t b{color:#5ad1ff}
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
.disc .dt{font-family:'Bowlby One',sans-serif;font-size:22px;color:#5ad1ff;padding:20px 0 0}
.disc .dh{font-size:12px;font-weight:700;letter-spacing:.14em;color:#bbb;padding:22px 0 8px}
.dg{border-top:1px solid #2a2a2a}
.dg summary{list-style:none;display:flex;justify-content:space-between;align-items:center;min-height:48px;font-size:14px;font-weight:700;letter-spacing:.08em;cursor:pointer}
.dg summary::-webkit-details-marker{display:none}
.dg summary em{font-style:normal;font-size:12px;color:#5ad1ff;border:1px solid #5ad1ff;border-radius:999px;padding:2px 9px}
.dg summary::after{content:"+";font-size:20px;color:#5ad1ff;margin-left:12px}
.dg[open] summary::after{content:"–"}
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
    EPMETA = '<meta name="s54-episodes" content="1">' if (SRC / "episodes.json").exists() else ""
    other = "en" if lang == "hu" else "hu"
    # the language switcher goes to the same page in the other language
    sw = f'{root}{other}/{rel}'
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="Shane 54: art, software, music, animation.">
<meta property="og:title" content="{e(title)}"><meta property="og:image" content="{root}assets/img/dj.jpg">
<link rel="icon" href="{root}assets/img/favicon.png">
{EPMETA}
{HEAD}
<link rel="stylesheet" href="{root}assets/style.css">
</head><body style="--ac:{accent}">
<div id="app">{body.replace('@ROOT@', root).replace('@LANG@', lang).replace('@SW@', sw)}</div>
<div id="dock" hidden></div><div id="sheet" hidden></div>
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
        posd = {"art": "50% 55%", "software": "50% 20%", "music": "50% 70%", "animation": "50% 50%"}[s]
        panels += (f'<a class="panel" href="{s}/"><img src="../assets/img/{img}" alt="" style="object-position:{posd}">'
                   f'<div class="sh"></div><div class="tx"><div><small>0{n}</small><h2>{T[s][lang]}</h2><p>{e(T["sub_" + s][lang])}</p></div>'
                   f'<span class="go" style="background:{ACCENT[s]}">→</span></div></a>')
    body = (f'<div class="hub"><header><a class="logo" href="./"><b>SHANE</b><i>54</i></a>'
            f'<a class="lang" href="@SW@">{"EN" if lang == "hu" else "HU"}</a></header>{panels}</div>')
    return page(lang, "", "Shane 54", body, up=1)


def build_art(lang):
    subs = [(T["bio"][lang], "#bio"), (T["gallery"][lang], "#gallery")]
    gal = "".join(f'<a href="@ROOT@assets/img/{p}.jpg"><img loading="lazy" src="@ROOT@assets/img/{p}.jpg" alt="{e(alt)}"></a>' for p, alt in PAINTINGS)
    paras = "".join(f'<p class="bio">{e(t)}</p>' for t in CONTENT["art_bio"][lang])
    exh = "".join(f'<div class="r"><span class="d">{m[lang]} {y}</span><span class="p">{e(pl)}</span></div>' for y, m, pl in EXHIBITIONS)
    body = (top(lang, "art", subs, 2) +
            f'<section id="bio" class="pad"><h1 class="t">ART</h1>{paras}</section>'
            f'<section class="pad" style="padding-bottom:0"><div style="font-size:12px;font-weight:700;letter-spacing:.14em;color:#bbb">{CONTENT["exh_title"][lang]}</div></section>'
            f'<div class="exh">{exh}</div>'
            f'<section id="gallery"><div class="gal">{gal}</div><div class="sig">–SHANE 54–</div></section>' + foot())
    return page(lang, "art/", "Art — Shane 54", body, ACCENT["art"], up=2)


def build_plugins(lang):
    subs = [(T["bio"][lang], "#bio"), (T["delay"][lang], "#delay")]
    body = (top(lang, "software", subs, 2) +
            f'<section id="bio" class="pad"><h1 class="t">SOFTWARE</h1><p class="bio">{e(CONTENT["plugins_bio"][lang])}</p></section>'
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
    return page(lang, "software/", "Software — Shane 54", body, ACCENT["software"], up=2)


def disco_cat(it):
    y, t, c, l, k = it
    if k == "REMIX":
        return "remixes"
    if k in ("ALBUM", "COMP", "MIX", "DIGITAL"):
        return "albums"
    if k == "PROMO" or ("remix" in t.lower() and k != "SINGLE"):
        return "remixes"
    return "singles"


def build_music(lang):
    subs = [(T["bio"][lang], "#bio"), (T["id"][lang], "#id"), (T["disco"][lang], "#disco")]
    rows = ""
    CATN = {"singles": {"hu": "SINGLE-K", "en": "SINGLES"}, "remixes": {"hu": "REMIXEK", "en": "REMIXES"}, "albums": {"hu": "ALBUMOK", "en": "ALBUMS"}}
    for head, link, items in DISCO:
        rows += f'<div class="dh">{head}</div>'
        groups = {"singles": [], "remixes": [], "albums": []}
        for it in items:
            groups[disco_cat(it)].append(it)
        asc = False
        for key_, g in groups.items():
            yr = lambda x: int(x[0]) if x[0].isdigit() else 0
            if asc and key_ == "remixes":
                g.sort(key=lambda x: (yr(x), 0 if x[1].startswith("I Love You (Shane 54") else 1))
            else:
                g.sort(key=lambda x: -yr(x))
        for key in ("singles", "remixes", "albums"):
            g = groups[key]
            if not g:
                continue
            rows += f'<details class="dg"><summary><span>{CATN[key][lang]}</span><em>{len(g)}</em></summary>'
            for y, t, c, l, k in g:
                c = c or ("Myon & Shane 54" if head.startswith("MYON") else "Shane 54")
                sub = " · ".join(x for x in (c, l) if x)
                rows += f'<div class="r"><span class="y">{y}</span><span class="n"><b>{e(t)}</b><s>{e(sub)}</s></span><span class="tag">{k}</span></div>'
            rows += '</details>'
        rows += f'<a class="btn" style="border:2px solid #5ad1ff;margin:12px 0 8px" href="{link}">Discogs →</a>'
    body = (top(lang, "music", subs, 2) +
            '<section id="disco" class="pad sp" style="padding-top:20px">'
            f'<iframe src="https://open.spotify.com/embed/artist/{SPOTIFY}" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy" title="Spotify"></iframe></section>'
            f'<section id="bio" class="pad" style="padding-top:24px"><h1 class="t">MUSIC</h1>{"".join(f'<p class="bio">{e(t)}</p>' for t in CONTENT["music_bio"][lang])}</section>'
            f'<section id="id" class="pad" style="padding-top:8px;padding-bottom:8px"><a class="idc" href="id/"><img src="../../assets/img/id_text.png" alt="International Departures with Shane 54" style="display:block;width:78%;height:auto"><span style="font-size:22px">→</span></a></section>'
            f'<div id="disco" class="disc"><div class="dt">{T["disco"][lang]}</div>{rows}</div>'
            + foot())
    return page(lang, "music/", "Music — Shane 54", body, ACCENT["music"], up=2)


def build_id(lang):
    subs = [(T["bio"][lang], "../#bio"), (T["id"][lang], "#"), (T["disco"][lang], "../#disco")]
    subs_html = top(lang, "music", subs, 3)
    subs_html = subs_html.replace('<a href="#">ID</a>', '<a href="#" class="on">ID</a>').replace('<a href="../#bio" class=on>', '<a href="../#bio">')
    body = (subs_html +
            f'<section class="pad" style="padding:12px 16px 0"><a href="../" style="display:flex;align-items:center;min-height:44px;font-size:13px;font-weight:700;color:#5ad1ff">{T["back"][lang]}</a>'
            '<h1 style="margin:0 0 10px"><img src="../../../assets/img/id_text.png" alt="International Departures with Shane 54" style="display:block;width:100%;max-width:300px;height:auto"></h1>'
            f'<p class="bio" style="font-size:15px;line-height:1.5">{e(CONTENT["id_bio"][lang])}</p></section>'
            f'<div id="idlist" class="eplist"><p class="bio" style="margin:0;padding:16px;color:#bbb;font-size:14px">{e(CONTENT["id_soon"][lang])}</p></div>' + foot())
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


def build_player_preview():
    body = ('<div style="padding:12px 16px 0"><a class="logo" href="../hu/music/id/"><b>SHANE</b><i>54</i></a></div>'
            '<section class="pad" style="padding:8px 16px 0"><h1 class="t" style="font-size:30px;margin-bottom:6px">PLAYER PREVIEW</h1>'
            '<p class="bio" style="font-size:14px">Demo: 3 placeholder episodes (test tone). Press play, then use the logo link above: the music keeps playing on the other page.</p></section>'
            '<div id="idlist" class="eplist" data-demo="1"></div>')
    return page("hu", "", "Player preview", body, ACCENT["music"], up=1).replace("<head>", '<head><meta name="robots" content="noindex">', 1)


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
    (OUT / "assets" / "demo").mkdir()
    shutil.copy(SRC / "demo" / "demo.wav", OUT / "assets" / "demo" / "demo.wav")
    if (EPJSON := SRC / "episodes.json").exists():
        shutil.copy(EPJSON, OUT / "assets" / "episodes.json")
    if (SRC / "ep").exists():
        shutil.copytree(SRC / "ep", OUT / "assets" / "ep")
    shutil.copy(SRC / "site.js", OUT / "assets" / "site.js")
    (OUT / "assets" / "style.css").write_text(CSS, "utf-8")
    (OUT / ".nojekyll").write_text("")
    (OUT / "index.html").write_text(
        '<!doctype html><meta charset="utf-8"><title>Shane 54</title><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<script>location.replace((navigator.language||"hu").slice(0,2)=="hu"?"hu/":"en/")</script>'
        '<noscript><meta http-equiv="refresh" content="0;url=hu/"></noscript><a href="hu/">Shane 54</a>', "utf-8")
    (OUT / "preview-player").mkdir()
    (OUT / "preview-player" / "index.html").write_text(build_player_preview(), "utf-8")
    for lang in LANGS:
        for rel, fn in (("", build_hub), ("art", build_art), ("software", build_plugins), ("music", build_music),
                        ("music/id", build_id), ("animation", build_animation)):
            d = OUT / lang / rel
            d.mkdir(parents=True, exist_ok=True)
            (d / "index.html").write_text(fn(lang), "utf-8")
    print("built ->", OUT)


if __name__ == "__main__":
    main()
