import logging

__author__  = "davood akbari <daak1365@yahoo.com>"
__status__  = "production"
__version__ = "0.0.0.1"
__date__    = "27 November 2017"


logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s [%(threadName)-12.12s] [%(name)-12s] [%(levelname)-5.5s]  %(message)s",
                    # datefmt='%m-%d %H:%M',
                    filename='../log/daak.log',
                    filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("[%(threadName)-12.12s] [%(name)-12s] [%(levelname)-5.5s]  %(message)s")
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


loggerDaak = logging.getLogger('daak')

# logging.info('Jackdaws love my big sphinx of quartz.')

# logger1 = logging.getLogger('myapp.area1')
# logger2 = logging.getLogger('myapp.area2')

# logger1.debug('Quick zephyrs blow, vexing daft Jim.')
# logger1.info('How quickly daft jumping zebras vex.')
# logger2.warning('Jail zesty vixen who grabbed pay from quack.')
# logger2.error('The five boxing wizards jump quickly.')




