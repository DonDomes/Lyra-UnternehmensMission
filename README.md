# LYRA – UnternehmensMission

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

- [Lyra-Quiz](https://github.com/DonDomes/Lyra-Quiz): UI-/Teilbewertungs-/Qualitätsprinzipien aus V7.1, keine unverifizierte 1:1-Engineübernahme.
- [Rewe1](https://github.com/DonDomes/Rewe1): Projektregelwerk, SKR04 und Kursstruktur; aktueller Drive-MASTER_Status 12.11.2026 hat Vorrang vor der älteren Repo-README.
- [Rewe5](https://github.com/DonDomes/Rewe5): Spiel-/Rollenspielkonzepte, als getrennte Fachrichtung.
- [lyra-campus](https://github.com/DonDomes/lyra-campus): Native-Protokoll nur bei tatsächlicher Implementierung seiner Funktionen deklarieren.
- [duo-training-simulator](https://github.com/DonDomes/duo-training-simulator): Beleg-/OPOS-Prozessideen, **nicht** den PHP-/SQL-Backendcode als Offline-Abhängigkeit kopieren.
- [Virtueller-Dozent](https://github.com/DonDomes/Virtueller-Dozent): optionaler späterer Sprach-/Dialoganschluss, kein Pflichtbestandteil.

## Architektur & Fortschritt

Die Entwicklung verwendet einen getrennten, validierbaren Fragen-/Szenendatensatz und einen gemeinsamen Spielkern. Aus den Quellen wird ein **einzelnes Standalone-HTML** gebaut. Quellfassungen, Tests, Prüfnachweise und datierte Entscheidungen werden im Repository versioniert; nichts aus anderen Repositories wird überschrieben.

**Stand:** Quellen- und Architekturaufnahme abgeschlossen. Dateien und Testergebnisse werden ausschließlich dann als implementiert/bestanden bezeichnet, wenn sie im Repository bzw. als Ausführung nachweisbar sind.

> Hinweis: Eine im HTML enthaltene Lösungstabelle ist durch den Ablauf verdeckt, aber in einer Offline-Datei nicht kryptographisch geheim. Die Mission ist ein Lernspiel und keine manipulationssichere Prüfung.
