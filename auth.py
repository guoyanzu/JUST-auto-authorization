# -*- coding: UTF-8 -*-

import sys
import requests
import json

get = requests.get('http://10.250.255.34/api/v1/ip')

ip = get.json()["data"]

login_addr = "http://10.250.255.34/api/v1/login"

login_header = {
    'Host': '10.250.255.34',
    'Connection': 'keep-alive',
    'Content-Length': '133',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'http://10.250.255.34',
    'Referer': 'http://10.250.255.34/authentication/login',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
}

login_json = {
    "username":"",#account here
    "password":"",#passwd here
    "channel":"2",#ChinaMobile-2 ChinaTelecom-3 ChinaUnicom-4
    "ifautologin":"0",
    "pagesign":"secondauth",
    "usripadd":ip
}

print("login at",ip)

response = requests.post(login_addr,data=json.dumps(login_json,separators=(',',':')),headers=login_header)
