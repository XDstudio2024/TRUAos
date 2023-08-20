import config
config.install()
while True:
    main = input('>')
    if main == '?':
        config.relate()
    elif main == 'info':
        config.info()
    elif main == 'write':
        config.write()
    elif main == 'github':
        config.github()
    elif main == 'calc':
        config.calc()
    elif main == 'find':
        config.find()
    elif main == 'search':
        config.search()
    elif main == 'plugins':
        config.plugin()