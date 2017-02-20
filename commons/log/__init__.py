import logging.handlers
import os
import time


def get_logger(logger, level=logging.DEBUG, path='../log', prefix='%Y/%m/%d', suffix='%H%M%S', formatter='[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s',file_size=128, encoding='utf-8', config=None):
    now = time.localtime()
    
    folder = '{}/{}'.format(config and config.get('log','path')or path, time.strftime(config and config.get('log','prefix')or prefix, now))
    filename = '{}.{}.log'.format(logger.name, time.strftime(config and config.get('log','suffix')or suffix, now))
    logger_formatter = logging.Formatter(config and config.get('log','formatter')or formatter)
    
    if not os.path.exists(folder):
        os.makedirs(folder)

    # MB 기준
    fileMaxByte = 1024 * 1024 * (config and int(config.get('log','file.size')) or file_size)
    fileHandler = logging.handlers.RotatingFileHandler(filename='{}/{}'.format(folder, filename), maxBytes=fileMaxByte, backupCount=10, encoding=config and config.get('log','encoding')or encoding)
    streamHandler = logging.StreamHandler()

    fileHandler.setFormatter(logger_formatter)
    streamHandler.setFormatter(logger_formatter)
    
    logger.setLevel(level)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)
    return logger
