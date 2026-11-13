# LYRA – UnternehmensMission

## Verfügbare Offline-Spiele

| Fachbereich | Einzeldatei | Status |
| --- | --- | --- |
| **ReWe1 · SKR04 · Module 01–09** | [BüroWerk – 72 Schritte, 9 Kapitel](dist/LYRA_UnternehmensMission_ReWe1_BueroWerk_SKR04_2026_v1.html) | HTML gebaut; Kern- und DOM-Browsertests bestanden; echter lokaler Dateistart auf Endgeräten offen |
| **ReWe5 · Controlling · Tag 01–13** | [ProServa – archivierte Original-HTML](archive/ReWe5/LYRA_UnternehmensMission_ProServa_Tag01-13_v1__LPRV_ReWe5-UnternehmensMission_20261111-102301_0e8e4c4f.html) | Vorhandenes ursprüngliches Artefakt unverändert im Repo gesichert; keine neue ReWe5-Fachfreigabe in diesem Lauf |

**ReWe1-Umfang:** eine vollständig offlinefähige HTML-Datei; 72 Schritte, 352 mögliche Fachpunkte, Teilpunkte ohne Minuspunkte, neun Kapitel, drei rein optische Grafikmodi, Charaktereditor und JSON-Spielstand. Vollständige Musterlösungen erst nach bestätigtem Abschluss. Die geplante Spielzeit beträgt ca. 90–120 Minuten und ist noch nicht in einer Lerngruppe gemessen.

### Reproduzierbare ReWe1-Entwicklung

```bash
python3 scripts/build.py
node tests/test_core.cjs
# optional: python3 tests/test_browser_inline.py  (Playwright/Chromium benötigt)
```

- [Fachkonzept, Quellen, Wiederverwendung und QA-Grenzen](docs/REWE1_MISSION_2026-11-13.md)
- [Unterrichts-/Endgeräte-Testanleitung](docs/TESTANLEITUNG.md)
- [Szenen, Aufgaben, Lösungsschlüssel](src/rewe1-mission.json)
- [Spielvorlage mit Engine und SVG](src/mission-template.html)
- [Reproduzierbarer Generator](scripts/build.py)
- [Erstellungs-/Prüfmanifest](manifest.json)

**ReWe1-Build-SHA-256:** `f7f27076e2d4f9e01d767651cfc3961e6c77802a58042e738cb88c27b4ae684f`. Die vollständige HTML wurde über GitHub erstellt und anschließend mit den übertragenen Bytes abgeglichen. Der ReWe5-Altbuild wurde ebenfalls bytegenau übernommen. Beide bilden eigenständige Releases; ein ReWe1-Build überschreibt nicht ReWe5.

---


Zentrales Repository für die **LYRA-UnternehmensMission** als eigenständige, offlinefähige HTML-Lernabenteuer. Projektbereiche werden fachlich getrennt gehalten: **ReWe1 (Buchführung, SKR04)** und **ReWe5 (Controlling)**.

## Verbindliche ReWe1-Entscheidungen (13.11.2026)

- Zielgruppe: Teilnehmer im Kurs ReWe1; große **spielerische Wiederholung** nach den Kernmodulen, nicht Ersatz für sämtliche Unterrichtsstunden.
- Ausgangsmaterial: `Google Drive / Meine Ablage / Arbeit / ReWe1_2026_Aktualisiert` (Ordner-ID `1mpiAqpv7qKVUZGXm8rdObLg4G4d3t3pm`), maßgeblich die aktuellen neun Master-Skripte sowie Übungen und Lösungen.
- Inhalte: (01) Grundlagen/GoB, (02) Inventur–Inventar–Bilanz, (03) Bestandskonten/EBK/SBK, (04) Erfolgskonten/GuV/Privat, (05) AfA/GWG, (06) Forderungen/Verbindlichkeiten/OPOS, (07) USt/VSt, (08) Abgrenzung/Rückstellungen/Bewertung, (09) **ausschließlich DATEV-Praxis**.
- **SKR04**, keine Lexware- oder IKR-Bestandteile im aktiven ReWe1-Spiel.
- Ziel: ca. **90–120 Minuten** Einzelspiel mit neuen Fallhandlungen, Belegprüfung, Buchungssätzen, Zuordnung, Rechnungen und begründeten Entscheidungen.
- Ein **einziges offline nutzbares HTML** als verteilbares Spiel, ohne Backend, CDN oder externe Abhängigkeiten.
- Eine Bedienung und identische Inhalte in drei rein optischen Modi (**Cartoon**, **2,5D-Look**, **Adventure**), persönliche Spielfigur, sichere Spielstand-Sicherung/Import.
- **Keine Lösungen oder Richtig/Falsch-Hinweise während des Spiels**; fachliche Erklärungen, Teilpunkte und Auswertung erst nach bestätigtem Abschluss. Keine Schulnote, keine Minuspunkte.
- Eigenständige Schulungsoberfläche mit DVBS-Branding; **keine 1:1-Kopie der DATEV-Oberfläche**, kein Drittanbieterlogo, keine echte DATEV-Verbindung.
- Jede Datei wird vor einer Freigabe mit Inhalts-, Syntax-, Bewertungs- und Browsertests geprüft; ausdrücklich benannte QA-Grenzen bleiben offen.

## Repositories als Referenz

**Erweiterte Sichtung vom 13.11.2026:** [Auswahlmatrix für alle 16 sichtbaren Repositories und priorisierte Ausbaukandidaten](docs/REPO_AUSWAHL_2026-11-13__LPRV_UnternehmensMission-Repoauswahl_20261113-120933_12229dfa.md). Zusätzlich berücksichtigt: DMS, DVBS-Homepage, Local/Bridge/Core, Skills, Geld, Berlin und Bio. Quellenbefunde und eigene Erweiterungsideen sind getrennt dokumentiert.

**Status:** Dokumentation ergänzt; diese Sichtung ändert die ausgelieferten HTMLs nicht. Suchbare Lernhilfe, Belegakte und zusätzliche Integritätsprüfungen sind Kandidaten, keine bereits eingebauten Funktionen.

- [Lyra-Quiz](https://github.com/DonDomes/Lyra-Quiz): UI-/Teilbewertungs-/Qualitätsprinzipien aus V7.1, keine unverifizierte 1:1-Engineübernahme.
- [Rewe1](https://github.com/DonDomes/Rewe1): Projektregelwerk, SKR04 und Kursstruktur; aktueller Drive-MASTER_Status 12.11.2026 hat Vorrang vor der älteren Repo-README.
- [Rewe5](https://github.com/DonDomes/Rewe5): Spiel-/Rollenspielkonzepte, als getrennte Fachrichtung.
- [lyra-campus](https://github.com/DonDomes/lyra-campus): Native-Protokoll nur bei tatsächlicher Implementierung seiner Funktionen deklarieren.
- [duo-training-simulator](https://github.com/DonDomes/duo-training-simulator): Beleg-/OPOS-Prozessideen, **nicht** den PHP-/SQL-Backendcode als Offline-Abhängigkeit kopieren.
- [Virtueller-Dozent](https://github.com/DonDomes/Virtueller-Dozent): optionaler späterer Sprach-/Dialoganschluss, kein Pflichtbestandteil.

## Architektur & Fortschritt

Die Entwicklung verwendet einen getrennten, validierbaren Fragen-/Szenendatensatz und einen gemeinsamen Spielkern. Aus den Quellen wird ein **einzelnes Standalone-HTML** gebaut. Quellfassungen, Tests, Prüfnachweise und datierte Entscheidungen werden im Repository versioniert; nichts aus anderen Repositories wird überschrieben.

**Stand:** ReWe1 v1 im Repository gespeichert und als reproduzierbarer Stand getestet. Originales ReWe5-HTML als eigenständiger Archivstand erhalten. Der echte Endgeräte-Check des heruntergeladenen HTMLs bleibt offen.

> Hinweis: Eine im HTML enthaltene Lösungstabelle ist durch den Ablauf verdeckt, aber in einer Offline-Datei nicht kryptographisch geheim. Die Mission ist ein Lernspiel und keine manipulationssichere Prüfung.
