#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

import click

'''
description: 
'''


@click.command
def sdist():
    """ 这个是  sdist 命令行 """
    click.echo('sdist called')


@click.command
def bdist_wheel():
    """ 这个是 bdist_wheel 命令行 """
    click.echo('bdist_wheel called')
