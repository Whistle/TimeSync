from datetime import datetime
from datetime import timedelta
from time import sleep

# setup tty serial device with
# stty -F /dev/ttyUSB0 9600

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
