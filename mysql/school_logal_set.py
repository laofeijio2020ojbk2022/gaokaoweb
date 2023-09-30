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

col_name = ['Logao_id', 'Logal_name', 'Logal_data']
col_name = ','.join(col_name)

def insert_sql(i, a, name, img):
    try:
        # 打开数据库连接
        db = pymysql.connect(host='huadi', user='root', password='12345678', database='gaokao')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        sql = "insert into School_Logal(Logao_id,Logal_name,Logal_data) values(%s,%s,%s);"
        # print(sql)
        cursor.execute(sql, (str(a), name, img))

        db.commit()
        cursor.close()
        db.close()
    except:
        sql = "insert into School_Logao(Logao_id,Logal_name,Logal_data) values(%s,%s,%s);"
        print(str(i), '插入失败：\n', sql % (str(a), name, img))

filePath = '../data/school_logal/'
name = os.listdir(filePath)
# print(name)

df = pd.read_csv("../data/school_id.csv")

for i in name:
    # data = []

    name = i.split('.')[0]
    print(name)
    a = list(df[df['name'] == name]['school_id'])[0]
    # print(type(a))
    # data.append(str(a))

    # data.append("'" + name + "'")

    with open(filePath + i, 'rb') as f:
        img = f.read()
    # print(img)
    # data.append(img)

    # data = ','.join(data)
    # print(data)

    insert_sql(i, a, name, img)

    # break
