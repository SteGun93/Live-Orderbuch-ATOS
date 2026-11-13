---
name: atos-orderbuch-release
description: Ein Release von Live-Orderbuch ATOS nach dem vorhandenen Projektablauf vorbereiten oder konkret freigegeben durchführen. Kein Publishing aus einem normalen Änderungs- oder Draft-PR-Auftrag ableiten.
---

# Live-Orderbuch ATOS-Release vorbereiten

1. „Befugnisse und Release“ in `CONTRIBUTING.md` und die dort genannten Primärdateien lesen. Ziel, Version, Commit und vorhandenen Veröffentlichungsweg feststellen. Fehlt ein eingerichteter Weg, nicht selbst einen erfinden.
2. Bestehende konkrete Freigaben berücksichtigen. Ohne Publishing-Auftrag nur den prüfbaren Vorschlag vorbereiten; Tags, Deployments und andere Veröffentlichungsnebenwirkungen nicht auslösen.
3. Versionsstellen und betroffene Prüfungen nach `atos-orderbuch-checks` abgleichen. Projektblocker, Hardware-/Datenbankgrenzen und rechtliche/betriebliche Voraussetzungen aus den Projektquellen als offen behandeln, solange sie nicht nachgewiesen sind. Keine Version allein für eine Agentenregeländerung erhöhen.
4. Vor Veröffentlichung Version und Commit, Artefakte soweit vorgesehen, Ergebnisse, Rückweg und offene Punkte zur Entscheidung vorlegen. Vorhandene Freigaben nicht wiederholt erfragen; bei geänderter Zielversion oder erweitertem Umfang neu abstimmen.
5. Nur im konkret beauftragten Umfang den vorhandenen Ablauf ausführen. Keine Geheimnisse, Signierschlüssel, Konten, Rechte oder Schutzregeln als Nebenarbeit ändern.
6. Veröffentlichten Stand verifizieren. Bei Fehlschlag erst feststellen, was bereits angewendet/veröffentlicht wurde. Keine blinde Wiederholung von Tags, Uploads oder Migrationen; unklare Teilzustände mit nächstem notwendigen Schritt zurückmelden.
