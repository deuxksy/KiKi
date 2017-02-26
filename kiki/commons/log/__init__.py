import logging.handlers
import os
import time


def get_logger(logger, level=logging.DEBUG, path='../log', prefix='%Y/%m/%d', suffix='%H%M%S',
               formatter='[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s', file_size=128,
               encoding='utf-8', config=None):
    now = time.localtime()

    folder = '{}/{}'.format(config and config['log']['path'] or path,
                            time.strftime(config and config['log']['prefix'] or prefix, now))
    filename = '{}.{}.log'.format(logger.name, time.strftime(config and config['log']['suffix'] or suffix, now))
    logger_formatter = logging.Formatter(config and config['log']['formatter'] or formatter)

    if not os.path.exists(folder):
        os.makedirs(folder)

    # MB 기준
    fileMaxByte = 1024 * 1024 * (config and int(config['log']['file_size']) or file_size)
    fileHandler = logging.handlers.RotatingFileHandler(filename='{}/{}'.format(folder, filename), maxBytes=fileMaxByte,
                                                       backupCount=10,
                                                       encoding=config and config['log']['encoding'] or encoding)
    streamHandler = logging.StreamHandler()

    fileHandler.setFormatter(logger_formatter)
    streamHandler.setFormatter(logger_formatter)

    logger.setLevel(level)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)
    return logger
