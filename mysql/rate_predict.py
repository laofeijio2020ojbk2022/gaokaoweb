import pymysql
import json
import csv
import time
import random
import pandas as pd
import numpy as np
from pandas import DataFrame

col_name = ['ra_School_id', 'ra_School_name', 'ra_Loc_province', 'ra_Pro_id', 'ra_Pro_name',
            'ra_Avg_Min_2021', 'ra_Avg_Min_2022', 'ra_Score_rate', 'ra_Avg_Min_section_2021',
            'ra_Avg_Min_section_2022', 'ra_section_rate', 'ra_average_score', 'ra_average_section',
            'ra_predict_score', 'ra_predict_section']
col_name = ','.join(col_name)

# 打开数据库连接
db = pymysql.connect(host='huadi', user='root', password='12345678', database='gaokao')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

def insert_sql(i, data):
    try:

        # 使用 execute()  方法执行 SQL 查询
        sql = "insert into rate_predict (" + col_name + ") values(" + data + ")"
        # print(sql)
        cursor.execute(sql)

        db.commit()

    except:
        sql = "insert into rate_predict (" + col_name + ") values(" + data + ")"
        print(str(i), '插入失败：\n', sql)


df = pd.read_csv("../new_data/rate_predict(0.1).csv")
print(df.head(5))

for i in range(len(df)):
    data = []
    for j in df:
        if type(df[j][i]) == str:
            data.append("'" + df[j][i] + "'")
        elif j == 'ra_School_id' or j == 'ra_Pro_id' or j == 'ra_Avg_Min_2021' or j == 'ra_Avg_Min_2022'\
                or j == 'ra_Avg_Min_section_2021' or j == 'ra_Avg_Min_section_2022':
            data.append(str(df[j][i]))
        else:
            data.append(str(round(df[j][i], 2)))
    data = ','.join(data)
    # print(data)

    insert_sql(i, data)

    # break

cursor.close()
db.close()