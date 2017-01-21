from commons import log
from commons import arg
from commons import config

import os
import logging

conf = config.get_config(file_path=arg.get_args_config().config_path)
logger = log.get_logger(logger=logging.getLogger(os.path.basename(__file__).split('.')[0]), config=conf)
