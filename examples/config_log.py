import logging
import os

from kiki.commons import log
from kiki.settings import config

logger = log.get_logger(logger=logging.getLogger(os.path.basename(__file__).split('.')[0]), config=config)
logger.debug("qwe")
