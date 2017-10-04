# coding=utf-8
"""
@author: beyourself
@time: 2017/10/4 13:36
"""

import pytz
import calendar
from datetime import date, timedelta, datetime
from time import time

ONE_DAY_IN_SECONDS = 60 * 60 * 24
HOUR_IN_SECONDS = 60 * 60
MINUTE_IN_SECONDS = 60


# Note: the type of arguments (year, mon, day, hour, min and sec)
# in below functions are int


def is_valid_date(date):
    if not isinstance(date, int):
        return False
    if len(str(date)) != 8:
        return False
    year = date / 10000
    month = (date / 100) % 100
    day = date % 100
    if not 1 <= month <= 12:
        return False
    if day == 0:
        return False
    days_of_month = calendar.monthrange(year, month)[1]
    if day > days_of_month:
        return False
    return True


def is_past_date(date):
    """
    return true if the date (20170501) is past date
    """
    return date < stamp2date(time())


def stamp2date(timestamp, time_format='%Y%m%d', tz='Asia/Shanghai'):
    timezone = pytz.timezone(tz)
    return int(datetime.fromtimestamp(timestamp, timezone).strftime(time_format))


# 获取开始结束时间戳之间的天数
def get_date_length(s, e):
    """
    s, e --- int, 20170501 [s, e) 左开右闭
    return --- int, the number of days
    """
    if s >= e:
        return 0
    return (date(e / 10000, (e / 100) % 100, e % 100) - date(s / 10000, (s / 100) % 100, s % 100)).days


def is_date_ok(start_date, end_date):
    """左闭右开区间[start_date, end_date)"""
    # 合法日期检查
    if not is_valid_date(start_date) or not is_valid_date(end_date):
        return False
    if start_date >= end_date or start_date == end_date or is_past_date(start_date):
        return False
    return True


# 获取两个日期之间的时间列表
def get_date_list(start_date, end_date):
    """
    [start_date, end_date) 左开右闭
    20170501
    """
    date_list = []
    s = date(start_date / 10000, (start_date / 100) % 100, start_date % 100)
    e = date(end_date / 10000, (end_date / 100) % 100, end_date % 100)
    if e < s:
        return date_list

    while s < e:
        date_list.append(int(s.strftime('%Y%m%d')))
        s = s + timedelta(days=1)

    return date_list


# 时间戳转日期
def stamp2datetime(stamp, time_format='%Y-%m-%d %H:%M:%S', tz='Asia/Shanghai'):
    """
    :return: the formated datetime string
    """
    timezone = pytz.timezone(tz)
    d = datetime.fromtimestamp(stamp, timezone)
    return d.strftime(time_format)


# 把日期转换为某一天的时间戳(默认零点的时间)
def date2timestamp(date, hour=0, minute=0, second=0, tz='Asia/Shanghai'):
    """
    date --- int, example 20170423
    return --- int, timestamp
    """
    timezone = pytz.timezone(tz)
    dt = datetime(date / 10000, (date / 100) % 100, date % 100, 0, 0, 0)
    sdt = dt - timezone.utcoffset(dt)
    return calendar.timegm(sdt.timetuple()) + hour * HOUR_IN_SECONDS + minute * MINUTE_IN_SECONDS + second


if __name__ == '__main__':
    print(int(time()))
    print(date2timestamp(20170524, hour=14))
