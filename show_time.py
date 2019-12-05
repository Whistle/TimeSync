from datetime import datetime
from datetime import timedelta
from time import sleep

while True:
    dt = datetime.utcnow()
    print(dt)
    delta = timedelta(seconds=1)
    print(dt + delta)
    ms = dt.microsecond/1000.0
    print(ms)
    s = ms/1000.0
    print(s)
    sleep(1.0 - s)
