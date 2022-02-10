import logging

# Gets or creates a logger
logger = logging.getLogger(__name__)

# set log level
logger.setLevel(logging.WARNING)

# define file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

# Logs
logger.debug('A debug message')
logger.info('An info message')
logger.warning('Something is not right.')
logger.error('A Major error has happened.')
logger.critical('Fatal error. Cannot continue')

def log(text, level):
    if level == 'warning':
        logger.setLevel(logging.WARNING)
        logger.warning(text)

    elif level == 'info':
        logger.setLevel(logging.INFO)
        logger.info(text)

    elif level == 'error':
        logger.setLevel(logging.ERROR)
        logger.error(text)

    elif level == 'critical':
        logger.setLevel(logging.CRITICAL)
        logger.critical(text)

    else:
        logger.setLevel(logging.INFO)
        logger.info(text)

log("pruebas 123","warning")

kwargs = {'a':3, 'b':4, 'c':hypotenuse(3, 4)}

logger.debug('A debug message').format(**kwargs)