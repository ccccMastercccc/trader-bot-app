import pandas as pd
from datetime import datetime
import time
import requests

crp1 = 'BTC'
crp2 = 'USDT'

market = 'okx'

readf = pd.read_csv(f'{crp1}-{crp2}/{market}.csv')

svdlist = []

gtlastDt = list(readf['timestamp'])[-1]
nowdt = datetime.now().timestamp()*1000

if (nowdt - gtlastDt)/1000 > 86400:
    while (nowdt - gtlastDt)/1000 > 86400:
        try:
            getprs = requests.post(f"http://194.146.123.51:8000/{market}/{gtlastDt}")
            if getprs.status_code == 200:
               lasttm = getprs.json()['prs'][-1][0]
               tmsp = lasttm
               rbtmst = datetime.fromtimestamp(lasttm/1000)
    
               svdlist = svdlist + getprs.json()['prs'][1:]
               
               print(rbtmst, len(svdlist))
               startDate = f"{rbtmst.year}-{rbtmst.month}-{rbtmst.day}"
               time.sleep(1)
        except:
            print("error")

print((nowdt - gtlastDt)/1000)
print(datetime.fromtimestamp(gtlastDt/1000).date())