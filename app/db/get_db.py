#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :get_db.py
# @Time      :2023/1/28 16:33
# @Author    :liuguanghong

from utils import load_db
from pymongo import MongoClient
import redis
from sqlalchemy.orm import Session

db_dic = {}
db_dic["redis"], db_dic["mongo"], db_dic["sql"] = load_db()

def get_sql_session() -> Session:
    return db_dic["sql"]()


def get_redis_session() -> redis.Redis:
    return redis.Redis(connection_pool=db_dic["redis"])


def get_mongo_session() -> MongoClient:
    return db_dic["mongo"]


if __name__ == '__main__':
    client = get_redis_session()
    client.set("test","test20230128")
