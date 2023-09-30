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


headers_list = [
    {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666'
    }, {
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320'
    }, {
        'user-agent': 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+'
    }, {
        'user-agent': 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)'
    }, {
        'user-agent': 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    }, {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    }
]

headers = random.choice(headers_list)


def get_url(url):
    try:
        response = requests.get(url, headers=headers, timeout=1)  # 超时设置为10秒
    except:
        response = requests.get(url, headers=headers, timeout=20)

    html_str = response.text
    return html_str


df = pd.read_csv("../data/school_id.csv")
# print(df.head())
school_id = df.sort_values(by='school_id')

years = [2020, 2021, 2022, 2023]

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

pro_df = pd.DataFrame(province_id)
pro_id = pro_df['name']
# print(pro_id)

for school in range(len(school_id)):
    # print(pro)
    for year in years:
        for pro in range(len(pro_df)):
            url = 'https://static-data.gaokao.cn/www/2.0/schoolspecialscore/' + str(
                school_id['school_id'][school]) + '/' + str(
                year) + '/' + str(pro_df['name'][pro]) + '.json'
            print("get URL:\t", url)

            html = get_url(url)
            html = json.loads(html)
            html = json.dumps(html, ensure_ascii=False)
            # print(type(html))
            print(html)

            School = re.findall(r'"school_id":(.*?),', html)
            # print(School)
            Special_id = re.findall(r'"special_id":(.*?),', html)
            # print(Special_id)
            Type = re.findall(r'"type":(.*?),', html)
            # print(Type)
            Batch = re.findall(r'"batch":(.*?),', html)
            # print(Batch)
            Zslx = re.findall(r'"zslx":(.*?),', html)
            # print(Zslx)
            Max = re.findall(r'"max":(.*?),', html)
            # print(Max)
            Min = re.findall(r'"min":(.*?),', html)
            # print(Min)
            Average = re.findall(r'"average":(.*?),', html)
            # print(Average)
            Min_section = re.findall(r'"min_section":(.*?),', html)
            # print(Min_section)
            Province = re.findall(r'"province":(.*?),', html)
            # print(Province)
            Spe_id = re.findall(r'"spe_id":(.*?),', html)
            # print(Spe_id)
            Info = re.findall(r'"info":(.*?),', html)
            # print(Info)
            Special_group = re.findall(r'"special_group":(.*?),', html)
            # print(Special_group)
            First_km = re.findall(r'"first_km":(.*?),', html)
            # print(First_km)
            Sp_type = re.findall(r'"sp_type":(.*?),', html)
            # print(Sp_type)
            Sp_fxk = re.findall(r'"sp_fxk":(.*?),', html)
            # print(Sp_fxk)
            Sp_sxk = re.findall(r'"sp_sxk":(.*?),', html)
            # print(Sp_sxk)
            Sp_info = re.findall(r'"sp_info":(.*?),', html)
            # print(Sp_info)
            Sp_xuanke = re.findall(r'"sp_xuanke":(.*?),', html)
            # print(Sp_xuanke)
            Level1_name = re.findall(r'"level1_name":(.*?),', html)
            # print(Level1_name)
            Level2_name = re.findall(r'"level2_name":(.*?),', html)
            # print(Level2_name)
            Level3_name = re.findall(r'"level3_name":(.*?),', html)
            # print(Level3_name)
            Level1 = re.findall(r'"level1":(.*?),', html)
            # print(Level1)
            Level2 = re.findall(r'"level2":(.*?),', html)
            # print(Level2)
            Level3 = re.findall(r'"level3":(.*?),', html)
            # print(Level3)
            Spname = re.findall(r'"spname":(.*?),', html)
            # print(Spname)
            Zslx_name = re.findall(r'"zslx_name":(.*?),', html)
            # print(Zslx_name)
            Local_batch_name = re.findall(r'"local_batch_name":(.*?),', html)
            # print(Local_batch_name)
            Sg_fxk = re.findall(r'"sg_fxk":(.*?),', html)
            # print(Sg_fxk)
            Sg_sxk = re.findall(r'"sg_sxk":(.*?),', html)
            # print(Sg_sxk)
            Sg_type = re.findall(r'"sg_type":(.*?),', html)
            # print(Sg_type)
            Sg_name = re.findall(r'"sg_name":(.*?),', html)
            # print(Sg_name)
            Sg_info = re.findall(r'"sg_info":(.*?),', html)
            # print(Sg_info)
            Sg_xuanke = re.findall(r'"sg_xuanke":(.*?),', html)
            # print(Sg_xuanke)

            Year = []
            School_name = []
            for j in range(len(Sg_xuanke)):
                Year.append(year)
                School_name.append(school_id['name'][school])

            print(Year)
            print(School_name)

            df_it = DataFrame(
                zip(School, Special_id, Type, Batch, Zslx, Max, Min, Average, Min_section, Province, Spe_id, Info,
                    Special_group, First_km, Sp_type, Sp_fxk, Sp_sxk, Sp_info, Sp_xuanke, Level1_name, Level2_name,
                    Level3_name, Level1, Level2, Level3, Spname, Zslx_name, Local_batch_name, Sg_fxk, Sg_sxk, Sg_type,
                    Sg_name, Sg_info, Sg_xuanke, Year, School_name)
            )

            print(df_it)

            df_name = "../data/高校分数线/" + str(pro_df['value'][pro]) + ".csv"
            df_it.to_csv(df_name, mode='a', header=False, index=None)

            break
            time.sleep(random.uniform(1.5, 2.5))
        break
    break

# https://static-data.gaokao.cn/www/2.0/schoolspecialscore/31/2020/11.json
