# dev TRUA DEV 171
import os
import time
import sys
import webbrowser

# 配置返回文件

def install():
    file = open('install.txt','r',encoding='utf-8')
    ins = file.read()
    if ins == '0':
        oobe()
    else:
        info()
def oobe():
    print('启动程序后可以输入?来查看可用操作')
def relate():
    print('info 系统关于')
    print('write 打开文件编辑器')
    print('github 快速打开GitHub')
    print('calc 打开计算器')
    print('find 打开文件查找工具')
    print('search 开始打开搜索引擎')
    print('plugin 打开插件管理器')
def info():  # 系统关于
    print('TRUA os')
    print('版本号 2.0.0 BETA')
    print('开发者 TRUA DEV 171')
def search():
    webbrowser.open('www.bing.com')
    print('操作完成!')
def write():
    os.system('PROGRAMS\write\write.exe')
    print('操作完成！')
def find():
    os.system('PROGRAMS\Everything.exe')
    print('操作完成！')
def calc():
    os.system('PROGRAMS\calc.exe')
    print('操作完成！')
def github():
    webbrowser.open('github.com')

def plugin():
    os.system(r'python plugins\plugins.py')