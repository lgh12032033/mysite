#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :gunicorn.py
# @Time      :2023/1/20 16:11
# @Author    :liuguanghong

from app import pro_conf

# 设置守护进程
daemon = True
# 监听内网端口8000
bind = f'{pro_conf.host}:{pro_conf.port}'
# 设置进程文件目录
pidfile = '/var/run/gunicorn.pid'
chdir = '/root/web'  # 工作目录
# 工作模式
worker_class = 'uvicorn.workers.UvicornWorker'
# 并行工作进程数 核心数*2+1个
workers = pro_conf.workers  # multiprocessing.cpu_count()+1
# 指定每个工作者的线程数
threads = pro_conf.threads
# 设置最大并发量
worker_connections = pro_conf.worker_connections
loglevel = 'info'  # 错误日志的日志级别
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
# 设置访问日志和错误信息日志路径
accesslog = "./run_log/gunicorn_access.log"
errorlog = "./run_log/gunicorn_error.log"
