"""Rigenera la navigazione di Diritti al Lavoro a partire da STRUTTURA.

Aggiorna in tutte le pagine: menu, briciole, riquadro "In questa sezione",
link precedente/successiva; nelle pagine indice di sezione e di gruppo:
titolo, descrizione, sommario e schede; nella home le schede delle sezioni;
infine js/indice.js (l'indice della ricerca).

Titolo e descrizione delle pagine di contenuto si leggono dalla pagina stessa
(<h1> e meta description). Le parole chiave della ricerca restano quelle già
presenti in js/indice.js.

Uso, dalla cartella del sito:  python tools/naviga.py
"""
import html, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# sezione: (url, titolo, descrizione, contenuto)
# contenuto = lista di pagine oppure lista di gruppi (url, titolo, descrizione, pagine)
STRUTTURA = [
    ("sindacato.html", "Diritto sindacale",
     "Le fonti del diritto del lavoro, il contratto collettivo, la libertà e l'attività sindacale e il diritto di sciopero.",
     ["costituzione.html", "statuto-lavoratori.html", "contratto-collettivo.html",
      "diritti-sindacali.html", "sciopero.html"]),
    ("rapporto-di-lavoro.html", "Rapporto di lavoro",
     "Diritti e obblighi delle parti, tipi di contratto, mansioni, retribuzione, orario e assenze: tutto ciò che regola il lavoro dipendente giorno per giorno.",
     [
        ("tutele.html", "Diritti e obblighi delle parti",
         "Cosa il datore di lavoro può e non può fare o chiederti e quali obblighi ha: opinioni, controlli, sanzioni disciplinari, sicurezza, discriminazioni, molestie e ambiente di lavoro.",
         ["opinioni-e-colloqui.html", "controlli.html", "disciplinare.html", "sicurezza.html",
          "stress.html", "discriminazioni.html", "molestie-e-mobbing.html", "whistleblowing.html",
          "ambiente-di-lavoro.html"]),
        ("contratti.html", "Il contratto e le mansioni",
         "L'assunzione, i tipi di contratto di lavoro dipendente e le mansioni: prova, tempo determinato, part-time, apprendistato, lavoro tramite agenzia, cambi di mansione e trasferimenti.",
         ["assunzione.html", "periodo-di-prova.html", "tempo-determinato.html", "part-time.html",
          "apprendistato.html", "somministrazione.html", "mansioni-e-trasferimenti.html"]),
        ("paga.html", "Il trattamento economico",
         "Quanto e come deve essere pagato il tuo lavoro, come leggere la busta paga e come funziona il TFR.",
         ["retribuzione.html", "busta-paga.html", "tfr.html"]),
        ("tempo.html", "Tempo e luogo di lavoro",
         "I limiti del tempo di lavoro e il luogo in cui si lavora: orario, straordinari, pause, riposi, lavoro notturno, ferie, lavoro agile e tempo libero.",
         ["orario.html", "straordinari.html", "riposi-e-pause.html", "ferie.html",
          "lavoro-agile.html", "tempo-libero.html"]),
        ("famiglia.html", "Malattia, famiglia e congedi",
         "Malattia, permessi per assistere i familiari, maternità, paternità e congedo parentale.",
         ["malattia.html", "legge-104.html", "maternita.html", "paternita.html", "congedo-parentale.html"]),
     ]),
    ("fine-rapporto.html", "Estinzione del rapporto",
     "Dimissioni, licenziamento individuale e collettivo, tutele contro il licenziamento illegittimo, come impugnarlo e cosa ti spetta quando il rapporto finisce.",
     ["dimissioni.html", "licenziamento.html", "licenziamento-illegittimo.html",
      "impugnare-licenziamento.html", "licenziamento-collettivo.html", "cosa-spetta.html"]),
    ("previdenza.html", "Previdenza",
     "Contributi, indennità di disoccupazione, pensione, previdenza complementare, infortuni e malattie professionali.",
     ["contributi.html", "naspi.html", "pensione.html", "previdenza-complementare.html",
      "infortuni.html"]),
    ("aiuto.html", "Aiuto",
     "Cosa fare quando un diritto non viene rispettato: a chi rivolgersi, come calcolare le scadenze, il glossario e le fonti.",
     ["a-chi-rivolgersi.html", "calcola-scadenze.html", "glossario.html", "fonti.html"]),
]

# pagine che non fanno parte della struttura e non vanno toccate (rinvii)
ESCLUSE = {"basi.html"}

# ---------- Dati ----------
indice_src = (ROOT / "js/indice.js").read_text(encoding="utf-8")
VOCE = re.compile(r'\{ url: "([^"]+)", titolo: "((?:[^"\\]|\\.)*)", descrizione: "((?:[^"\\]|\\.)*)", chiavi: "((?:[^"\\]|\\.)*)", sezione: "((?:[^"\\]|\\.)*)" \}')
CHIAVI = {m[1]: m[4] for m in VOCE.finditer(indice_src)}
intestazione_indice = indice_src.split("window.INDICE_GUIDA")[0]

def leggi(url):
    return (ROOT / url).read_text(encoding="utf-8")

DATI = {}
POS = {}
for sez in STRUTTURA:
    s_url, s_tit, s_desc, cont = sez
    DATI[s_url] = {"titolo": s_tit, "descrizione": s_desc}
    POS[s_url] = {"sezione": sez, "gruppo": None, "tipo": "sezione"}
    for g in cont:
        if isinstance(g, tuple):
            DATI[g[0]] = {"titolo": g[1], "descrizione": g[2]}
            POS[g[0]] = {"sezione": sez, "gruppo": g, "tipo": "gruppo"}
            for p in g[3]:
                POS[p] = {"sezione": sez, "gruppo": g, "tipo": "pagina", "fratelli": g[3], "nome_box": g[1]}
        else:
            POS[g] = {"sezione": sez, "gruppo": None, "tipo": "pagina", "fratelli": cont, "nome_box": s_tit}

for url, p in POS.items():
    if p["tipo"] != "pagina":
        continue
    h = leggi(url)
    tit = re.search(r"<h1>(.*?)</h1>", h, re.S)
    desc = re.search(r'<meta name="description" content="([^"]*)">', h)
    if not tit or not desc:
        sys.exit(f"{url}: manca <h1> o meta description")
    DATI[url] = {"titolo": tit.group(1).strip(), "descrizione": html.unescape(desc.group(1))}

def t(url): return DATI[url]["titolo"]
def d(url): return html.escape(DATI[url]["descrizione"], quote=True).replace("&#x27;", "'")

# ---------- Generatori ----------
def menu(corrente):
    sez_corr = POS.get(corrente, {}).get("sezione")
    cur = lambda u: ' aria-current="page"' if u == corrente else ''
    r = ['<nav class="menu" id="menu" aria-label="Sezioni della guida">',
         '    <div class="menu-interno">',
         '      <button type="button" class="menu-apri" id="menuApri" aria-expanded="false" aria-controls="menuLista">Menu &#9776;</button>',
         '      <ul class="menu-lista" id="menuLista">']
    for sez in STRUTTURA:
        s_url, s_tit, _, cont = sez
        gruppi = bool(cont) and isinstance(cont[0], tuple)
        attivo = ' aria-current="true"' if sez is sez_corr else ''
        r.append(f'        <li class="menu-voce{" menu-voce-larga" if gruppi else ""}">')
        r.append(f'          <a class="menu-link" href="{s_url}"{attivo}>{s_tit}</a>')
        if gruppi:
            r.append('          <div class="sottomenu sottomenu-largo">')
            for g in cont:
                r += ['            <div class="sottomenu-gruppo">',
                      f'              <a class="sottomenu-titolo" href="{g[0]}"{cur(g[0])}>{g[1]}</a>',
                      '              <ul>']
                r += [f'                <li><a href="{p}"{cur(p)}>{t(p)}</a></li>' for p in g[3]]
                r += ['              </ul>', '            </div>']
            r.append('          </div>')
        elif cont:
            r.append('          <ul class="sottomenu">')
            r += [f'            <li><a href="{p}"{cur(p)}>{t(p)}</a></li>' for p in cont]
            r.append('          </ul>')
        r.append('        </li>')
    r += ['      </ul>', '    </div>', '  </nav>']
    return "\n".join(r)

def briciole(url):
    p = POS[url]
    passi = [("index.html", "Home"), (p["sezione"][0], p["sezione"][1])]
    if p["gruppo"]:
        passi.append((p["gruppo"][0], p["gruppo"][1]))
    if p["tipo"] == "pagina":
        passi.append((url, t(url)))
    li = "".join(f'<li><a href="{u}">{n}</a></li>' for u, n in passi[:-1])
    return f'<nav class="briciole" aria-label="Percorso"><ol>{li}<li aria-current="page">{passi[-1][1]}</li></ol></nav>'

def in_sezione(url):
    p = POS[url]
    r = ['<aside class="in-sezione testo" aria-label="Altre pagine della sezione">',
         f'        <h2>In questa sezione: {p["nome_box"]}</h2>', '        <ul>']
    corrente = ' aria-current="page"'
    r += [f'          <li><a href="{f}"{corrente if f == url else ""}>{t(f)}</a></li>' for f in p["fratelli"]]
    r += ['        </ul>', '      </aside>']
    return "\n".join(r)

def vicine(url):
    fr = POS[url]["fratelli"]; i = fr.index(url)
    r = ['<nav class="naviga-pagine testo" aria-label="Pagine vicine">']
    if i > 0:
        r.append(f'        <a class="precedente" href="{fr[i-1]}"><span>Precedente</span>{t(fr[i-1])}</a>')
    if i < len(fr) - 1:
        r.append(f'        <a class="successiva" href="{fr[i+1]}"><span>Successiva</span>{t(fr[i+1])}</a>')
    r.append('      </nav>')
    return "\n".join(r)

def schede(urls):
    r = ['<ul class="schede">']
    r += [f'        <li><a href="{u}"><strong>{t(u)}</strong><span>{d(u)}</span></a></li>' for u in urls]
    r.append('      </ul>')
    return "\n".join(r)

def figli(url):
    p = POS[url]
    if p["tipo"] == "gruppo":
        return p["gruppo"][3]
    return [g[0] if isinstance(g, tuple) else g for g in p["sezione"][3]]

def sub(pattern, nuovo, testo, url):
    nuovo_testo, n = re.subn(pattern, lambda m: nuovo, testo, count=1, flags=re.S)
    if n != 1:
        sys.exit(f"{url}: blocco non trovato ({pattern[:40]})")
    return nuovo_testo

# ---------- Pagine ----------
for f in sorted(ROOT.glob("*.html")):
    url = f.name
    if url in ESCLUSE:
        continue
    h = f.read_text(encoding="utf-8")
    h = sub(r'<nav class="menu" id="menu".*?</nav>', menu(url), h, url)
    if url == "index.html":
        h, n = re.subn(r'(<h2>Le sezioni della guida</h2>\s*)<ul class="schede">.*?</ul>',
                       lambda m: m.group(1) + schede([s[0] for s in STRUTTURA]), h, count=1, flags=re.S)
        if n != 1:
            sys.exit("index.html: schede delle sezioni non trovate")
    elif url not in POS:
        sys.exit(f"pagina fuori struttura: {url} (aggiungila a STRUTTURA o a ESCLUSE)")
    else:
        p = POS[url]
        h = sub(r'<nav class="briciole".*?</nav>', briciole(url), h, url)
        if p["tipo"] == "pagina":
            h = sub(r'<aside class="in-sezione.*?</aside>', in_sezione(url), h, url)
            h = sub(r'<nav class="naviga-pagine.*?</nav>', vicine(url), h, url)
        else:
            h = sub(r'<title>.*?</title>', f'<title>{t(url)} | Diritti al Lavoro</title>', h, url)
            h = sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{d(url)}">', h, url)
            occhiello = "Sezione" if p["tipo"] == "sezione" else p["sezione"][1]
            h = sub(r'<p class="occhiello">.*?</p>', f'<p class="occhiello">{occhiello}</p>', h, url)
            h = sub(r'<h1>.*?</h1>', f'<h1>{t(url)}</h1>', h, url)
            h = sub(r'<p class="sommario">.*?</p>', f'<p class="sommario">{d(url)}</p>', h, url)
            h = sub(r'<ul class="schede">.*?</ul>', schede(figli(url)), h, url)
    f.write_text(h, encoding="utf-8", newline="\n")

# ---------- js/indice.js ----------
def js(s): return s.replace("\\", "\\\\").replace('"', '\\"')
righe = []
def voce(u, sezione):
    righe.append(f'    {{ url: "{u}", titolo: "{js(t(u))}", descrizione: "{js(DATI[u]["descrizione"])}", '
                 f'chiavi: "{js(CHIAVI.get(u, ""))}", sezione: "{js(sezione)}" }},')
for s_url, s_tit, _, cont in STRUTTURA:
    voce(s_url, "Sezione")
    for g in cont:
        if isinstance(g, tuple):
            voce(g[0], s_tit)
            for p in g[3]:
                voce(p, g[1])
        else:
            voce(g, s_tit)
(ROOT / "js/indice.js").write_text(
    intestazione_indice + "window.INDICE_GUIDA = [\n" + "\n".join(righe) + "\n];\n",
    encoding="utf-8", newline="\n")
print(f"ok: {len(righe)} voci nell'indice")
