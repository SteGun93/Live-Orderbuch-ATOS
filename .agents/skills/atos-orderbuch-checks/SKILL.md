---
name: atos-orderbuch-checks
description: Passende Prüfungen für Änderungen an Live-Orderbuch ATOS auswählen, ausführen und mit Grenzen berichten. Für Code, Konfiguration und Doku; kein Deployment.
---

# Live-Orderbuch ATOS prüfen

1. Im Repository-Stamm die Tabelle „Prüfungen“ in `CONTRIBUTING.md`, referenzierte Konfigurationen und vorhandene CI lesen. Nur existierende Befehle verwenden; Paketmanager, Laufzeit und Projektpfad vor dem Start prüfen.
2. Diff in betroffene Bereiche einordnen. Gezielte Prüfungen aus der Tabelle ausführen; bei gemeinsam genutztem Code die Aufrufer einbeziehen. Eine Textänderung braucht Quellen-/Verweisprüfung, keine künstlich hinzugefügten Laufzeittests.
3. Datenbanken, Hardware und Dienste ausschließlich isoliert und im beauftragten Umfang verwenden. Voraussetzungen prüfen, bevor ein Befehl Migrationen, Geräteaktionen, Dateiumbenennungen oder externe Verbindungen auslösen kann.
4. Skilldateien auf gültiges YAML mit `name` und `description`, klaren Auslöser, existierende Referenzen und echte Befugnisse prüfen; vorhandenen Skill-Validator nutzen, wenn verfügbar. Mit `git diff --check` die Textänderung prüfen. Kein Framework installieren, nur um diese Metadatenprüfung auszuführen.
5. Relevante CI-Checks des aktuellen PR-Kopfs verfolgen, falls eingerichtet. Bei Fehlern zwischen neuem Problem, fehlender Umgebung und bestehendem Fehler unterscheiden; keine Tests oder Schutzmechanismen für Grün abschwächen. Ohne eingerichtete CI das ausdrücklich berichten.
6. Stand, Befehle und Ergebnisse nennen. Ausgelassene oder wegen fehlender Voraussetzungen nicht aussagekräftige Prüfungen mit Grund ausweisen. Nur nach neuen Änderungen oder offenen Befunden breiter/wiederholt testen.
