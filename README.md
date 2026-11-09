# Diritti al Lavoro

Informative website explaining workers' rights in Italy: working hours and overtime, leave, family, dignity and workplace monitoring, health and safety, harassment, end of employment, trade unions and where to get help.

The content is in Italian, because it is written for people working in Italy. Every legal statement links to its official source (Normattiva, Senato, Ministero del Lavoro, INL, INPS, INAIL, CNEL).

> Status: work in progress, not published yet.

## Structure

```
index.html            # Home: key numbers and guide sections
costituzione.html     # Constitution articles on work
contratto.html        # Contract, probation period, pay and payslip
orario.html           # Working hours, overtime, breaks and rest
ferie-assenze.html    # Holidays, sick leave, law 104 leave
famiglia.html         # Maternity, paternity, parental leave, remote work
dignita.html          # What employers can and cannot do
sicurezza.html        # Health and safety (Legislative Decree 81/2008)
molestie.html         # Discrimination, harassment, whistleblowing
ambiente.html         # Healthy workplace and good management practices
fine-rapporto.html    # Resignation, dismissal and deadlines
sindacato.html        # Trade union rights and strikes
aiuto.html            # Where to get help
fonti.html            # Full list of sources
css/style.css         # Stylesheet
js/main.js            # Mobile table of contents toggle
```

## Design choices

- Plain HTML, CSS and JavaScript, no frameworks and no build step.
- System fonts only: no external fonts, cookies, trackers or third-party requests.
- Clear separation between legal obligations and good practices.
- Responsive layout with a sticky table of contents on desktop.

## Running locally

Open `index.html` in a browser, or start a local server:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/index.html`.

## Disclaimer

The content is for information only and does not replace advice from a trade union, a *patronato* or an employment lawyer. Last content review: November 2026.
