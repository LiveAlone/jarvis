# jarvis
py 日常脚本工作方式

## utils 工具模块
1. 文本内容输入输出。 txt, excel,file 内容处理
2. requests http 请求get, post 支持参数，json-body 返回结果内容解析。
3. template 模版引擎支持渲染方式。
4. mysql db 数据库数据内容阅读获取。
5. redis 缓存数据连接获取等

## Commands 命令行动态加载
基于Click模块，动态加载命令行工具

## 无头浏览器 playwright 支持录制方式
1. install [playwright](https://playwright.dev/python/docs/intro)
支持 HTML 录制执行脚本
```
pip install pytest-playwright
playwright install

# 交互方式录制流程 生成代码
playwright codegen https://123.cn/\#/login
```

## ipython 交互方式执行命令
```shell
ipython
```