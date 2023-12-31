#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yaoqijun'
__mail__ = 'yaoqijunmail@foxmail.com'

import os
import typing

import click

'''
description: 动态加载commands中所有子命令, @click.command()实现的完成列表展示
'''

plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')


@click.command()
@click.option('--sub', '-s', default=None, help='子命令前缀', type=str)
@click.pass_context
def sc(ctx: click.Context, sub: str) -> None:
    """ 展示子命令列表 """
    if sub is None:
        sub = ''
    for k, v in ctx.obj['commands'].items():
        if sub in k:
            # click.echo(click.style('Hello World!', fg='green'))
            # click.echo(click.style('Some more text', bg='blue', fg='white'))
            # click.echo(click.style('ATTENTION', blink=True, bold=True))
            click.echo(click.style(f'{k}', fg='yellow', bold=True))
            click.echo(f'  {v.help}')


class MyCLI(click.MultiCommand):
    """
    自定义动态解析多命令行参数
    """
    def __init__(
        self,
        name: typing.Optional[str] = None,
        **attrs: typing.Any,
    ) -> None:
        super().__init__(name, **attrs)
        self.commands: typing.MutableMapping[str, click.Command] = {}

    def list_commands(self, ctx):
        ctx.ensure_object(dict)
        if len(self.commands) == 0:
            self.__dynamic_load_command(ctx)
        return [cmd for cmd in self.commands.keys()]

    def get_command(self, ctx, name):
        ctx.ensure_object(dict)
        if name in self.commands:
            return self.commands[name]
        self.__dynamic_load_command(ctx)
        return self.commands.get(name)

    def __dynamic_load_command(self, ctx: click.Context) -> None:
        """ 动态加载文件夹下所有子命令 """
        # 获取命令行资源文件
        source_files = []
        for root, dirs, files in os.walk(plugin_folder):
            for file in files:
                if file.endswith('.py') and file != '__init__.py':
                    source_files.append(os.path.join(root, file))
        source_files.sort()

        # 解析command 函数
        for source_file in source_files:
            ns = {}
            with open(source_file) as f:
                code = compile(f.read(), source_file, 'exec')
                eval(code, ns, ns)
            prefix_name, ext_name = os.path.splitext(os.path.relpath(source_file, plugin_folder))
            for k, v in ns.items():
                if isinstance(v, click.core.Command):
                    self.commands[f'{prefix_name}/{k}'] = v

        self.commands['sc'] = sc
        ctx.obj['commands'] = self.commands


cli = MyCLI(help='动态加载目录下命令行工具')


if __name__ == '__main__':
    cli()