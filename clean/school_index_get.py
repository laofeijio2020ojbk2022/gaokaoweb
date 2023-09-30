import pymysql
import json
import csv
import time
import random
import pandas as pd
import numpy as np
from pandas import DataFrame

df = pd.read_csv("../data/school_Image.csv", header=None)
# print(df.info())
col_name = ['Img_1', 'Img_2', 'Img_3', 'Img_4', 'Img_5', 'Img_6', 'Img_name']

df2 = pd.read_csv("../data/school_id.csv")

# for i in col_name:
#     df2[i] = '无'
# print(df2.head(2))
df.columns = ['school_id', 'name', 'Img_1', 'Img_2', 'Img_3', 'Img_4', 'Img_5', 'Img_6', 'Img_name']
# print(df.head(2))
df2 = df2.merge(df, on=['school_id', 'name'], how='left')

df2.replace(np.nan, "无", inplace=True)

df2.to_csv('../new_data/school_index2.csv', mode='w', header=True, index=None)


