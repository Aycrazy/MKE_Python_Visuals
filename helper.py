import requests as req
from bs4 import BeautifulSoup
import json
import pandas as pd
from standardize import *
from key import api_key
from key import g_api_key

url = 'https://data.milwaukee.gov/api/3/action/datastore_search?resource_id='


def pull_data(url, record_id, api_key, u_text = False):
    '''
    pull data from ckan exploiting row limits and offsets
    '''

    limit = '50000'

    offset = 0

    empty = False

    df = pd.DataFrame()

    #for r_id in record_id:

    while not empty:

        print('offset'+ str(offset))

        url_adj = url+record_id+'&limit='+limit+'&offset='+str(offset)

        records = req.get(url_adj, auth=('Authorization', api_key))

        #soup = BeautifulSoup(records.content,'html.parser')
        records = records.json()

        print(records['success'])

        offset+=50000

        if records['success'] == True:

            # if u_text:

            #     if not len(pd.DataFrame(records)['result']['records']):
            #         return df
            #     else:
            #         df = df.append(pd.DataFrame(pd.io.json.json_normalize(records)['result']['records']))

            # else:

            if not len(pd.DataFrame(records)['result']['records']):
                return df
            else:
                new_df = pd.DataFrame(records['result']['records'])
                df = df.append(new_df)
        else:
            return df
            # else:

            #     print(pd.DataFrame(pd.read_json(soup.contents[0])).loc['records'].loc['result'][1])

            #     if not len(pd.DataFrame(pd.read_json(soup.contents[0])).loc['result'].loc['records']):
            #         return df
            #     else:
            #         df = df.append(pd.DataFrame(pd.read_json(soup.contents[0]).loc['result'].loc['records']))


lead_sl = 'c8c72ec0-8331-4ccb-949b-bd284d0054db'

crime_sl = '87843297-a6fa-46d4-ba5d-cb342fb2d3bb'


cfs_sl = '6b290551-3a5d-4d2b-a95e-2e82c28a0889'

master_prop = '0a2c7f31-cd15-4151-8222-09dd57d5f16d'

ems_18qtr2 = '2208b5e8-3b7a-48bc-97b7-02641a21aa4f'

#crime_df = pull_data(url, crime_sl, api_key)

#lead_df = pull_data(url, lead_sl, api_key)

#master_df = pull_data(url, master_prop, api_key)

#cfs_df = pull_data(url, cfs_sl, api_key)

#can multiprocessing help here?
