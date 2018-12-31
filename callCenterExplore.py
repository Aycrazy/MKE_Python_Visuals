#%%
import pandas as pd
import re
import os
import bokeh as bo
import numpy as np 
import matplotlib as mp
from helper import *
from standardize import *

#%%
#live nuissance list
ln_list = ['rat','mice','mouse',\
'racoon','racoons','possum','vermin']

url_sql = "https://data.milwaukee.gov/api/3/action/datastore_search?"

rats_endpoint = "resource_id=bf2b508a-5bfa-49da-8846-d87ffeee020a&q=rats"


df = pull_data(url_sql, rats_endpoint, api_key)

for rodent_end in ln_list:
    df= df.append(pull_data(url_sql,rodent_end,api_key))

df = df.remove_duplicates(inplace=True)
#%%
#https://data.milwaukee.gov/api/3/action/datastore_search?resource_id=bf2b508a-5bfa-49da-8846-d87ffeee020a&q=mice
url_sql = "https://data.milwaukee.gov/api/3/action/datastore_search?"
mice_endpoint = "resource_id=bf2b508a-5bfa-49da-8846-d87ffeee020a&q=mice"

calls_mice = pull_data(url_sql, mice_endpoint, api_key)
#%%
calls_mice


#%%
#https://data.milwaukee.gov/api/3/action/datastore_search?resource_id=bf2b508a-5bfa-49da-8846-d87ffeee020a&q=mice
url_sql = "https://data.milwaukee.gov/api/3/action/datastore_search?"
rats_endpoint = "resource_id=bf2b508a-5bfa-49da-8846-d87ffeee020a&q=rats"

calls_rats = pull_data(url_sql, rats_endpoint, api_key)

#%%
url_sql = "https://data.milwaukee.gov/api/3/action/datastore_search?"
rodents_endpoint = "resource_id=bf2b508a-5bfa-49da-8846-d87ffeee020a&q=rodents"

calls_rats = pull_data(url_sql, rodents_endpoint, api_key)
