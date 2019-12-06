from datetime import datetime
from datetime import timedelta
from time import sleep

# setup tty serial device with
# stty -F /dev/ttyUSB0 9600

while True:
    # determine now
    now = datetime.utcnow()
    ms = now.microsecond/1000.0
    s = ms/1000.0

    # determine the future (now + 1 second)
    delta = timedelta(seconds=1)
    next_second = now + delta

    # setup payload
    msg = "{:04d}{:02d}{:02d}{:02d}{:02d}{:02d}".format(next_second.year, next_second.month, next_second.day, next_second.hour, next_second.minute, next_second.second)
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

    # wait until next second start and send future time
    sleep(1.0 - s)
    with open('serial_dev', 'wb') as f:
        f.write(payload)
    print("send: ", msg, flush=True)
