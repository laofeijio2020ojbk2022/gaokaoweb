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
School_id = df.sort_values(by='school_id')

for school in range(len(School_id)):
    # print(str(school_id['school_id'][school]))
    url = 'https://static-data.gaokao.cn/www/2.0/school/' + str(School_id['school_id'][school]) + '/info.json'
    print("get URL:\t", url)

    html = get_url(url)
    html = json.loads(html)
    html = json.dumps(html, ensure_ascii=False)
    # print(type(html))
    print(html)

    dic = [{"ok": 1}]
    data = pd.DataFrame(dic)
    # print(data)

    school_col = ['school_id', 'data_code', 'name', 'type', 'school_type', 'school_nature', 'level', 'code_enroll',
                  'belong', 'f985', 'f211', 'department', 'admissions', 'central', 'dual_class', 'is_seal',
                  'applied_grade', 'num_subject', 'num_master', 'num_doctor', 'num_academician', 'num_library',
                  'num_lab', 'province_id', 'city_id', 'is_ads', 'is_recruitment', 'create_date', 'area', 'old_name',
                  'is_fenxiao', 'status', 'add_id', 'add_time', 'ad_level', 'short', 'e_pc', 'e_app', 'ruanke_rank',
                  'single', 'colleges_level', 'doublehigh', 'wsl_rank', 'qs_rank', 'xyh_rank', 'is_sell', 'eol_rank',
                  'school_batch', 'us_rank', 'is_logo', 'num_master2', 'num_doctor2', 'ai_status', 'is_ads2',
                  'coop_money', 'bdold_name', 'gbh_num', 'level_name', 'type_name', 'school_type_name',
                  'school_nature_name', 'dual_class_name', 'xueke_rank', 'province_single', 'single_year', 'remark',
                  'province_name', 'city_name', 'town_name', 'weiwangzhan', 'yjszs', 'xiaoyuan', 'urllinks', 'email',
                  'school_email', 'address', 'postcode', 'site', 'school_site', 'phone', 'school_phone', 'miniprogram',
                  'content', 'video', 'video_pc', 'is_video', 'dualclass', 'special', 'nature_name',
                  'province_score_min', 'pro_type_min', 'pro_type', 'province_score_year', 'qs_world', 'rank',
                  'fenxiao', 'gbh_url', 'is_yikao', 'yk_feature', 'yk_type']

    for i in school_col:
        # print(i)
        if i == 'xueke_rank' or i == 'province_single' or i == 'video' or i == 'video_pc' or i == 'rank':
            # print(i, re.findall(r'"' + str(i) + '":(.*?)},', html)[0])
            data[i] = re.findall(r'"' + str(i) + '":(.*?)},', html)[0]
        elif i == 'remark' or i == 'yk_feature':
            # print(i, re.findall(r'"' + str(i) + '":(.*?)],', html)[0])
            data[i] = re.findall(r'"' + str(i) + '":(.*?)],', html)[0]
        elif i == 'urllinks' or i == 'province_score_min':
            try:
                # print(i, re.findall(r'"' + str(i) + '":(.*?)}},', html)[0])
                data[i] = re.findall(r'"' + str(i) + '":(.*?)}},', html)[0]
            except:
                # print(i, re.findall(r'"' + str(i) + '":(.*?)},', html)[0])
                data[i] = re.findall(r'"' + str(i) + '":(.*?)},', html)[0]
        elif i == 'dualclass' or i == 'special':
            try:
                # print(i, re.findall(r'"' + str(i) + '":(.*?)}],', html)[0])
                data[i] = re.findall(r'"' + str(i) + '":(.*?)}],', html)[0]
            except:
                # print(i, re.findall(r'"' + str(i) + '":(.*?)],', html)[0])
                data[i] = re.findall(r'"' + str(i) + '":(.*?)],', html)[0]
        elif i == 'pro_type' or i == 'yk_type':
            try:
                # print(i, re.findall(r'"' + str(i) + '":(.*?)]},', html)[0])
                data[i] = re.findall(r'"' + str(i) + '":(.*?)]},', html)[0]
            except:
                # print(i, re.findall(r'"' + str(i) + '":(.*?)},', html)[0])
                data[i] = re.findall(r'"' + str(i) + '":(.*?)},', html)[0]
        elif i == 'fenxiao':
            try:
                # print(i, re.findall(r'"' + str(i) + '":(.*?)}]}],', html)[0])
                data[i] = re.findall(r'"' + str(i) + '":(.*?)}]}],', html)[0]
            except:
                # print(i, re.findall(r'"' + str(i) + '":(.*?)],', html)[0])
                data[i] = re.findall(r'"' + str(i) + '":(.*?)],', html)[0]
        elif i == 'pro_type_min':
            try:
                # print(i, re.findall(r'"' + str(i) + '":(.*?)}}]},', html)[0])
                data[i] = re.findall(r'"' + str(i) + '":(.*?)}}]},', html)[0]
            except:
                # print(i, re.findall(r'"' + str(i) + '":(.*?)},', html)[0])
                data[i] = re.findall(r'"' + str(i) + '":(.*?)},', html)[0]
        else:
            # print(i, re.findall(r'"' + str(i) + '":(.*?), ', html)[0])
            data[i] = re.findall(r'"' + str(i) + '":(.*?), ', html)[0]
        # print(data[i])

    print(data)
    data.to_csv('../data/school_info.csv', mode='a', header=False, index=None)
    print('-'*30, School_id['name'][school], 'over', '-' * 30)

    # break

