#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :index.py
# @Time      :2023/1/20 14:13
# @Author    :liuguanghong

from app import app
import json


#
# @app.get("/")
# def index():
#     return {"msg": "hello ok"}


@app.get("/info")
def info():
    with open("app/static/site_info.json", "r",encoding="utf8") as f:
        dic = json.load(f)
    return dic

