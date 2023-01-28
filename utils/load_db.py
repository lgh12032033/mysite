#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :load_db.py
# @Time      :2023/1/28 15:40
# @Author    :liuguanghong

from utils import load_yaml
import redis
from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def load_db() -> (redis.ConnectionPool, MongoClient, Session):
    conf = load_yaml("../../conf/conf.yml")
    database = conf["database"]
    redis_conf = database["redis"]
    mongo_conf = database["mongo"]
    mysql_conf = database["mysql"]
    redis_pool = redis.ConnectionPool(host=redis_conf["host"], port=redis_conf["port"],
                                      decode_responses=True)
    mongo_clients = MongoClient(mongo_conf["host"], mongo_conf["port"], maxPoolSize=200)
    engine = create_engine(
        f'mysql+pymysql://{mysql_conf["username"]}:{mysql_conf["password"]}@{mysql_conf["host"]}/{mysql_conf["db"]}',
        echo=True)
    Session = sessionmaker(bind=engine)
    return redis_pool, mongo_clients, Session
