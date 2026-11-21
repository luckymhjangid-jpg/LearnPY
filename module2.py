import datetime

now = datetime.datetime.now()
future_date = now + datetime.timedelta(days=3)
past_date = now - datetime.timedelta(days=3)
print(now)
print(future_date)
print(past_date)
date1 = datetime.datetime(2026,11,1)
date2 = datetime.datetime(2026,12,16)   
interval = date2 - date1
print(interval)