#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :fds.py
# @Time      :2023/1/30 10:30
# @Author    :liuguanghong

from app import app
import json

r = "/fds/"

@app.get(f"{r}addTest")
def addTest():
    return "ok"

