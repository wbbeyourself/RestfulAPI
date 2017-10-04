# coding=utf-8
"""
@author: beyourself
@time: 2017/10/4 13:31
"""

import functools
import time

from common import mylog

_inc = 0


def call_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        global _inc
        _inc += 1
        l0, t0 = _inc, time.time()
        logger = mylog.logger
        logger.info('')
        logger.info('')
        logger.info('------------------[%s]--begin---------------------', func.__name__)
        logger.info('call[%s] bgn %s with \n%s\n%s' % (l0, func.__name__, args, mylog.dict2log(kw)))
        r = func(*args, **kw)
        result = mylog.dict2log(r) if isinstance(r, dict) else r
        logger.info('call[%s] end %s using %sms with \n%s'
                    % (l0, func.__name__, int((time.time() - t0) * 1000), result))
        logger.info('------------------[%s]--end---------------------', func.__name__)
        logger.info('')
        logger.info('')
        return r

    return wrapper


# 检查必备参数是否都在names中，都有的话返回'',否则返回缺少的第一个参数名
def check(required_args, names):
    for arg in required_args:
        if arg not in names:
            return arg
    return ''


# 必备参数检查，args_tuple中为必备的参数，如果没有,ret为-1，从此不用重复写参数校验代码了
def args_required(*args_tuple):
    def wrapper1(func):
        @functools.wraps(func)
        def wrapper2(*args, **kwargs):
            if kwargs:
                missed = check(args_tuple, kwargs.keys())
                if missed:
                    return {'ret': -1, 'err': 'missing %s' % missed}
            else:  # 其他情况，不做处理
                return func(*args, **kwargs)

        return wrapper2

    return wrapper1


if __name__ == '__main__':
    pass
