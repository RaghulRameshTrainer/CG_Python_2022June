import logging

'''
debug     10
info      20
warning  30
error    40
critical 50
'''

logging.basicConfig(level=logging.DEBUG,
                    filename='output.log',
                    format='%(levelname)s - %(asctime)s - %(message)s',
                    filemode='w')
logger=logging.getLogger()
logger.info("Information message")
logger.debug("Debug message")
logger.warning("Warning message")
logger.error("Error messages")
logger.critical("Critical message")