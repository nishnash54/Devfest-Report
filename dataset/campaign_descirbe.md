## Devfest campaign

###### Description
Dataset contains details of all the various online publicity campaigns run through Email, whatsapp, Facebook, LinkedIn etc.

###### File name
```py
camapign_data.csv
```

###### Details
```py
Rows: 265
Columns: 18
Size: 64.8 kB
```

###### Column names
```py
[
    'fest_id',
    'campaign_id',
    'source',
    'ip',
    'city',
    'country',
    'countryCode',
    'isp',
    'lat',
    'lon',
    'org',
    'query',
    'region',
    'regionName',
    'status',
    'timezone',
    'zip',
    'timestamp'
]
```

###### Definition
```py
{
    'fest_id': Id of the event or fest,
    'campaign_id': Id of the online campaign,
    'source': Type of online campaing,
    'ip': User IP address,
    'city': User city,
    'country': User country,
    'countryCode': User country code,
    'isp': User Internet Service Provider,
    'lat': Latitude position,
    'lon': Longitude position,
    'org': Organization (ISP Company),
    'query': Queried data (IP Address),
    'region': User region code,
    'regionName': User region name,
    'status': Return status,
    'timezone': User timezone,
    'zip': User PIN code,
    'timestamp': Timestamp of API call,
}