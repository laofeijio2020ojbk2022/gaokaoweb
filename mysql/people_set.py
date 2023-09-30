import pymysql
import json
import csv
import time
import random
import pandas as pd
import numpy as np
from pandas import DataFrame

col_name = ['P_name', 'P_password', 'P_sex', 'P_age', 'P_word', 'P_score', 'P_pro', 'P_adm']
col_name = ','.join(col_name)

# 打开数据库连接
db = pymysql.connect(host='huadi', user='root', password='12345678', database='gaokao')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

def insert_sql(i, data):
    try:

        # 使用 execute()  方法执行 SQL 查询
        sql = "insert into People (" + col_name + ") values(" + data + ")"
        # print(sql)
        cursor.execute(sql)

        db.commit()

    except:
        sql = "insert into People (" + col_name + ") values(" + data + ")"
        print(str(i), '插入失败：\n', sql)


df = pd.read_csv("../new_data/final.csv")
print(df.head(5))

for i in range(len(df)):
    P_name = "'" + str(df['P_name'][i]) + "'"
    P_password = "'" + str(df['P_password'][i]) + "'"
    P_sex = str(df['P_sex'][i])
    P_age = str(df['P_age'][i])
    P_word = "'" + str(df['P_word'][i]) + "'"
    P_score = str(df['P_score'][i])
    P_pro = "'" + str(df['P_pro'][i]) + "'"
    P_adm = str(df['P_adm'][i])

    data = [P_name, P_password, P_sex, P_age, P_word, P_score, P_pro, P_adm]
    data = ','.join(data)
    print(data)

    insert_sql(i, data)


cursor.close()
db.close()