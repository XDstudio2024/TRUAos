import os
import configp

while True:
    main = input('插件管理器:')
    if main == 'list':
        configp.list()
    elif main == 'use':
        configp.use()
