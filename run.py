# coding=utf-8
"""
@author: beyourself
@time: 2017/10/3 14:10
"""

import sys
from app.app import app
from common import config

if __name__ == '__main__':
    app.run(debug=True, port=config.PORT)
