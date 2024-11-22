#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: TODO
'''
import asyncio


async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')


if __name__ == '__main__':
    asyncio.run(main())
