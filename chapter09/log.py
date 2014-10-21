import logging

logfile = 'log.out'

logging.basicConfig(filename=logfile, level=logging.DEBUG)

logging.debug("this message should go to the log file")

logger = logging.getLogger(__name__)
logger.info("this message too")
