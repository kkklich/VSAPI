from functools import lru_cache
import requests
# Supported intervals: 1min, 5min, 15min, 30min, 45min, 1h, 2h, 4h, 8h, 1day, 1week, 1month

api_key = "d0739ef720fd49f9bc8bd27139a679ee"

@lru_cache(maxsize=128)
def fetch_twelvedata(symbol, interval = "1day"):
    url = f"https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data

def get_twelvedata_values(symbol, interval="1day"):
    data = fetch_twelvedata(symbol, interval)
    return data.get("values", [])
