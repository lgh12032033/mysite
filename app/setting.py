#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :setting.py
# @Time      :2023/1/20 13:49
# @Author    :liuguanghong


# 配置
import multiprocessing


class BaseConfig:
    host = "127.0.0.1"
    port = 8000
    title = "BaseConfig"
    description = "BaseConfig Test"
    Version = "test.v1"
    isdebug = False


class DebuggerConfig(BaseConfig):
    isdebug = True


class ProductionConfig(DebuggerConfig):
    isdebug = False
    workers = multiprocessing.cpu_count() * 2 + 1  # 并行工作进程数 核心数*2+1个
    threads = 2  # 指定每个工作者的线程数
    worker_connections = 2000  # 设置最大并发量



# 在此处切换配置
# pro_conf = DebuggerConfig
pro_conf = ProductionConfig
