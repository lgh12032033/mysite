#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :fds.py
# @Time      :2023/1/30 10:30
# @Author    :liuguanghong

from app import app
import json
from app.models.std import *
from fastapi.responses import JSONResponse, Response
from app.db import sql_crud
import math
from utils import load_yaml

yml = load_yaml("conf/conf.yml")
token = yml["token"]
username = str(yml["admin"])
password = str(yml["password"])

r = "/fds/"


@app.post(f"{r}update_info")
def update_info(info: Info):  # 修改主站信息
    with open("app/static/site_info.json", "w", encoding="utf8") as f:
        json.dump(info.dict(), f)
    return {"mesg": "ok", "code": 200}


@app.post("/login")
def login(loginItem: LoginItem):  # 登录接口
    response = {}
    if loginItem.username == username and loginItem.password == password:
        response = {"mesg": "ok", "token": token, "code": 0}
        # response.set_cookie("token", token)
    elif loginItem.username != username:
        response = {"mesg": "用户名错误", "code": -1}
    elif loginItem.password != password:
        response = {"mesg": "密码错误", "code": -2}
    response_ = JSONResponse(response)
    if response.get("code") == 0:
        response_.set_cookie("token", token)
    return response_


@app.get(r + "cst")  # 获取最新的访问统计总量
def cst():
    return sql_crud.cst()


@app.get(r + "visiter_list/{page}")  # 获取访客列表
def visiter_list(page: int = 1):
    if page < 0:
        return Response(status_code=403)
    total, item = sql_crud.visiter_list(page)
    return {"total": math.ceil(total / 20), "page": page, "data": item}


@app.get(r + "create_flag/{flag}")
def create_flag(flag: str):  # 创建标签
    if sql_crud.create_flag(flag):
        return {"mesg": "ok", "code": 206}
    else:
        return {"mesg": "ok", "code": 200}
