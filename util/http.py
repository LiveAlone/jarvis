#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

import json

import requests

'''
description: http 请求封装，结构化数据返回
'''


def post_json(url, headers, body, data=None):
    """ post 请求封装结果 """
    response = requests.post(url, json=body, headers=headers, data=data)
    if response.status_code != 200:
        print('http request fail code : ', response.status_code)
        raise RuntimeError(response.status_code)
    else:
        resp_entity = json.loads(response.content)
        return resp_entity


def get_json(url, headers, params) -> dict:
    """ get 请求封装 """
    return json.loads(get_content(url, headers, params))


def get_content(url, headers, params) -> bytes:
    """ get 请求原始数据结果 """
    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        print('http request fail code : ', response.status_code)
        raise RuntimeError(response.status_code)
    else:
        return response.content
