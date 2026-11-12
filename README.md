# Diritti al Lavoro

Informative website explaining workers' rights in Italy, from employment contracts and pay to working hours, family leave, dignity at work, health and safety, end of employment and trade union rights.

The content is in Italian, because it is written for people working in Italy. Every legal statement links to its official source (Normattiva, Senate, Ministry of Labour, National Labour Inspectorate, INPS, INAIL, CNEL, Constitutional Court).

**Live site:** https://ambrosinofabio.github.io/diritti-al-lavoro/

## Structure

The guide follows the usual structure of Italian labour law: trade union law, the employment relationship, its termination and social security, plus a help section. Each section and group has an index page that links to its sub-pages.

| Section | Group | Pages |
|---|---|---|
| Diritto sindacale | | Constitution, Workers' Statute, collective agreements (CCNL), union rights, strikes |
| Rapporto di lavoro | Diritti e obblighi delle parti | Interviews, monitoring, disciplinary procedure, safety, stress, discrimination, harassment, whistleblowing, workplace culture |
| | Il contratto e le mansioni | Hiring, probation, fixed-term, part-time, apprenticeship, agency work, duties and transfers |
| | Il trattamento economico | Pay, payslip (with checklist), severance pay (TFR) |
| | Tempo e luogo di lavoro | Working hours (with weekly check), overtime, rest and night work, holidays, remote work, free time |
| | Malattia, famiglia e congedi | Sick leave, law 104, maternity, paternity, parental leave |
| Estinzione del rapporto | | Resignation, individual dismissal, unfair dismissal and remedies (art. 18 and *tutele crescenti*), how to challenge a dismissal, collective dismissal, final entitlements |
| Previdenza | | Contributions, NASpI unemployment benefit, pensions, supplementary pension funds, work accidents and occupational diseases (INAIL) |
| Aiuto | | Where to get help, deadline calculator, glossary, sources |

The menu, breadcrumbs, "In questa sezione" box and previous/next links are repeated in every page. They are generated, together with the section index pages and the search index `js/indice.js`, by `tools/naviga.py` from the `STRUTTURA` list at the top of the script. To add a page: create it (with its `<h1>`, meta description, `in-sezione` box and `naviga-pagine` block), add it to `STRUTTURA`, add its search keywords to `js/indice.js`, then run `python tools/naviga.py` from the site folder. `basi.html` is kept as a redirect to `sindacato.html` for old links.

## Interactive features

- Search across the whole guide (home page).
- Deadline calculator for dismissal, resignation, disciplinary notices, fixed-term contracts and unemployment benefit.
- Weekly working hours check against the legal limits.
- Payslip checklist, saved in the browser's local storage.
- Glossary filter and expandable FAQs.

## Files

```
*.html              # Pages
css/style.css       # Stylesheet
js/main.js          # Menu, search and interactive tools
js/indice.js        # Search index of all pages
fonts/              # Titillium Web (SIL Open Font License, see fonts/OFL.txt)
tools/naviga.py     # Regenerates navigation and search index (not used by the site)
```

## Design choices

- Plain HTML, CSS and JavaScript, no frameworks.
- Titillium Web font, hosted locally: no external fonts, cookies, trackers or third-party requests.
- A clear notice states that the site is independent and not an official institutional website.
- Clear separation between legal obligations and good practices.
- Responsive layout with a horizontal menu and dropdowns on desktop, a collapsible menu on mobile.

## Running locally

Open `index.html` in a browser, or start a local server:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/index.html`.

## Disclaimer

The content is for information only and does not replace advice from a trade union, a *patronato* or an employment lawyer. Last content review: November 2026.

## Credits

Titillium Web was designed by the Accademia di Belle Arti di Urbino and is released under the SIL Open Font License 1.1.

## License

- **Code** (HTML, CSS, JS): [MIT](LICENSE).
- **Original text**: [CC BY 4.0](LICENSE-CONTENT.md), credited as "Diritti al Lavoro — Fabio Ambrosino".
- **Quoted legal texts** (Constitution, codes, laws, decrees): official acts, not covered by copyright under art. 5 of Italian Law 633/1941, and therefore not covered by the licenses above.
- **Font**: Titillium Web, SIL Open Font License 1.1 ([fonts/OFL.txt](fonts/OFL.txt)).

## Disclaimer and privacy

- Independent, non-commercial informative site. It is not an official website and is not affiliated with any public body or trade union. No institutional logos or emblems are used.
- The text was drafted with the help of AI tools, then checked against the official sources linked on each page and reviewed by the author, Fabio Ambrosino, who holds editorial responsibility (see Article 50(4) of the EU AI Act).
- The content is general information, not legal advice. It may contain errors or be out of date; each page shows the date of the last review. Errors can be reported through [GitHub Issues](https://github.com/AmbrosinoFabio/diritti-al-lavoro/issues).
- No cookies, trackers or third-party requests. The payslip checklist is saved in the visitor's browser only (localStorage). The site is hosted on GitHub Pages, which logs visitors' IP addresses for security purposes.

