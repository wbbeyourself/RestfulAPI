# coding=utf-8
"""
@author: beyourself
@time: 2017/10/3 14:10
"""

import sys
from app.app import app

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(0)
    port = int(sys.argv[1])
    app.run(debug=True, port=port)
