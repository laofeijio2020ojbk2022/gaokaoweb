import pymysql
import json
import csv
import time
import random
import pandas as pd
import numpy as np
from pandas import DataFrame


col_name = ['Pro_id', 'Pro_name']
col_name = ','.join(col_name)

def insert_sql(i, data):
    try:
        # 打开数据库连接
        db = pymysql.connect(host='huadi', user='root', password='12345678', database='gaokao')
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        sql = "insert into Pro_Index(" + col_name + ") values(" + data + ")"
        # print(sql)
        cursor.execute(sql)

        db.commit()
        cursor.close()
        db.close()
    except:
        sql = "insert into Pro_Index(" + col_name + ") values(" + data + ")"
        print(str(i), '插入失败：\n', sql)

province_id = [{"name": 11, "value": "北京"}, {"name": 12, "value": "天津"}, {"name": 13, "value": "河北"},
               {"name": 14, "value": "山西"}, {"name": 15, "value": "内蒙古"}, {"name": 21, "value": "辽宁"},
               {"name": 22, "value": "吉林"}, {"name": 23, "value": "黑龙江"}, {"name": 31, "value": "上海"},
               {"name": 32, "value": "江苏"}, {"name": 33, "value": "浙江"}, {"name": 34, "value": "安徽"},
               {"name": 35, "value": "福建"}, {"name": 36, "value": "江西"}, {"name": 37, "value": "山东"},
               {"name": 41, "value": "河南"}, {"name": 42, "value": "湖北"}, {"name": 43, "value": "湖南"},
               {"name": 44, "value": "广东"}, {"name": 45, "value": "广西"}, {"name": 46, "value": "海南"},
               {"name": 50, "value": "重庆"}, {"name": 51, "value": "四川"}, {"name": 52, "value": "贵州"},
               {"name": 53, "value": "云南"}, {"name": 54, "value": "西藏"}, {"name": 61, "value": "陕西"},
               {"name": 62, "value": "甘肃"}, {"name": 63, "value": "青海"}, {"name": 64, "value": "宁夏"},
               {"name": 65, "value": "新疆"}]

df = pd.DataFrame(province_id)
# print(df)
for i in range(len(df)):
    Pro_id = str(df['name'][i])
    Pro_name = "'" + df['value'][i] + "'"
    data = [Pro_id, Pro_name]
    data = ','.join(data)
    insert_sql(i, data)