# Time Sync
Simple script which pulls the utc time and date from its host and writes the result to a device

## Usage
Simply call the script like this

```python time_sync.py /dev/ttyUSB0```

__Note:__ The script will loop forever and send the utc time every second to the device
