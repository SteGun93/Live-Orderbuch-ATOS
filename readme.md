# 📊 Live Orderbuch - ATOS

Beiträge und agentische Arbeit: [CONTRIBUTING.md](CONTRIBUTING.md) und [AGENTS.md](AGENTS.md).

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

## 🐳 Docker-Setup

Falls du die Anwendung mit **Docker** betreiben möchtest, kannst du dies einfach mit **Docker Compose** tun.

### 1️⃣ Container starten
Stelle sicher, dass **Docker** installiert ist und führe dann folgenden Befehl aus:

```sh
docker-compose up -d
```

- Die Anwendung läuft dann unter **`http://localhost:5001`** (Standardmäßig auf Port **5001**, kann in `docker-compose.yml` angepasst werden).
- **`-d`** sorgt dafür, dass der Container im Hintergrund läuft.

### 2️⃣ Container stoppen
Falls du den Container beenden möchtest:

```sh
docker-compose down
```

### 3️⃣ Logs anzeigen
Falls du die Live-Logs des Containers sehen möchtest:

```sh
docker logs -f live-orderbuch
```

### 4️⃣ Änderungen übernehmen (Neuaufbau)
Falls Änderungen am Code gemacht wurden und du den Container neu aufbauen möchtest:

```sh
docker-compose up --build -d
```

### 5️⃣ Port ändern
Falls du den Port ändern möchtest, passe die folgende Zeile in der `docker-compose.yml` an:

```yaml
ports:
  - "5001:5000"  # Ändere "5001" auf den gewünschten Port
```

Dann **Container neustarten**:

```sh
docker-compose down && docker-compose up -d
```

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

