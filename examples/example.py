from commons import log
from commons import arg
import os
import logging
from settings import config

logger = log.get_logger(logger=logging.getLogger(os.path.basename(__file__).split('.')[0]), config=config)
logger.info("qwe")