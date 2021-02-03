# zabbix-apcupsd

Zabbix template & script to monitor APC UPS through `apcupsd` daemon.
It gathers data directly from the `apcupsd` using TCP, no `apcaccess` needed.

Single Python script that emits all information needed for discovery & data gathering in a single JSON.
All items are defined as `Dependent` and extract relevant data using JSONPath queries.

<details>
    <summary>Click to expand JSON example</summary>

```json
{
  "ALARMDEL": "No alarm",
  "APC": "001,047,1135",
  "BATTDATE": "2017-08-07",
  "BATTV": 13.6,
  "BCHARGE": 100.0,
  "CABLE": "USB Cable",
  "CUMONBATT": 30,
  "DATE": "2021-02-03 18:04:34 +0300",
  "DRIVER": "USB UPS Driver",
  "DSHUTD": 0,
  "DWAKE": 0,
  "END APC": "2021-02-03 18:04:34 +0300",
  "FIRMWARE": "817.v9.I USB FW:v9",
  "HITRANS": 256.0,
  "HOSTNAME": "foobar",
  "ITEMP": 29.2,
  "LASTSTEST": "2021-01-22 20:30:45 +0300",
  "LASTXFER": "Low line voltage",
  "LINEFREQ": 50.0,
  "LINEV": 218.0,
  "LOADPCT": 9.0,
  "LOTRANS": 196.0,
  "MANDATE": "2012-06-18",
  "MAXTIME": 0,
  "MBATTCHG": 5,
  "MINTIMEL": 180,
  "MODEL": "Back-UPS CS 650",
  "NOMBATTV": 12.0,
  "NOMINV": 230,
  "NOMOUTV": 230,
  "NOMPOWER": 400,
  "NUMXFERS": 4,
  "OUTPUTV": 230.0,
  "RETPCT": 0.0,
  "SELFTEST": "NO",
  "SENSE": "High",
  "SERIALNO": "4B1225P01343",
  "STARTTIME": "2021-01-21 21:20:13 +0300",
  "STATFLAG": "0x05000008",
  "STATUS": "ONLINE",
  "STESTI": "None",
  "TIMELEFT": 1950.0,
  "TONBATT": 0,
  "UPSMODE": "Stand Alone",
  "UPSNAME": "apc",
  "VERSION": "3.14.14 (31 May 2016) debian",
  "XOFFBATT": "2021-02-03 12:40:22 +0300",
  "XONBATT": "2021-02-03 12:40:04 +0300"
}
```

</details>

## Features

- Items:
  - Line voltage & frequency
  - Battery charge & voltage
  - UPS status
  - Temperature
  - Model, serial, firmware
- Triggers:
  - UPS is not online
  - Self Test is running
  - Temperature
  - Overload
- Zabbix agent passive checks. Can be converted to active if needed.

## Macros

- `{$APCUPSD_CHARGE_CRIT}` - Battery charge crit threshold
- `{$APCUPSD_CHARGE_LOW}` - Battery charge low threshold
- `{$APCUPSD_HOST}` - Host to query
- `{$APCUPSD_PORT}` - Port to query
- `{$APCUPSD_LOAD_CRIT}` - UPS load crit threshold
- `{$APCUPSD_LOAD_HIGH}` - UPS load high threshold
- `{$APCUPSD_TEMP_CRIT}` - Temperature crit threshold
- `{$APCUPSD_TEMP_HIGH}` - Temperature high threshold

## Requirements

- Tested on Zabbix 5.0, but should work on 4.2+
- Python3

## Installation

- Place `apc.conf` in `/etc/zabbix/zabbix_agentd.d`
- Place `apc.py` in `/etc/zabbix/scripts`
  - You can put it into any other place, but then you'll have to adjust `apc.conf`
- Restart `zabbix-agentd`
- Import `template_apcupsd.xml`
- Adjust `{$APCUPSD_HOST}` and `{$APCUPSD_PORT}` macros if needed
- You're good to go
