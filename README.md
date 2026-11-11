# Diritti al Lavoro

Informative website explaining workers' rights in Italy, from employment contracts and pay to working hours, family leave, dignity at work, health and safety, end of employment and trade union rights.

The content is in Italian, because it is written for people working in Italy. Every legal statement links to its official source (Normattiva, Senate, Ministry of Labour, National Labour Inspectorate, INPS, INAIL, CNEL, Constitutional Court).

> Status: work in progress, not published yet.

## Structure

The guide has 52 pages organised in 9 sections. Each section has an index page that links to its sub-pages.

| Section | Pages |
|---|---|
| Le basi | Constitution, collective agreements (CCNL), Workers' Statute |
| Contratti | Hiring, probation, fixed-term, part-time, apprenticeship, agency work |
| Paga | Pay, payslip (with checklist), severance pay (TFR) |
| Orario e ferie | Working hours (with weekly check), overtime, rest and night work, holidays |
| Salute e famiglia | Sick leave, law 104, maternity, paternity, parental leave, remote work, free time |
| Dignità e tutele | Interviews, monitoring, disciplinary procedure, duties and transfers, safety, stress, discrimination, harassment, whistleblowing, workplace culture |
| Fine del rapporto | Resignation, dismissal, final entitlements |
| Sindacato | Union rights, strikes |
| Aiuto | Where to get help, deadline calculator, glossary, sources |

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
- The content is general information, not legal advice. It may contain errors or be out of date; each page shows the date of the last review. Errors can be reported through [GitHub Issues](https://github.com/AmbrosinoFabio/diritti-al-lavoro/issues).
- No cookies, trackers or third-party requests. The payslip checklist is saved in the visitor's browser only (localStorage). The site is hosted on GitHub Pages, which logs visitors' IP addresses for security purposes.

