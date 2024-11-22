#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

import json
import typing

import requests

'''
description: 通过curl 转换requests 代码 
'''


def curl_request(json_data_handler: typing.Callable[[dict], dict] = None):
    """
    通过 https://curlconverter.com/python/ curl 转换成python 代码
    后面按照需要添加钩子参数
    :return:
    """
    cookies = {
    }

    headers = {
    }

    json_data = {
    }
    json_data = json_data_handler(json_data)

    response = requests.post(
        'https://www.ads',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    return response


def request(json_data_handler: typing.Callable[[dict], dict] = None):
    response = curl_request(json_data_handler)
    if response.status_code != 200:
        print('http request fail code : ', response.status_code)
        raise RuntimeError(response.status_code)
    return json.loads(response.content)
