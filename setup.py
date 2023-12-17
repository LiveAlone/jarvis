#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

import stringcase
import click

'''
description: 脚本项目启动
'''


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    ctx.obj['DEBUG'] = debug


@cli.command()
@click.pass_context
def sync(ctx):
    click.echo(f"Debug is {'on' if ctx.obj['DEBUG'] else 'off'}")


if __name__ == '__main__':
    cli(obj={})


