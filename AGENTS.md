# Einstieg für Coding-Agenten

Flask-Anwendung mit WebSocket-Marktdaten, Python-Controllern und HTML-/JavaScript-Frontend.

Zuerst [CONTRIBUTING.md](CONTRIBUTING.md) und die zur Aufgabe passenden Quellen daraus lesen. Den betroffenen Code und seine Aufrufer prüfen; Widersprüche zur Dokumentation vor der Umsetzung benennen.

## Projektgrenzen

- Externe Login- und WebSocket-Verbindungen in Tests mocken; keine echten Zugangsdaten oder unkontrollierten Abfragen an den Datenanbieter verwenden.
- Marktdaten, Zeitstempel, Reihenfolge und Volumen unverfälscht verarbeiten; Anzeige und Datenabruf nicht um ungefragte Handelsfunktionen erweitern.
- Reconnect, Polling und konkurrierende Datenzugriffe bei Änderungen gemeinsam prüfen; Fehler dürfen keine aggressive Anfrageschleife auslösen.
- Keine laufende Compose-Instanz der Person stoppen: Compose nutzt feste Container-/Volume-Namen. Für Tests isolierte Namen, Ports und eigene Daten verwenden.
- Keine Geheimnisse oder produktiven Personen-/Gerätedaten in Tests, Logs, Screenshots oder PRs verwenden.
- Tests nicht abschwächen oder als bestanden melden, wenn sie nicht ausgeführt wurden.
- Nicht direkt auf `main` pushen. Ein Draft-PR-Auftrag gibt weder Merge noch Tags oder Veröffentlichung frei. Bereits konkret erteilte Freigaben gelten weiter.

## Skills

Die Skills liegen im Codex-Suchpfad `.agents/skills/`; andere Agenten lesen dieselben Dateien. Projektregeln stehen einmal in der Beitragsdokumentation und den dort genannten Fachquellen.

| Aufgabe | Skill |
| --- | --- |
| Änderung und Draft-PR | [atos-orderbuch-aenderung](.agents/skills/atos-orderbuch-aenderung/SKILL.md) |
| Prüfungen auswählen | [atos-orderbuch-checks](.agents/skills/atos-orderbuch-checks/SKILL.md) |
| Unabhängiges Review | [atos-orderbuch-review](.agents/skills/atos-orderbuch-review/SKILL.md) |
| Release vorbereiten | [atos-orderbuch-release](.agents/skills/atos-orderbuch-release/SKILL.md) |
