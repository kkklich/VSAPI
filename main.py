from fastapi import FastAPI
from typing import Optional
from loaderData import fetch_twelvedata, get_twelvedata_values

# run below command in terminal
# uvicorn main:app --reload

app = FastAPI()

#http://127.0.0.1:8000/ → check if API is live
@app.get("/")
def root():
    return {"status": "API is live"}

#http://127.0.0.1:8000/stock/?interval=1day&symbol=AMD → zwraca dane AMD
@app.get("/stock/")
def get_items(symbol: str, interval: Optional[str] = "1day"):
    data = fetch_twelvedata(symbol, interval)
    return data

#http://127.0.0.1:8000/stock/?interval=1day&symbol=AMD→ zwraca notowania AMD
@app.get("/stockValues/")
def get_items(symbol: str, interval: Optional[str] = "1day"):
    data = get_twelvedata_values(symbol, interval)
    return data

