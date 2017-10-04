# coding=utf-8
"""
@author: beyourself
@time: 2017/10/4 11:59
"""

import logging
import os
import re
import time
import simplejson as json
import datetime
from common import config, date_tools
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler

formatter = logging.Formatter('%(asctime)s %(filename)s:%(lineno)d %(levelname)-8s %(message)s')


def get_maxsize_logger(log_file='restful.log'):
    global formatter
    log_obj = logging.getLogger('Restful')

    filename = os.path.join(config.log_path, log_file)
    with open(filename, 'a'):
        pass

    Rthandler = RotatingFileHandler(filename=filename,
                                    maxBytes=20 * 1024 * 1024, backupCount=20)
    Rthandler.setFormatter(formatter)
    log_obj.addHandler(Rthandler)

    log_obj.setLevel(logging.DEBUG)

    return log_obj


def get_roll_logger(log_file='restful_roll.log'):
    filename = os.path.join(config.log_path, log_file)
    with open(filename, 'a'):
        pass

    TimeRthandler = TimedRotatingFileHandler(filename=filename, when="d", interval=1, backupCount=3)
    TimeRthandler.suffix = "%Y%m%d"
    TimeRthandler.extMatch = re.compile(r"^\d{4}\d{2}\d{2}$")
    formatter = logging.Formatter('%(asctime)s %(filename)s:%(lineno)d %(levelname)-8s %(message)s')
    TimeRthandler.setFormatter(formatter)
    log_obj = logging.getLogger('Restful_roll')
    log_obj.addHandler(TimeRthandler)
    log_obj.setLevel(logging.DEBUG)
    return log_obj


logger = get_roll_logger()


def is_stamp(stamp):
    if not isinstance(stamp, int):
        return False
    s = int(time.mktime(datetime.date(2017, 1, 1).timetuple()))  # 1483200000
    e = int(time.mktime(datetime.date(2117, 12, 30).timetuple()))  # 1609257600
    if s <= stamp <= e:
        return True
    else:
        return False


def dict2log(dic):
    if not isinstance(dic, dict):
        return None
    js = {}
    for k, v in dic.items():
        if 'time' in str(k) and is_stamp(v):
            js[k] = date_tools.stamp2datetime(v)
        else:
            js[k] = v
    return json.dumps(js, encoding='UTF-8', ensure_ascii=False, indent=2)


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
