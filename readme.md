# 📊 Live Orderbuch - ATOS

Dieses Projekt zeigt ein **Live-Orderbuch** und **Tick-Daten** für die ATOS-Aktie. Es nutzt **Websockets** zur Echtzeit-Datenübertragung und **Flask** als Backend, während das Frontend mit **HTML** umgesetzt ist.

---

## **Funktionen**

- 📈 **Live Orderbuch:**
  - Darstellung der **Bid- und Ask-Preise** mit zugehörigen **Shares** und **Orders**.
  - **Summenzeile** unter dem Orderbuch mit:
    - Gesamtzahl der **Shares** (Bid und Ask)
    - Gesamtzahl der **Orders** (Bid und Ask)
    - **Verhältnis** von Bid zu Ask als **Prozentbalken**

- 📊 **Tick-Daten:**
  - Zeigt die letzten 50 Trades an mit:
    - **Zeit**
    - **Preis**
    - **Volumen**

- 🚀 **Echtzeit-Updates**:
  - Automatische Aktualisierung der Daten alle 2 Sekunden.

---

## **Voraussetzungen**

- **Python 3.12** oder höher
- **Flask** für das Backend
- **Websockets** zur Echtzeit-Kommunikation

---

## **Installation**

1. **Repository klonen:**
   ```sh
   git clone https://github.com/SteGun93/Live-Orderbuch-ATOS.git
   cd Live-Orderbuch-ATOS
   ```

2. **Virtuelle Umgebung erstellen:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Für Linux/MacOS
   .\venv\Scripts\activate  # Für Windows
   ```

3. **Abhängigkeiten installieren:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Umgebungsvariablen einrichten:**
   Erstelle eine `.env`-Datei im Root-Verzeichnis, falls diese nicht existiert und füge folgende Zeile hinzu:
   ```
   DEBUG=True
   ```

---

## **Starten der Anwendung**

```sh
python main.py
```

- Die Anwendung ist unter **`http://localhost:5000`** erreichbar.

---

## **Projektstruktur**

```plaintext
Live-Orderbuch-ATOS/
│
├── controllers/
│   ├── websocket_controller.py      # WebSocket-Verbindung und Datenverarbeitung
│   ├── orderbook_controller.py      # Verwaltung des Orderbuchs
│   └── login_service.py             # Login und Token-Handling
│
├── templates/
│   └── index.html                   # Frontend
│
├── .env                             # Umgebungsvariablen
├── requirements.txt                 # Python-Abhängigkeiten
└── main.py                          # Einstiegspunkt der Anwendung
```

---

## **Verwendete Technologien**

- **Backend:**
  - `Flask` - Webserver und API
  - `Websockets` - Echtzeitdaten
  - `asyncio` - Asynchrone Verarbeitung

- **Frontend:**
  - `HTML` und `Tailwind CSS` - UI und Layout
  - `jQuery` - Datenverarbeitung und DOM-Manipulation

---

## **Mitwirken**

- **Pull Requests** sind willkommen!
- Bitte erstelle ein **Issue**, bevor du größere Änderungen vornimmst.

---

## **Autor**

👤 **SteGun93**  
🐙 **GitHub**: [https://github.com/SteGun93](https://github.com/SteGun93)

---

## **Danke für deinen Beitrag!**

---

Viel Erfolg mit deinem **Live Orderbuch für ATOS**! 🚀

