#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

'''
description: login
'''

import re
from playwright.sync_api import Playwright, sync_playwright, expect, BrowserContext


def ctx_login(ctx: BrowserContext) -> None:
    """ 统一登录平台 """
    page = ctx.new_page()
    page.goto("https://123.cn/#/login")
    page.get_by_placeholder("用户名").fill("")
    page.get_by_placeholder("密码").fill("")
    page.get_by_role("button", name="登录").click()
    validate_code  = input("输入OA登录验证码: ")
    page.get_by_placeholder("验证码").fill(validate_code)
    page.get_by_role("button", name="登录").click()

def ctx_action(ctx: BrowserContext) -> None:
    """ 登录完成，相关页面等待执行 """
    page2 = ctx.new_page()
    page2.goto("https://123.cn/")
    page2.goto("https://123.cn/#/")
    page2.get_by_text("123").click()
    page2.get_by_label("111").get_by_role("textbox").fill("select * from ")
    page2.get_by_role("button", name="Execute Sync").click()

def oa_auto():
    """ 自动化界面 playwright codegen 执行录入自动化结果内容 """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        ctx_login(context)
        context.close()
        browser.close()

if __name__ == '__main__':
    oa_auto()
