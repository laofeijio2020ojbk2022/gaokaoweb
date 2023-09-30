import pymysql
import json
import csv
import time
import random
import pandas as pd
import numpy as np
from pandas import DataFrame

import os
from PIL import Image
from io import BytesIO

filePath = '../new_data/高校分数线/'
f_names = os.listdir(filePath)
# print(f_names)

def insert_sql(i, data, col_name):
    try:
        # 打开数据库连接
        # db = pymysql.connect(host='huadi', user='root', password='12345678', database='gaokao')
        # 使用 cursor() 方法创建一个游标对象 cursor
        # cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        sql = "insert into Score_Table(" + col_name + ") values(" + data + ")"
        # print(sql)
        cursor.execute(sql)

        db.commit()
        # cursor.close()
        # db.close()
    except:
        sql = "insert into Score_Table(" + col_name + ") values(" + data + ")"
        print(str(i), '插入失败：\n', sql)

for f_name in f_names:
    print(f_name)
    f_name2 = filePath + f_name
    # print(f_name2)
    df = pd.read_csv(f_name2)
    # print(df)
    del df['Unnamed: 0']
    col_name = []
    for i in df:
        col_name.append('ST_' + i)
    col_name[1] = 'SI_id'
    col_name[2] = 'Pro_id'
    col_name = ','.join(col_name)
    # print(col_name)

    db = pymysql.connect(host='huadi', user='root', password='12345678', database='gaokao')
    cursor = db.cursor()
    for i in range(len(df)):
        data = []
        for k in df:
            if type(df[k][i]) == str:
                data.append('"' + df[k][i] + ' "')
            else:
                data.append(str(df[k][i]).split('.')[0])

        data = ','.join(data)
        # print(data)

        insert_sql(i, data, col_name)

        # break

    print("-"*50)
    # break

    cursor.close()
    db.close()