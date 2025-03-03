#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

import ai.keys

'''
description: TODO
'''

from openai import OpenAI

client = OpenAI(api_key=ai.keys.API_KEY, base_url="https://api.deepseek.com")
print(client.models.list())

import requests

url = "https://api.deepseek.com/user/balance"

payload={}
headers = {
  'Accept': 'application/json',
  'Authorization': f'Bearer {ai.keys.API_KEY}'
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)