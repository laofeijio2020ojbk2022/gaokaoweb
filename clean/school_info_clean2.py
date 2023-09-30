from ast import Str
import time
import requests
import json
import csv
import time
import random
from sqlalchemy import null
import pandas as pd
from pandas import DataFrame
import re
import urllib.parse

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = pd.read_csv("../new_data/school_info.csv")
df_1 = df.copy()

for i in range(len(df_1['dualclass'])):
    try:
        dualclass = re.findall(r', class: (.*?)}', df_1['dualclass'][i])
        df_1['dualclass'][i] = ",".join(dualclass)
    except:
        df_1['dualclass'][i] = ''


for i in range(len(df_1['special'])):
    try:
        limit_year = re.findall(r' limit_year: (.*?), ', df_1['special'][i])
        # print(limit_year)
        special_name = re.findall(r' special_name: (.*?), ', df_1['special'][i])
        # print(special_name)
        level_name = re.findall(r' level_name: (.*?)}', df_1['special'][i])
        # print(level_name)

        special = []
        for j in range(len(limit_year)):
            a = ",".join([limit_year[j], special_name[j], level_name[j]])
            special.append('[' + a +']')
        # print(special)
        df_1['special'][i] = ",".join(special)
    except:
        df_1['special'][i] = ''



for i in range(len(df_1['fenxiao'])):
    fenxiao = re.sub(r'[0-9a-zA-Z :_{}]+', '', df_1['fenxiao'][i]).replace(',,', ',')\
        .replace(',],', ',]').replace(',[,', ',[').replace(',[', ',{').replace('],', '}.')\
        .replace(']]', '}]').replace('{', '[').replace('}', ']')
    fenxiao = fenxiao[1:-1].split('.')
    a = []
    for j in fenxiao:
        a.append('{' + j + '}')
    # print(','.join(a))
    fenxiao = a
    if fenxiao == ['{}']:
        df_1['fenxiao'][i] = ''
    else:
        df_1['fenxiao'][i] = ','.join(fenxiao)

del df_1['Unnamed: 0']
df_1.to_csv('../new_data/school_info2.csv', mode='w', header=True, index=None)