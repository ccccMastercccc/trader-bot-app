from datetime import datetime
import time
import requests
import pandas as pd
import os

startDate = '2019-01-01'
market = 'okx'
crp1 = 'BTC'
crp2 = 'USDT'

tmsp = 0

svdlist = []

nowdt = datetime.now().timestamp()*1000
tmsp = int(datetime.strptime(f"{startDate} 00:00:00", "%Y-%m-%d %H:%M:%S").timestamp()*1000)
print(startDate)
while (nowdt - tmsp)/1000 > 90000:
    try:
       getprs = requests.post(f"http://194.146.123.51:8000/{market}/{startDate}")
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

print('convert to dtfrm....')
dtfm = pd.DataFrame(svdlist, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
try:
    os.mkdir(f'{crp1}-{crp2}')
    print('created dir...')
except FileExistsError:
    print('saving...')
dtfm.to_csv(f'{crp1}-{crp2}\{market}.csv')
print('saved.')