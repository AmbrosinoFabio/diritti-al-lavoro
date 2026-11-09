/*=========================================================
    Diritti al Lavoro
    main.js - menu, ricerca e strumenti interattivi.
    Ogni funzione si attiva solo se la pagina contiene
    gli elementi che le servono.
=========================================================*/


/*==========================
MENU SU SCHERMI PICCOLI
==========================*/

const menu = document.getElementById("menu");
const menuApri = document.getElementById("menuApri");

if(menu && menuApri){

    menuApri.addEventListener("click", () => {

        const aperto = menu.classList.toggle("aperto");

        menuApri.setAttribute("aria-expanded", aperto ? "true" : "false");

        menuApri.textContent = aperto ? "Chiudi menu ✕" : "Menu ☰";

    });

}


/*==========================
FUNZIONI DI SUPPORTO
==========================*/

// toglie accenti e maiuscole, per cercare "liberta" e trovare "libertà"
function normalizza(testo){

    return testo
        .toLowerCase()
        .normalize("NFD")
        .replace(/[̀-ͯ]/g, "");

}

function formattaData(data){

    return data.toLocaleDateString("it-IT", {
        weekday: "long",
        day: "numeric",
        month: "long",
        year: "numeric"
    });

}

function aggiungiGiorni(data, giorni){

    const nuova = new Date(data.getTime());

    nuova.setDate(nuova.getDate() + giorni);

    return nuova;

}

// legge un campo data (aaaa-mm-gg) come data locale, senza problemi di fuso orario
function leggiData(valore){

    if(!valore) return null;

    const parti = valore.split("-").map(Number);

    return new Date(parti[0], parti[1] - 1, parti[2]);

}


/*==========================
RICERCA NELLA GUIDA
==========================*/

const campoRicerca = document.getElementById("campoRicerca");
const listaRisultati = document.getElementById("risultatiRicerca");

if(campoRicerca && listaRisultati && window.INDICE_GUIDA){

    campoRicerca.addEventListener("input", () => {

        const parole = normalizza(campoRicerca.value.trim()).split(/\s+/).filter(Boolean);

        listaRisultati.innerHTML = "";

        if(parole.length === 0) return;

        const trovati = window.INDICE_GUIDA.filter(pagina => {

            const testo = normalizza(pagina.titolo + " " + pagina.descrizione + " " + pagina.chiavi + " " + pagina.sezione);

            return parole.every(parola => testo.includes(parola));

        });

        if(trovati.length === 0){

            const vuoto = document.createElement("li");
            vuoto.textContent = "Nessuna pagina trovata. Prova con un'altra parola, ad esempio \"ferie\", \"licenziamento\" o \"straordinari\".";
            listaRisultati.appendChild(vuoto);
            return;

        }

        trovati.slice(0, 12).forEach(pagina => {

            const voce = document.createElement("li");
            const link = document.createElement("a");
            const dettaglio = document.createElement("small");

            link.href = pagina.url;
            link.textContent = pagina.titolo;
            dettaglio.textContent = pagina.sezione + " · " + pagina.descrizione;

            link.appendChild(dettaglio);
            voce.appendChild(link);
            listaRisultati.appendChild(voce);

        });

    });

}


/*==========================
FILTRO DEL GLOSSARIO
==========================*/

const filtroGlossario = document.getElementById("filtroGlossario");
const glossario = document.getElementById("glossario");

if(filtroGlossario && glossario){

    const termini = glossario.querySelectorAll("dt");
    const vuoto = document.getElementById("glossarioVuoto");

    filtroGlossario.addEventListener("input", () => {

        const cerca = normalizza(filtroGlossario.value.trim());
        let visibili = 0;

        termini.forEach(termine => {

            const definizione = termine.nextElementSibling;
            const testo = normalizza(termine.textContent + " " + definizione.textContent);
            const mostra = testo.includes(cerca);

            termine.hidden = !mostra;
            definizione.hidden = !mostra;

            if(mostra) visibili++;

        });

        if(vuoto) vuoto.hidden = visibili > 0;

    });

}


/*==========================
CONTROLLO DELLA SETTIMANA DI LAVORO
==========================*/

const formSettimana = document.getElementById("formSettimana");

if(formSettimana){

    formSettimana.addEventListener("submit", (evento) => {

        evento.preventDefault();

        const esito = document.getElementById("esitoSettimana");
        const campi = formSettimana.querySelectorAll("input[data-giorno]");

        let totale = 0;
        let giorniLavorati = 0;
        const giorniLunghi = [];

        campi.forEach(campo => {

            const ore = parseFloat(campo.value.replace(",", ".")) || 0;

            totale += ore;

            if(ore > 0) giorniLavorati++;

            if(ore > 13) giorniLunghi.push(campo.dataset.giorno);

        });

        const messaggi = [];

        messaggi.push("<p>Hai indicato <strong>" + totale.toLocaleString("it-IT") + " ore</strong> in " + giorniLavorati + " giorni.</p>");

        const punti = [];

        if(totale > 40){
            punti.push("<li>Hai superato le <strong>40 ore</strong> dell'orario normale: le ore in più sono straordinario e vanno registrate e pagate con la maggiorazione del tuo CCNL (o recuperate con riposi compensativi, se previsto).</li>");
        }

        if(totale > 48){
            punti.push("<li class=\"esito-no\">Hai superato le 48 ore. La legge fissa 48 ore come media massima su un periodo fino a 4 mesi (estendibile dal CCNL): una singola settimana sopra le 48 ore non è automaticamente illegittima, ma se succede spesso la media rischia di essere superata.</li>");
        }

        if(giorniLunghi.length > 0){
            punti.push("<li class=\"esito-no\">In questi giorni hai lavorato più di 13 ore: " + giorniLunghi.join(", ") + ". Con un riposo di 11 ore consecutive ogni 24, una giornata non dovrebbe superare 13 ore, salvo deroghe dei contratti collettivi con riposi compensativi.</li>");
        }

        if(giorniLavorati >= 7){
            punti.push("<li class=\"esito-no\">Hai lavorato tutti e 7 i giorni. Il riposo settimanale di almeno 24 ore consecutive si calcola come media su 14 giorni: verifica di recuperarlo nella settimana successiva.</li>");
        }

        if(punti.length === 0){
            messaggi.push("<p class=\"esito-ok\">In base ai dati inseriti la settimana rientra nei limiti di legge.</p>");
        }else{
            messaggi.push("<ul>" + punti.join("") + "</ul>");
        }

        messaggi.push("<p class=\"fonte\">Controllo indicativo basato sul D.Lgs. 66/2003. Il tuo contratto collettivo può prevedere regole diverse o migliori.</p>");

        esito.innerHTML = messaggi.join("");

    });

}


/*==========================
CALCOLO DELLE SCADENZE
==========================*/

const formScadenze = document.getElementById("formScadenze");

if(formScadenze){

    const regole = {
        licenziamento: {
            titolo: "Licenziamento ricevuto",
            passi: [
                { giorni: 60, testo: "Ultimo giorno per contestare il licenziamento per iscritto (60 giorni)" },
                { giorni: 240, testo: "Ultimo giorno indicativo per depositare il ricorso o chiedere la conciliazione, se hai contestato proprio il 60° giorno (60 + 180 giorni). Se contesti prima, i 180 giorni decorrono dalla tua contestazione." }
            ]
        },
        dimissioni: {
            titolo: "Dimissioni inviate online",
            passi: [
                { giorni: 7, testo: "Ultimo giorno per revocare le dimissioni (7 giorni dall'invio)" }
            ]
        },
        disciplinare: {
            titolo: "Contestazione disciplinare ricevuta",
            passi: [
                { giorni: 5, testo: "Fino a questa data non può esserti applicata una sanzione più grave del rimprovero verbale: usa questi giorni per difenderti (5 giorni)" }
            ]
        },
        termine: {
            titolo: "Fine di un contratto a tempo determinato",
            passi: [
                { giorni: 180, testo: "Ultimo giorno per impugnare il contratto a termine (180 giorni dalla cessazione)" }
            ]
        },
        naspi: {
            titolo: "Fine del rapporto di lavoro",
            passi: [
                { giorni: 68, testo: "Ultimo giorno per presentare la domanda di NASpI all'INPS (68 giorni)" }
            ]
        }
    };

    formScadenze.addEventListener("submit", (evento) => {

        evento.preventDefault();

        const esito = document.getElementById("esitoScadenze");
        const tipo = document.getElementById("tipoScadenza").value;
        const data = leggiData(document.getElementById("dataScadenza").value);

        if(!data){
            esito.innerHTML = "<p class=\"esito-no\">Inserisci una data.</p>";
            return;
        }

        const regola = regole[tipo];
        const oggi = new Date();
        oggi.setHours(0, 0, 0, 0);

        let html = "<h3>" + regola.titolo + " il " + formattaData(data) + "</h3><ul>";

        regola.passi.forEach(passo => {

            const scadenza = aggiungiGiorni(data, passo.giorni);
            const mancano = Math.round((scadenza - oggi) / 86400000);

            let stato = "";
            if(mancano < 0) stato = " <span class=\"esito-no\">(termine già passato)</span>";
            else if(mancano === 0) stato = " <span class=\"esito-no\">(scade oggi)</span>";
            else stato = " (mancano " + mancano + " giorni)";

            html += "<li><strong>" + formattaData(scadenza) + "</strong>" + stato + "<br>" + passo.testo + "</li>";

        });

        html += "</ul><p class=\"fonte\">Calcolo indicativo in giorni di calendario. Quando una scadenza cade di sabato, domenica o in un giorno festivo possono valere regole particolari: non aspettare l'ultimo giorno e fatti assistere da un sindacato o da un avvocato.</p>";

        esito.innerHTML = html;

    });

}


/*==========================
CHECKLIST (es. busta paga)
I segni di spunta restano salvati nel browser.
==========================*/

document.querySelectorAll("[data-checklist]").forEach(lista => {

    const chiave = "checklist-" + lista.dataset.checklist;
    const caselle = lista.querySelectorAll("input[type=checkbox]");
    const barra = document.querySelector("[data-progresso='" + lista.dataset.checklist + "'] span");
    const conteggio = document.querySelector("[data-conteggio='" + lista.dataset.checklist + "']");

    let salvati = [];

    try{
        salvati = JSON.parse(localStorage.getItem(chiave)) || [];
    }catch(errore){
        salvati = [];
    }

    function aggiorna(){

        const fatti = Array.from(caselle).filter(c => c.checked).length;

        if(barra) barra.style.width = Math.round(fatti / caselle.length * 100) + "%";

        if(conteggio) conteggio.textContent = fatti + " di " + caselle.length + " controlli completati";

        try{
            localStorage.setItem(chiave, JSON.stringify(Array.from(caselle).map(c => c.checked)));
        }catch(errore){
            // se il browser non permette di salvare, la checklist funziona comunque
        }

    }

    caselle.forEach((casella, i) => {

        casella.checked = Boolean(salvati[i]);
        casella.addEventListener("change", aggiorna);

    });

    aggiorna();

});
