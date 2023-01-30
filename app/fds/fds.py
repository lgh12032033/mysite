#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :fds.py
# @Time      :2023/1/30 10:30
# @Author    :liuguanghong

from app import app
import json
from app.models.std import *
from fastapi import Response

r = "/fds/"


@app.post(f"{r}update_info")
def update_info(info: Info):
    with open("app/static/site_info.json", "w", encoding="utf8") as f:
        json.dump(info.dict(), f)
    return {"mesg": "ok", "code": 200}


@app.get(f"/login")
def login():
    return "ok"
