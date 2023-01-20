#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2023/1/20 13:48
# @Author    :liuguanghong


# 启动文件
import os
import sys

from app import *
from uvicorn import run


def main():
    if pro_conf.isdebug:
        run("app.app:app", host=pro_conf.host, port=pro_conf.port, reload=True)
    elif sys.platform == "win32" or sys.platform == "cygwin":
        run("app.app:app",host=pro_conf.host,port=pro_conf.port,workers=pro_conf.workers,limit_concurrency=pro_conf.worker_connections)
    else:
        os.system("gunicorn app.app:app -c gunicorn.py")



if __name__ == '__main__':
    main()
