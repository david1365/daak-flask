REGISTERED_CLASSES = []


def registered_class(cls):
    REGISTERED_CLASSES.append(cls)
    return cls




@registered_class
def myFunction():
    print 'calling my funcion...'




# from os.path import basename, dirname, join
# from glob import glob
# pwd = dirname(__file__)
# for x in glob(join(pwd, '*.py')):
#     if not x.startswith('__'):
#         __import__(basename(x)[:-3], globals(), locals())


for x in REGISTERED_CLASSES:
    x();


__all__ = [
    'REGISTERED_CLASSES'
]