#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :app.py
# @Time      :2023/1/20 13:53
# @Author    :liuguanghong


# 主app

from fastapi import FastAPI
from app.setting import pro_conf
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=pro_conf.title, description=pro_conf.description, version=pro_conf.Version)

origins = [
    "http://api.liugh.cn",
    "https://api.liugh.cn",
    # "https://liugh.cn",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
