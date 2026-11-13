---
name: atos-orderbuch-aenderung
description: Eine Änderung an Live-Orderbuch ATOS umsetzen und als Draft-PR vorbereiten. Für Code, Fehlerkorrekturen und Projektregeln; führt keinen Merge oder Release aus.
---

# Live-Orderbuch ATOS ändern

1. Vom Repository-Stamm `AGENTS.md`, `CONTRIBUTING.md` und die zur Aufgabe passenden Fachquellen lesen. Auftrag und Akzeptanzkriterien festhalten; Produktfragen von bereits freigegebener Arbeit trennen.
2. Betroffene Einstiegspunkte, Aufrufer und Tests erkunden. Die Projektgrenzen aus AGENTS gegen den geplanten Ansatz prüfen; keine Version oder Architektur aus einem anderen Projekt übernehmen.
3. Den Branch nach „Branch und Pull Request“ in CONTRIBUTING wählen; bestehende Arbeit und offene PRs beachten.
4. Regression möglichst zunächst nachweisen, minimal umsetzen und betroffene Doku im selben PR pflegen. UI-Ausgangszustand vor der Bearbeitung mit Testdaten erfassen.
5. Nach `atos-orderbuch-checks` gezielt prüfen. Selbstprüfung gegen Auftrag und Diff; für unabhängige Prüfung `atos-orderbuch-review` verwenden. Noch fehlendes Review im Draft ausdrücklich offenlassen.
6. Im beauftragten Umfang committen, pushen und Draft-PR gegen den passenden Basisbranch erstellen. PR-Vorlage mit tatsächlichen Ergebnissen füllen; bei CLI-Nutzung mehrzeilige Beschreibung über `--body-file`. Nach jedem Push CI auf dem aktuellen Kopf prüfen, soweit eingerichtet, und Beschreibung bei geändertem Ergebnis nachziehen.
7. Link, Kopf-Commit, Prüfungen und offene Punkte zurückmelden. Ein Draft-Auftrag berechtigt nicht zu Merge oder Veröffentlichung.
