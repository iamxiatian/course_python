import logging
import os

#logging.debug('debug message')
#logging.info('info message')
#logging.warning('warning message')
#logging.error('error message')
#logging.critical('critical message')


FILE = os.getcwd()
print('Current word dir:', FILE)
logging.basicConfig(filename=os.path.join(FILE, 'log.txt'),
                    level=logging.DEBUG)

logging.debug('more debug message...')
logging.info('more info messages...')
logging.warning('more warning messages...')
