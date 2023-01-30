#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :index.py
# @Time      :2023/1/20 14:13
# @Author    :liuguanghong

from app import app
import json
from app.db import sql_crud

#
# @app.get("/")
# def index():
#     return {"msg": "hello ok"}


@app.get("/info")
def info():
    with open("app/static/site_info.json", "r", encoding="utf8") as f:
        dic = json.load(f)
    return dic


@app.get("/flags/{flag_id}")
def flags(flag_id: str):
    ids = flag_id.split("_")
    flags_list = sql_crud.get_flags(ids)
    return flags_list
