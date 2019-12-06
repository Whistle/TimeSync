from datetime import datetime
from datetime import timedelta
from time import sleep

# setup tty serial device with
# stty -F /dev/ttyUSB0 9600

while True:
    dt = datetime.utcnow()
    delta = timedelta(seconds=1)
    ms = dt.microsecond/1000.0
    s = ms/1000.0
    sleep(1.0 - s)

    # setup payload
    msg = "{:04d}{:02d}{:02d}{:02d}{:02d}{:02d}".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    payload = bytearray()
    # Add header
    payload.append(0x55)
    payload.extend(map(ord, msg))
    # build checksum
    checksum = 0
    for b in payload:
        checksum = checksum ^ b
    payload.append(checksum)
    # mark message end
    payload.append(0xAA)
    with open('serial_dev', 'wb') as f:
        f.write(payload)
    break
