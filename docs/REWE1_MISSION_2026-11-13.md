# ReWe1-UnternehmensMission – Fachkonzept, Quellen und Nachweise

**Stand: 13.11.2026**  
**Repo:** `DonDomes/Lyra-UnternehmensMission`  
**Aktiver Build:** `dist/LYRA_UnternehmensMission_ReWe1_BueroWerk_SKR04_2026_v1.html`  
**Rechts-/Lehrkontext:** ReWe1 2026, ausschließlich SKR04, Modul 09 ausschließlich DATEV

## Produkt

Eigenständige Offline-HTML für individuelles Üben und die abschließende fachliche Besprechung. Die 90–120 Minuten sind ein **Planungsziel** und noch nicht an einer Lerngruppe gemessen. Die neun Kapitel behandeln eine fiktive Firma `BüroWerk e.K.`; Beträge, Personen und Geschäftsfälle sind ausdrücklich simulierte Unterrichtsannahmen. Manche Kapitel verwenden unabhängige Fallrechnungen, keine durchgängig abgestimmte einheitliche Jahresbuchhaltung.

| Modul | Kompetenz | Narrativer Schwerpunkt |
| --- | --- | --- |
| 01 | Aufgaben RW, FiBu/KLR, GoB, Belegprinzip | Eingangspost und Belegdetektiv |
| 02 | Inventur, Inventar, Bilanz, Eigenkapital | Nacht im Lager |
| 03 | Soll/Haben, Aktiv/Passiv, EBK/SBK | Die Spur von Soll und Haben |
| 04 | Aufwand/Ertrag/GuV, Privat, FE/UE | Das verschwundene Ergebnis |
| 05 | Anlagen, lineare AfA, GWG, Investition | Die Maschine mit dem Preisschild |
| 06 | Debitoren, Kreditoren, OPOS, Skonto | Der Fall der offenen Rechnungen |
| 07 | Netto/Brutto, USt/VSt, Zahllast | Der Steuerprüfer im Postfach |
| 08 | ARAP/PRAP, Rückstellungen, Durchschnittsbewertung | Die Nacht vor dem Abschluss |
| 09 | DATEV-orientierte Beleg-/Buchungszeile, Automatik, OPOS | Der letzte Buchungsstapel |

Pro Kapitel acht interaktive Aufgaben = **72 Schritte** mit **352 möglichen Fachpunkten**, Aufgabenvarianten `inspect`, `dialogue`, `match`, `order`, `single`, `multi`, `numbers`, `reflect`, `portfolio`. Lesen, eigene Begründungen und Gesprächswahl werden nicht künstlich fachlich benotet. Bewertung enthält Teilpunkte und **keine Minuspunkte**. Die vollständigen Lösungen werden erst nach bestätigter Abgabe sichtbar. Da die einzelne HTML die Antworten im Quellcode enthält, ist sie für **keine manipulationssichere Prüfung** geeignet.

Visuell drei SVG-Stile (Cartoon, illustrativer 2,5D-Look, Adventure), gleiche Inhalte und Bedienung. Acht Charaktervorlagen mit optionaler Individualisierung, Arbeitsmappe, Taschenrechner, allgemeine Formelsammlung, JSON-Export/-Import und Druckbericht. Ohne Backend/CDN oder externe Fonts.

## Primärquellen in Google Drive

Verbindliche Unterrichtsquelle: `Meine Ablage/Arbeit/ReWe1_2026_Aktualisiert`. In den Fachthemen als aktuelle, separat gespeicherte Master-Skripte vorhanden:

- `ReWe1_01_Master_Einfuehrung_Rechnungswesen_SKR04_2026.pdf`
- `ReWe1_02_Master_Inventur_Inventar_Bilanz_SKR04_2026.pdf`
- `ReWe1_03_Master_Bestandskonten_EBK_SBK_SKR04_2026.pdf`
- `ReWe1_04_Master_Erfolgskonten_GuV_Privat_SKR04_2026.pdf`
- `ReWe1_05_Master_Abschreibung_GWG_Anlagevermoegen_SKR04_2026.pdf`
- `ReWe1_06_Master_Forderungen_Verbindlichkeiten_Personenkonten_SKR04_2026.pdf`
- `ReWe1_07_Master_Umsatzsteuer_Vorsteuer_SKR04_2026.pdf`
- `ReWe1_08_Master_Abgrenzung_Rueckstellungen_Bewertung_SKR04_2026.pdf`
- `ReWe1_09_Master_DATEV_Praxis_SKR04_2026.pdf`

`MASTER_Status_ReWe1_2026` und `MASTER_Regeln_ReWe1_2026` (Stand 12.11.2026) gehen vor veraltete README-Angaben in anderen Repositories. Es wurden keine originalen Drive-Unterrichtsdateien geändert und keine älteren Unterrichtsreihen samt Markennamen veröffentlicht. Der Aufbau nimmt ihre Fachbegriffe und Modulzuordnungen auf und konstruiert **neue, explizite Modellfälle**.

## Wiederverwendete Ideen aus Repos

| Repository | Was verwendet wurde | Was **nicht** übernommen wurde |
| --- | --- | --- |
| `Lyra-Quiz` | V7.1-Prinzipien: ruhige Bedienung, Tastaturfokus, Teilpunkte, Lernhilfen, Antworten erst am Schluss | Kein blindes Einbetten der vollständigen Quiz-/V6.1-Engine; andere Darstellung wegen Adventure |
| `Rewe1` | SKR04-Fachsystem, didaktische Themenmatrix, QA-Fehlerbilder | Kein Kopieren historischer Quiz-Antwortschlüssel ohne eigene Fallprüfung |
| `Rewe5` | Vorhandene selbstständige Offline-Spiel-Engine, SVG-Szenen/Avatar, Persistenz-/Review-/Druckmechanik | **Keine** ReWe5-Fragen oder Controlling-Aufgaben, keine Vermischung der Fachbereiche |
| `lyra-campus` | Dokumentiertes `lyra-quiz-campus-v1` als mögliche spätere Integrationsoption | **Keine** Protokoll-Deklaration ohne tatsächlich getestete State-/Restore-/Result-Kompatibilität |
| `duo-training-simulator` | Strukturideen Beleg, Bank, Zuordnung, Status | Kein PHP/MariaDB, kein DUO-Buchungsfeld, keine Drittanbieter-UI-Kopie |
| `Virtueller-Dozent` | spätere eigenständige Option für Sprachausgabe/Dialog | Keine KI-, Netzwerk- oder Modellpflicht im Offline-Spiel |

## Technischer Aufbau & Rekonstruktion

```text
src/rewe1-mission.json       9 Kapitel + 72 Aufgaben, Lösungen und Quellzuordnung
src/mission-template.html   kompletter HTML-/CSS-/SVG-/JS-Spielkern mit Daten-Platzhalter
scripts/build.py            deterministische Zusammenführung in eine HTML
 dist/LYRA_..._v1.html      fertige HTML zur Weitergabe an Lernende
 tests/test_core.cjs        deterministische Node-Bewertungsprüfung
 tests/test_browser_inline.py Browser-Abnahme im eingeschränkten Testkontext
 manifest.json             Versions- und Quellübersicht mit SHA-256
```

Rekonstruktion: `python3 scripts/build.py` (nur Python-Standardbibliothek), danach `node tests/test_core.cjs`. Für Browser-Test zusätzlich `python3` mit `playwright` und lokal verfügbarem Chromium. `dist/` ist **das** Nutzerartefakt, keine weiteren Dateien zum Spielstart notwendig.

## QA-Nachweis und Grenzen

- `src/rewe1-mission.json`: neun Kapitel, 72 eindeutige IDs, neun definierte Fragetypen; 352 Maximalpunkte aus Einzelaufgaben.
- `tests/test_core.cjs`: Referenzlösungen und alle 72 Schritte bis Abschluss; Review 352/352; Restore-Akzeptanz und Versions-/ID-Ablehnung; 39 Teilpunkte-Beispiele; Deutsches Zahlenformat/invalid inputs und Taschenrechner-Validierung. **Bestanden** am 13.11.2026.
- `tests/test_browser_inline.py`: Playwright Chromium, HTML direkt als DOM-Inhalt eingebracht; vollständig alle 72 Aufgaben bearbeitet, drei Themenmodi gewechselt, Endfreigabe und detaillierte Ergebnis-DOMs geprüft, Desktop und schmaler Viewport, ohne JavaScript-Ausnahmen. **Bestanden** am 13.11.2026 für diesen eingeschränkten Modus.
- **Offen:** vollständiger `file://`-Start und HTTP-Start im realen Browser waren im Testcontainer wegen `net::ERR_BLOCKED_BY_ADMINISTRATOR` nicht möglich; daher echter Dateistart, dauerhafter Speicher nach Browserneustart, echte mobile Touch-Bedienung, Druck/PDF auf dem Nutzergerät und Lyra-Campus-Import bleiben gesondert zu prüfen. Die JS/DOM-Abnahme beweist diese Punkte nicht.
- **Fach-QA-Grenze:** Die aktuellen Master-PDFs wurden inhaltlich gelesen und Modellbeispiele abgestimmt. Kein unabhängiges neues vollständiges DATEV-Programmversionsaudit und keine Lehrgruppen-Pilotdauer. Konkrete DATEV-Maske ist eine eigene Schulungsdarstellung.

## Fortsetzung

Die Quell-JSON und die Engine-Vorlage sind die pflegbaren Primärdateien. Änderungen erst daran und dann mit Tests + neuem SHA-256 ein HTML bauen. Weder Quelldaten noch ältere Release-Dateien still überschreiben. Für neue Missionen einen separaten Themenzweig oder neue Versionsdatei verwenden. Keine produktiven Systeme, ReWe1-Unterrichtsordner oder andere Repositories aus dieser Mission heraus ändern.
