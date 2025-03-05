import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()
LOGIN_URL = "https://www.boursorama.com/streaming/bootstrap"
DEBUG = os.getenv("DEBUG", "false").lower() in ("true", "1", "yes")

def debug_log(message):
    if DEBUG:
        print(message)

def get_boursorama_login():
    """Holt die aktuellen Login-Daten für den WebSocket-Feed und zusätzliche Konfigurationswerte."""
    try:
        debug_log("🔄 Sende Anfrage an die Login-API...")
        response = requests.get(LOGIN_URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        debug_log(f"✅ Config-Daten erhalten: \n{data}")
        
        config = data.get("config", {})
        login = config.get("login")
        password = config.get("password")
        timeout = config.get("timeout", 0) 
        ttl = config.get("ttl", 1800) 
        uri = config.get("uri", "wss://streaming.boursorama.com/quotes")
        quota_period = config.get("quotaPeriod", 3600)
        quota_limit = config.get("quotaLimit", 600)
        exchanges = config.get("filterExchangeCodes", [])
        symbols = config.get("filterSymbols", [])

        expiration_time = time.time() + ttl 

        if login in [None, "login"] or password in [None, "password"]:
            debug_log("⚠ Fehlerhafte Login-Daten erhalten! Erneuter Versuch in 10 Sekunden...")
            time.sleep(10)
            return get_boursorama_login()

        debug_log(f"🔑 Login erfolgreich erhalten: {login} / {password}")
        debug_log(f"📌 Timeout: {timeout}, TTL: {ttl}, Ablauf in {expiration_time - time.time():.0f} Sekunden")
        debug_log(f"🌍 WebSocket-URI: {uri}")
        debug_log(f"📊 Börsenfilter: {exchanges}")
        debug_log(f"📈 Symbolfilter: {symbols}")
        debug_log(f"📏 API-Limit: {quota_limit} Anfragen pro {quota_period} Sekunden")

        return {
            login, password
        }
    except requests.RequestException as e:
        debug_log(f"⚠ Fehler beim Abrufen der Login-Daten: {e}")
        return None
