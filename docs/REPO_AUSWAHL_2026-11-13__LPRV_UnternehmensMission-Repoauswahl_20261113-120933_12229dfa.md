# UnternehmensMission: erweiterte Repository-Auswahl

Stand: 13.11.2026. Ziel: DonDomes/Lyra-UnternehmensMission, Branch main.
Ausgangspunkt: Commit 0a95622f563217b1170b0f90b21d2d4203100a20.

## Ergebnis und Umfang

Alle 16 im verbundenen GitHub-Konto sichtbaren Repositories sind in der Auswahlmatrix berücksichtigt. Das ist eine dokumentationsbasierte Eignungssichtung mit gezielten Quellcode-Lesungen, KEIN vollständiger rekursiver Code-, Sicherheits- oder Laufzeitaudit.

In diesem Ergänzungslauf wurden die zuvor nicht vertieft behandelten Repositories dms, Lyra-Local-2026-, Lyra-Bridge, Lyra-Bio, lyra-core, Geld, lyra-skills und Berlin betrachtet. dvbs-hp wurde erneut gelesen; beim Virtuellen Dozenten wurde die Integrationsbeschreibung vertieft. Die bereits gesichteten Lernrepositories bleiben einbezogen. Ihr bestehender Einsatz ist im ReWe1-Fachkonzept dokumentiert.

**Ausgeführt:** Quellen sichten, Eignung und Grenzen unterscheiden, Erweiterungskandidaten dokumentieren.
**Nicht ausgeführt:** neue Spielfunktionen einbauen, Fremdcode in die HTML kopieren, Server anbinden, andere Repositories ändern oder ein neues Spielrelease freigeben.

Die verteilten ReWe1- und ReWe5-HTMLs bleiben bei diesem Dokumentationslauf unverändert. Historische Testaussagen werden nicht als in diesem Lauf wiederholte Tests ausgegeben.

## Auswahlmatrix: 16 von 16 sichtbaren Repositories

| Repository | Herangezogene Grundlage | Nutzen für die Mission | Entscheidung |
| --- | --- | --- | --- |
| Lyra-UnternehmensMission | Aktuelle README, Fachkonzept, Build-Skript und Git-Baum | Bestehender Spielkern, Quelldaten, Tests und Releases | Zielprojekt; kein zweiter Spielkern nötig |
| Lyra-Quiz | Vorherige Sichtung: README, Lyra-OS-Design, Template; bestehendes Missions-Fachkonzept | Bedienruhe, Tastaturfokus, kontrastreiche Felder, Bewertungsprüfung | Vorhandene Referenz beibehalten, nicht blind ersetzen |
| Rewe1 | Vorherige Repo-/Drive-Sichtung; aktuelles Missions-Fachkonzept | Fachstoff, SKR04, aktuelle Modulstruktur | Inhaltliche Basis; aktuelle Drive-Master vor historischer Repo-Doku |
| Rewe5 | Vorherige Sichtung und archiviertes ProServa-Spiel | Story-/Szenenmechanik, Grafikmodi, Auswertung | Spielprinzipien nutzen, Fachfragen getrennt halten |
| lyra-campus | Vorherige Sichtung: Native Protocol v1; Missions-Fachkonzept | Optionaler Ergebnis-/Resume-Anschluss | Separates späteres Integrationspaket, keine Offline-Pflicht |
| duo-training-simulator | Vorherige Sichtung: README und DUO-Fachreferenz | Beleg, Bank, OPOS und nachvollziehbare Statuswechsel | Produktneutrale Prozessideen; kein PHP-/SQL-Backend importieren |
| Virtueller-Dozent | INTEGRATION_CAMPUS.md, Zeilen 1-200 | Dokumentiert lokale BM25-Kurssuche, Navigation, TTS und quellengebundene Antworten | Suchbare Lernhilfe als Kandidat; keine fertige Engineübernahme nachgewiesen |
| dvbs-hp | README erneut gelesen | DVBS-Markenauftritt und Asset-Herkunft | Gestaltungsvorbild; Logo-Bytes vor Einbettung gesondert beschaffen/prüfen |
| dms | README und INDEX.md | Originalbelege, Metadatenrevisionen, Integrität und Dokumentverlauf | Didaktische Belegakte als Kandidat; keine behauptete Revisionssicherheit |
| lyra-skills | README und scripts/verify_source_bundle.py | Hash-/Versions-/Identitätsprüfungen, Dublettenerkennung und sichere Archivpfade | Qualitätsprinzipien für Spielreleases und Importtests adaptieren, keine Skills im Browser ausführen |
| Lyra-Local-2026- | README | Verständliche Bedienung, getrennte Daten-/Berechtigungszustände, kontrollierte Aktionen | UX-/Sicherheitsvorbild; kein Windows-/Ollama-/Autogrow-Anschluss |
| Lyra-Bridge | README | Explizite Aktivierung, sichtbarer Status, manueller Ersatzweg bei fehlender Fähigkeit | Bedienprinzip nutzen; Android-Wakeword-Service nicht portieren |
| lyra-core | README | Trennung von Zuständen, Nutzerkontext, Wiederherstellung und Fehlergrenzen | Nur technische Grundprinzipien; Core bleibt unverändert und ohne Laufzeitkopplung |
| Geld | README, nur Produkt-/Architekturüberblick | Strukturierte Gesprächsaufnahme, Rückfragen, keine unbelegten Zusagen | Optionales Gesprächsmuster für fiktive Kundenfälle; keine Telefonie oder Geschäftsdaten |
| Berlin | Nur README; keine Firmenakten oder Ledger-Inhalte | Quellenbezug, getrennte Fälle, Fortschritt aus belegten Arbeitsschritten | Allgemeines Dokumentationsprinzip; keine Mandatsdaten im Spiel |
| Lyra-Bio | README und vollständiger Git-Baum | Sichtbarer Baum enthält README, Mailrichtlinie und Snapshot, keinen Spielbaustein | Kein direkter Codekandidat identifiziert; private Kontinuität nicht ins Spiel kopieren |

## Priorisierte Erweiterungskandidaten

Die folgenden Punkte sind **eigene Ableitungen aus der Sichtung**, keine Aussage, dass die Quellrepositories bereits genau diese Spielfunktion liefern. Alle stehen auf KANDIDAT / NICHT IMPLEMENTIERT.

### P1: Spielstand und Release besser absichern

Vorbild: lyra-skills-Verifier, ergänzt um Zustands-/Datentrennung aus Local und Core.

Vor einer Erweiterung vorhandene Importprüfungen des Spiels charakterisieren, nicht doppelt bauen. Gezielt testen: falsche Mission, falsche Inhaltsversion, unbekannte Aufgaben-IDs, doppelte Einträge, unzulässige Datentypen, nicht endliche Zahlen und zu große Eingaben. Fehlerhafte Imports dürfen den bisherigen Stand nicht ersetzen. Punkte aus Antworten ableiten, nicht aus einem importierten Gesamtpunktwert übernehmen. Ein Hash beweist Byteintegrität, nicht fachliche Richtigkeit oder Manipulationssicherheit.

Abnahme: gültiger Export wiederherstellbar; alle Negativfälle abgewiesen; alter Spielstand bleibt erhalten. Gebautes HTML gegen Release-Manifest prüfen. Keine ZIP-Funktion nur wegen des Quell-Verifiers hinzufügen: Ziel bleibt eine HTML.

### P2: Quellengebundene, durchsuchbare Lernhilfe

Vorbild: dokumentierte lokale Kurssuche des Virtuellen Dozenten.

Kleine Suche in eigens freigegebenen Begriffs- und Formeltexten, ohne KI-Server und ohne vollständige Originalskripte öffentlich einzubetten. Zuerst einfache Suche prüfen; BM25 nur verwenden, wenn Trefferqualität und Datenumfang es rechtfertigen. Die aktuell gelesene Integrationsdokumentation ist keine Verifikation eines wiederverwendbaren Gamma-Codepakets.

Abnahme: Treffer zeigen Quelle/Thema; fehlende Antwort wird offen angezeigt. Vor Abschluss weder Musterlösungen noch Rechenwerte der konkreten Aufgabe durch Suchtreffer, Dateinamen oder Vorschautexte verraten. Nach Abschluss dürfen Erklärungen und Lösungen durchsucht werden.

### P3: Nachvollziehbare Belegakte

Vorbild: DMS-Revisionen sowie die Beleg-/Bank-/OPOS-Prozesse des DUO-Simulators.

Bestehende Arbeitsmappe erweitern statt einen zweiten Posteingang bauen. Nur fiktive Belege: Originaldarstellung, eigene Bearbeitungsnotiz, Verknüpfung und lokale Korrekturhistorie trennen. Bei unklarer Rechnungsrichtung keine Gegenpartei erfinden. Wirtschaftliche Bearbeitungszustände nicht als versteckte Richtig/Falsch-Ampeln verwenden.

Abnahme: Original bleibt erhalten; Korrekturen sind nachvollziehbar; derselbe Zahlungseingang wird nicht doppelt verarbeitet. Keine Kennzeichnung als echtes revisionssicheres Archiv oder DATEV-Originalanwendung.

### P4: Einheitliche Marke und robuste Bedienung

Vorbilder: dvbs-hp, Lyra-Quiz, Lyra-Local und Lyra-Bridge.

DVBS-Logo erst nach Prüfung der tatsächlichen Datei lokal einbetten. Fremde Partnerlogos nicht ungeprüft übernehmen. Cartoon/2,5D/Adventure behalten dieselben Schaltflächen, Navigation und Bewertung. Optionales Vorlesen bleibt abschaltbar und darf den Spielstart nicht blockieren. Aus den Quellen folgt keine garantierte vollständige Offline-Spracherkennung; deshalb kein Mikrofon-/Wakeword-Ausbau in dieser HTML.

Abnahme: Tastaturbedienung, Kontrast, schmale Ansichten und ohne Sprache bedienbarer Vollablauf; kein externer Netzabruf zum Laden von Logo, Schrift oder Pflichtfunktion.

### P5: Fiktive Kundengespräche mit gezielten Rückfragen

Vorbild: dokumentierte Aufnahme-/Bestätigungsprinzipien aus Geld.

Beispielhafte neue Spielidee: Ein Kunde behauptet, eine Rechnung bezahlt zu haben. Der Spieler klärt Belegnummer, Betrag und Zahlungsdatum und prüft die Zuordnung. Keine reale Telefonie, keine KI-Kosten und keine Übernahme echter Namen, Rufnummern oder Kundenvorgänge. Bereits vorhandene Dialogmechanik bevorzugen.

Abnahme: alle nötigen Informationen sind erreichbar; keine Sackgasse; keine Lösungsbewertung vor dem Spielende. Neue Fachfälle müssen gegen ReWe1-Master und eigene Sollantworten geprüft werden.

## Kritische Grenzen

- Einzige Standalone-HTML, identische Inhalte/Bedienung in allen Grafikmodi, SKR04 und DATEV-only in Modul 09 bleiben unverändert.
- Allgemeine Lernhilfe ist nicht gleich Lösungsfreigabe. Suche, Gespräche, Erfolge und Statusanzeigen dürfen die Endauswertung nicht vorwegnehmen.
- Die vorhandene Mission nutzt teilweise voneinander unabhängige Modellfälle. Ein durchgängig abgestimmtes Jahresbuchhaltungsmodell ist damit noch nicht belegt und wird durch eine Belegakte nicht automatisch hergestellt.
- Das Zielrepo ist öffentlich. Keine privaten Quellcode-Dumps, Originalrechnungen, Personen-/Unternehmensakten, Zugangsdaten oder privaten Kontinuitätsaufzeichnungen veröffentlichen. Dieser Bericht enthält nur abstrakte technische Zuordnungen und Quellenzeiger.
- README-Status ist ein Bericht des jeweiligen Projekts, kein neuer Laufzeitnachweis. Weder Server-/KI-Funktionen noch Zertifizierungen werden aus Beschreibungen abgeleitet.
- Kein Ausbau nur um des Ausbaus willen: bestehende Funktionen zuerst prüfen, dann die kleinste passende Ergänzung. Echte HTML-Dateistart-/Resume-/Drucktests bleiben wichtiger als zusätzliche Dekoration.

## Quellen und nachvollziehbarer Lesestand

Die folgenden Git-Blob-SHAs bezeichnen die tatsächlich gelesenen Dateifassungen, nicht Releasefreigaben. Verweise auf private Repositories bleiben für nicht berechtigte Leser unzugänglich.

| Quelle | Pfad | gelesener Blob |
| --- | --- | --- |
| [dms](https://github.com/DonDomes/dms) | README.md | 4bc186f00c4a4fef379c8ac49de4658a75c5f5ad |
| dms | INDEX.md | 34cb37ec4556fb439349c0750c2c9ec4528983dd |
| [Lyra-Local-2026-](https://github.com/DonDomes/Lyra-Local-2026-) | README.md | 98a41a94e80244a660df77e8b46b218c958c6e91 |
| [Lyra-Bridge](https://github.com/DonDomes/Lyra-Bridge) | README.md | b65792a36ea008f5483f7c4d78ff0d94944be4e1 |
| [Lyra-Bio](https://github.com/DonDomes/Lyra-Bio) | README.md | 8f2a44fe125afad895d7f6626316e3fc1e0ea0fb |
| [lyra-core](https://github.com/DonDomes/lyra-core) | README.md | 0ea3678c5ab52e5845a605475711e6b1d0e89e30 |
| [Geld](https://github.com/DonDomes/Geld) | README.md | b17a5c912a17732bca62b211fbd9f5203804ea7f |
| [lyra-skills](https://github.com/DonDomes/lyra-skills) | README.md | 339c3405e89a5e225472ba8b8b580f6025b4abb4 |
| lyra-skills | scripts/verify_source_bundle.py | a22699f6607ee05678b48943244f1716abd1e191 |
| [Berlin](https://github.com/DonDomes/Berlin) | README.md | 90a54484bb5540e375674d456b0204df9ded332c |
| [dvbs-hp](https://github.com/DonDomes/dvbs-hp) | README.md | b10517fd815c578d1684095700b9f2dd5a8288e3 |
| [Virtueller-Dozent](https://github.com/DonDomes/Virtueller-Dozent) | INTEGRATION_CAMPUS.md, Zeilen 1-200 | afedf8caaaefada1c9b79603a2ad59e5f612fe5d |
| Lyra-UnternehmensMission | README.md | 5b18d33a8d45e2529dc7faa06043fac1dc063916 |
| Lyra-UnternehmensMission | docs/REWE1_MISSION_2026-11-13.md | d57f3f105ae103f906f58891c07208e9d3f7f978 |
| Lyra-UnternehmensMission | scripts/build.py | bcbd31ae53933a6ed1c84fb98b7eb50f6a455846 |

Lyra-Bio: vollständiger Git-Baum bei 44ff6eabff23385e8e79278dcfdba7e5d611ace1, truncated=false; Snapshotinhalt bewusst nicht gelesen. UnternehmensMission: Baum des oben genannten Ausgangscommits, truncated=false. Ein versuchter DMS-Pfad src war nicht vorhanden; daraus wird keine Aussage über das gesamte DMS-Codeangebot abgeleitet.

## Freigabestatus dieses Berichts

Dokumentations-/Eignungsreview, Gegenprüfung SAME_MODEL; keine unabhängige Fach- oder Codefreigabe. Quellenbehauptungen, eigene Ableitungen und offene Umsetzungen sind getrennt. Nur dieser Bericht, sein Herkunftsnachweis und der README-Verweis werden hinzugefügt. Kein neues HTML-Release und keine Laufzeitprüfung in diesem Ergänzungslauf.
