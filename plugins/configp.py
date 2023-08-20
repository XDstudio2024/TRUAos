import os


def list():
    file = open('plugins.txt', 'r', encoding='utf-8')
    plugin = file.read()
    list = plugin.split(' ')
    print('---------------------------------------------------------')
    for i in list:
        print(i)
    print('---------------------------------------------------------')
    file.close()
def use():
    uses = input('name:')
    file = open('config/'+uses+'.txt', 'r', encoding='utf-8')
    plugin = file.read()
    list = plugin.split(' ')
    file.close()
    os.system(plugin)
