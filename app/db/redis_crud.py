#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :redis_crud.py
# @Time      :2023/1/30 11:35
# @Author    :liuguanghong
import logging

from .get_db import get_redis_session


def visiter(ip):
    redis = get_redis_session()
    pipeline = redis.pipeline()
    try:
        pipeline.watch(ip)
        pipeline.multi()
        if not redis.get(ip):
            pipeline.set(ip, 1, ex=3600 * 24)
        pipeline.execute()
    except Exception as e:
        logging.error(e)
    finally:
        pipeline.reset()
#
def query_ip(ip):
    redis = get_redis_session()
    return redis.get(ip)
