import pymysql
import json
import csv
import time
import random
import pandas as pd
import numpy as np
from pandas import DataFrame

df = pd.read_csv("../new_data/school_index2.csv")
# print(df.info())
col_name = ['SI_id', 'SI_name', 'Img_1', 'Img_2', 'Img_3', 'Img_4', 'Img_5', 'Img_6', 'Img_name']
col_name = ','.join(col_name)

def insert_sql(i, data):
    try:
        # 打开数据库连接
        db = pymysql.connect(host='huadi', user='root', password='12345678', database='gaokao')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        sql = "insert into School_Index(" + col_name + ") values(" + data + ")"
        # print(sql)
        cursor.execute(sql)

        db.commit()
        cursor.close()
        db.close()
    except:
        sql = "insert into School_Index(" + col_name + ") values(" + data + ")"
        print(str(i), '插入失败：\n', sql)


for i in range(len(df)):
    data = []
    data.append(str(df['school_id'][i]))
    for k in df:
        if k == 'school_id':
            pass
        else:
            data.append("'" + df[k][i] + "'")

    try:
        data = ','.join(data)
    except:
        print(str(i), "转化失败\n", data)

    insert_sql(i, data)
