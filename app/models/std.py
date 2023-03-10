#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :std.py
# @Time      :2023/1/30 11:00
# @Author    :liuguanghong

# 标准化模型

from pydantic import BaseModel
from datetime import datetime


class Visiter(BaseModel):
    visit_time: datetime
    visit_ip: str
    visit_route: str
    visit_method: str
    visit_code: int


class Link(BaseModel):
    title: str
    link: str


class Info(BaseModel):
    host: str
    info: str
    email: str
    friends: list[Link]
    bookmarks: list[Link]
    others: list[Link]
    pays: list[Link]

class LoginItem(BaseModel):
    username:str
    password:str