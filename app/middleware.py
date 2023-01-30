#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :middleware.py
# @Time      :2023/1/20 13:53
# @Author    :liuguanghong
import logging
import time

token = "xxxx"
# 中间件
from app import app
from fastapi import  Request, Response
from .models.std import Visiter
from datetime import datetime
from .db import sql_crud,redis_crud


@app.middleware("http")
async def token_verify(request: Request, call_next) -> Response:
    # 后台权限拦截中间件
    if "/fds/" in request.url.path:
        if token != request.headers.get("token"):
            return Response(status_code=403)
    response = await call_next(request)
    return response


@app.middleware("http")
async def doorman(request: Request, call_next) -> Response:
    # 门童负责记录访客
    response = await call_next(request)
    visiter_dic = {"visit_method": request.method,
                   "visit_route": request.url.path,
                   "visit_ip": request.client.host,
                   "visit_code": response.status_code,
                   "visit_time": datetime.fromtimestamp(int(time.time()))}
    v = Visiter(**visiter_dic)
    sql_crud.visit_log(v)
    if not redis_crud.query_ip(v.visit_ip):
        sql_crud.visit_total_log()
        redis_crud.visiter(v.visit_ip)
    return response
