import pymysql
import json
import csv
import time
import random
import pandas as pd
import numpy as np
from pandas import DataFrame

col_name = ['min_ST_School_name', 'min_Pro_name', 'min_ST_name', 'min_ST_Local_batch_name', 'min_ST_Min_section']
col_name = ','.join(col_name)

# 打开数据库连接
db = pymysql.connect(host='huadi', user='root', password='12345678', database='gaokao')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

def insert_sql(i, data):
    try:

        # 使用 execute()  方法执行 SQL 查询
        sql = "insert into sc_min_ana(" + col_name + ") values(" + data + ")"
        # print(sql)
        cursor.execute(sql)

        db.commit()

    except:
        sql = "insert into sc_min_ana(" + col_name + ") values(" + data + ")"
        print(str(i), '插入失败：\n', sql)


df = pd.read_csv("../new_data/part-00000-99bdedec-9fb2-40f8-9887-715bdba1edf6-c000.csv")
print(df.head(5))

for i in range(len(df)):
    data = []
    for j in df:
        if type(df[j][i]) == np.int64:
            data.append(str(df[j][i]))
        else:
            data.append("'" + df[j][i] + "'")
    data = ','.join(data)
    # print(data)

    insert_sql(i, data)

    # break

cursor.close()
db.close()