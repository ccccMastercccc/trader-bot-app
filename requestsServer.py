from datetime import datetime
import time
import requests

startDate = '2024-01-01'

tmsp = 0

nowdt = datetime.now().timestamp()*1000
tmsp = int(datetime.strptime(f"{startDate} 00:00:00", "%Y-%m-%d %H:%M:%S").timestamp()*1000)
print(startDate)
while (nowdt - tmsp)/1000 > 90000:
    try:
       getprs = requests.post(f"http://194.146.123.51:8000/okx/{startDate}")
       if getprs.status_code == 200:
          lasttm = getprs.json()['prs'][-1][0]
          tmsp = lasttm
          rbtmst = datetime.fromtimestamp(lasttm/1000)
          print(rbtmst)
          startDate = f"{rbtmst.year}-{rbtmst.month}-{rbtmst.day}"
          #print((nowdt - tmsp))
          time.sleep(1)
    except:
        print("error")