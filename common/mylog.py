# coding=utf-8
"""
@author: beyourself
@time: 2017/10/4 11:59
"""

import logging
import re
import time
from common import config
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler

formatter = logging.Formatter('%(asctime)s %(filename)s:%(lineno)d %(levelname)-8s %(message)s')


def get_maxsize_logger(log_file='restful.log'):
    global formatter
    log_obj = logging.getLogger('Restful')

    Rthandler = RotatingFileHandler(filename=config.log_path + log_file,
                                    maxBytes=20 * 1024 * 1024, backupCount=20)
    Rthandler.setFormatter(formatter)
    log_obj.addHandler(Rthandler)

    log_obj.setLevel(logging.DEBUG)

    return log_obj


def get_roll_logger(log_file='restful_roll.log'):
    TimeRthandler = TimedRotatingFileHandler(filename=config.log_path + log_file, when="d", interval=1, backupCount=3)
    TimeRthandler.suffix = "%Y%m%d"
    TimeRthandler.extMatch = re.compile(r"^\d{4}\d{2}\d{2}$")
    formatter = logging.Formatter('%(asctime)s %(filename)s:%(lineno)d %(levelname)-8s %(message)s')
    TimeRthandler.setFormatter(formatter)
    log_obj = logging.getLogger('Restful_roll')
    log_obj.addHandler(TimeRthandler)
    log_obj.setLevel(logging.DEBUG)
    return log_obj


if __name__ == '__main__':
    logger = get_roll_logger()
    logger.error('test error')
    logger.info('test_info')
    i = 0
    while True:
        if i > 100:
            break
        logger.debug("test log roll %d", i)
        logger.info('test_info')
        i += 1
        time.sleep(0.1)
