import uvicorn
from fastapi import FastAPI
import ccxt
from datetime import datetime

srf = ccxt.bybit()

app = FastAPI()

@app.post("/{gtdate}")
def get_prs(gtdate : str):
    timeval = int(datetime.strptime(f"{gtdate} 12:00:00", "%Y/%m/%d %H:%M:%S").timestamp()*1000)
    getprs = srf.fetch_ohlcv('BTC/USDT', '1d', since=timeval)
    return {"prs" : getprs}

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8080)