---
name: atos-orderbuch-review
description: Einen Live-Orderbuch ATOS-PR unabhängig auf Auftrag, Fehler, Regeln und Dokumentation prüfen. Belegte Code-, Sicherheits- und Konfigurationsbefunde; kein automatischer Merge.
---

# Live-Orderbuch ATOS unabhängig prüfen

`CONTRIBUTING.md` enthält die Reviewregeln und Projektquellen. Wer mitgeschrieben hat, führt nur eine Selbstprüfung aus und nutzt für Unabhängigkeit eine andere Person oder einen frischen Subagenten nach diesen Regeln.

1. Auftrag, Basis- und Kopf-Commit holen; kompletten Diff und betroffene Aufrufer lesen. In einem eigenen Checkout/Worktree arbeiten, keine produktiven Ressourcen nutzen.
2. Die vier Prüffragen und projektspezifischen Reviewprioritäten aus CONTRIBUTING durchgehen. Bestehende Daten/Schnittstellen und Fehlerfälle berücksichtigen. Dokumentation gegen tatsächlichen Code prüfen, geplante Funktionen nicht als vorhanden ausgeben.
3. Jeden Fehlerverdacht mit gezieltem Regressionstest oder reproduzierbarem Nachweis belegen. Bei Sicherheits-, Doku- und Konfigurationsbefunden genügen konkrete Stelle und überprüfbarer Gegenbeleg. Nicht testbare Vermutungen und Stilwünsche getrennt führen; grüne Tests auch gegen ihre Annahmen prüfen.
4. Geprüften Commit, Befunde mit Auswirkung und Nachweis, ausgeführte Prüfungen und Grenzen berichten, auch wenn kein Befund vorliegt. Sicherheitsdetails privat behandeln. Kommentare nur im beauftragten Umfang veröffentlichen.
5. Fixes nur nach Auftrag und abgestimmt auf gemeinsamen Branches. Danach den neuen Diff prüfen; vor einer Freigabe auf den aktuellen Stand beziehen. Bei offenen schweren Befunden oder Produktfragen zurückmelden. Kein Merge, Tag oder Release aus dem Reviewauftrag ableiten.
