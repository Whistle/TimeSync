from datetime import datetime
from datetime import timedelta
from time import sleep
import sys

def sync_loop(device):
    while True:
        # determine now
        now = datetime.utcnow()
        ms = now.microsecond/1000.0
        s = ms/1000.0

        # determine the future (now + 1 second)
        one_second = timedelta(seconds=1)
        one_second_later = now + one_second

        # setup payload
        payload = bytearray()
        # add header
        payload.append(0x55)
        # add body
        body = "{:04d}{:02d}{:02d}{:02d}{:02d}{:02d}".format(one_second_later.year, one_second_later.month, one_second_later.day, one_second_later.hour, one_second_later.minute, one_second_later.second)
        payload.extend(map(ord, body))
        # add checksum
        checksum = 0
        for b in payload:
            checksum = checksum ^ b
        payload.append(checksum)
        # mark message end
        payload.append(0xAA)

        # wait until next second starts and send future time
        sleep(1.0 - s)
        try:
            with open(device, 'wb') as f:
                f.write(payload)
            print("send: ", body, " - ", ms, "ms off", flush=True)
        except:
            print("Unable to write to ", device, flush=True)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        sync_loop(sys.argv[1])
    else:
        print("please execute the script like this: python ", sys.argv[0], " /dev/ttyUSB0")
