import pandas as pd

from credentials import mongodb_parameters
from pymongo import MongoClient

# Global parameters
params = mongodb_parameters()
file_name = 'campaign_data.csv'
col_names = [
    'fest_id',
    'campaign_id',
    'source',
    'ip',
    'as',
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
values = []

def parse_dict(data):

    values = []

    for key in list(data.keys())[1:]:
        if type(data[key]) is dict:
            values.extend(parse_dict(data[key]))
        else:
            values.append(data[key])

    return values

def get_data(dblink, database_name, collection_name, file_name):
    
    database = []
    global col_names
    
    try:
        client = MongoClient(dblink)
        db = client[database_name]
        collection = db[collection_name]
        cursor = collection.find({})
        for doc in cursor:
            row = parse_dict(doc)
            if len(row) == 18:
                database.append(row)
            
        df = pd.DataFrame(database, columns=col_names)
        print(df.head())
        df.to_csv(file_name, index=False)
        return 'Data parsed to csv file'
    
    except:
        return 'Connection cannot be estb.'

if __name__ == "__main__":

    data = get_data(*params.values(), file_name), 
    print(data)