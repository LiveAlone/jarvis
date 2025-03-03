#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

import ai.keys

'''
description: Fill-In-the-Middle 补全API
'''

from openai import OpenAI

client = OpenAI(
  api_key=ai.keys.API_KEY,
  base_url="https://api.deepseek.com/beta",
)
response = client.completions.create(
  model="deepseek-chat",
  prompt="def fib(a):",
  suffix="    return fib(a-1) + fib(a-2)",
  max_tokens=128)
print(response.choices[0].text)
