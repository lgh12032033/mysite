#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :indextest.py
# @Time      :2023/1/20 14:13
# @Author    :liuguanghong

from app import app


@app.get("/")
def index():
    return {"msg": "hello ok"}


