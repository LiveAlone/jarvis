#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

import json

import ai.keys

'''
description: 对话补全
'''

from openai import OpenAI

client = OpenAI(api_key=ai.keys.API_KEY, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    frequency_penalty=0,
    max_tokens=1024,
    temperature=0.7,
    stream=False,
    # logprobs=True,
    # top_logprobs=20,
)

print(response)
print(f'chat id: {response.id}')
print(f'chat choices: {response.choices}')
print(f'chat created at: {response.created}')
print(f'chat object: {response.object}')
print(f'chat model: {response.model}')
print(f'chat usage: {response.usage}')
