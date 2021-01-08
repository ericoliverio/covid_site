#!/usr/bin/env python
import pandas as pd 
import requests 
from datetime import datetime

df = pd.read_csv("/Users/ericoliverio/Desktop/erie_total.csv")

print(df.head())

#Create HTML request headers and parameters
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Origin': 'http://erieny.maps.arcgis.com',
    'Connection': 'keep-alive',
    'Referer': 'http://erieny.maps.arcgis.com/apps/opsdashboard/index.html',
    'TE': 'Trailers',
}

params1 = (
    ('f', 'json'),
)

response = requests.get('https://erieny.maps.arcgis.com/sharing/rest/content/items/dd7f1c0c352e4192ab162a1dfadc58e1/data', headers=headers, params=params1)

#Request date of most recent update
timestamp = response.json()['headerPanel']['subtitle']
date = timestamp.split()[-1][:-1]
#time = timestamp[20:-1]

print('Date: '+str(date))
#print('Time: '+str(time))
#--------------

#Request daily totals
params = (
    ('f', 'json'),
    ('where', '1=1'),
    ('returnGeometry', 'false'),
    ('spatialRel', 'esriSpatialRelIntersects'),
    ('outFields', '*'),
    ('orderByFields', 'ZIP_CODE asc'),
    ('resultOffset', '0'),
    ('resultRecordCount', '80'),
    ('resultType', 'standard'),
    ('cacheHint', 'true'),
)

response = requests.get('https://services1.arcgis.com/CgOSc11uky3egK6O/arcgis/rest/services/erie_zip_codes_confirmed_counts/FeatureServer/0/query', headers=headers, params=params)

data = response.json()['features']
#explore these!!

lists = []
for a in data:
    zipcode = a['attributes']['ZIP_CODE']
    confirmed =a['attributes']['CONFIRMED']
    #pop =a['attributes']['POPULATION']
    #name = a['attributes']['PO_NAME']
    
    lists.append((zipcode,confirmed))
    
df_today = pd.DataFrame(lists,columns=['Zip Code',date])

#return df_today

new_data = df_today.columns[-1]
prev = df.columns[-1]
prev = datetime.strptime(prev, "%m/%d/%Y")
new_data = datetime.strptime(new_data, "%m/%d/%Y")

print('prev: '+str(prev))
print('new: '+str(new_data))

if new_data > prev:
    df[date] = df_today[date]
    df.to_csv("/Users/ericoliverio/Desktop/erie_total.csv",index=False)
    print('updated...')
else:
    print('Already updated')

df_confirm = pd.read_csv("/Users/ericoliverio/Desktop/erie_total.csv")

print(df_confirm.head())