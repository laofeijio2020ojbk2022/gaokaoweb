import pymysql
import json
import csv
import time
import random
import pandas as pd
import numpy as np
from pandas import DataFrame

df = pd.read_csv("../new_data/school_info3.csv")
# print(df.info())

col_name = []
for i in df:
    col_name.append("SC_" + i)
col_name[1] = 'SC_id'
col_name = ','.join(col_name[1:])
# print(col_name)


def insert_sql(i, data):
    try:
        # 打开数据库连接
        db = pymysql.connect(host='huadi', user='root', password='12345678', database='gaokao')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        sql = "insert into School_Info(" + col_name + ") values(" + data + ")"
        # print(sql)
        cursor.execute(sql)

        db.commit()
        cursor.close()
        db.close()
    except:
        sql = "insert into School_Info(" + col_name + ") values(" + data + ")"
        print(str(i), '插入失败：\n', sql)


for i in range(len(df)):
    data = []
    for j in df:
        # print(type(df[j][i]))
        if type(df[j][i]) == str:
            if i == 897:
                data.append("'无'")
            else:
                data.append("'" + df[j][i] + "'")
        elif type(df[j][i]) == np.int64:
            data.append(str(df[j][i]))
        elif type(df[j][i]) == float:
            data.append('""')
        else:
            print(j, i, df[j][i], type(df[j][i]))
            print(data)
    try:
        data = ','.join(data[1:])
    except:
        print(str(i), "转化失败\n", data)
    insert_sql(i, data)

    # break

