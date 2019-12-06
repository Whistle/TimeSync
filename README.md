# Time Sync
Simple script which pulls the utc time and date from its host and writes the result to a device

## Usage
Setup your serial device with

```stty -F /dev/ttyUSB0 9600```

and call the script like this

```python time_sync.py /dev/ttyUSB0```

__Note:__ The script will loop forever and send the utc time every second to the device
