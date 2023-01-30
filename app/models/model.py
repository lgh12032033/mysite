#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :model.py
# @Time      :2023/1/29 10:56
# @Author    :liuguanghong

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Date, DateTime, String, Text

# declarative base class
Base = declarative_base()


class CST(Base):
    # 累计统计表
    __tablename__ = "cumulative_statistics_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    totady_visit = Column(Integer, default=0)
    total_visit = Column(Integer, default=0)


class Visiters(Base):
    # 访客表
    __tablename__ = "visiters"
    id = Column(Integer, primary_key=True, autoincrement=True)
    visit_time = Column(DateTime)
    visit_ip = Column(String(30))
    visit_route = Column(String(200))
    visit_method = Column(String(10))
    visit_code = Column(Integer)


class ALT(Base):
    # 后台登录表
    __tablename__ = "admin_login_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    login_time = Column(DateTime)
    login_ip = Column(String(30))


class BaseContent:
    id = Column(Integer, primary_key=True, autoincrement=True)
    content_id = Column(String(200), index=True, unique=True)
    title = Column(String(200))
    flag_id = Column(String(200))
    push_time = Column(DateTime)
    visit_count = Column(Integer, default=0)
    visit_like = Column(Integer, default=0)
    visit_comment = Column(Integer, default=0)


class Blogs(Base, BaseContent):
    __tablename__ = "blogs"
    profile = Column(String(200))


class Note(Base, BaseContent):
    __tablename__ = "notes"


class Vedio(Base, BaseContent):
    __tablename__ = "vedios"


class Flag(Base):
    __tablename__ = "flags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200))
    createtime = Column(DateTime)


class Comment(Base):
    __tablename__ = "Comment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content_id = Column(String(200), index=True)
    parent_id = Column(Integer, nullable=True)
    pusher_nick = Column(String(200))
    pusher_email = Column(String(200))
    pusher_host = Column(String(200), nullable=True)
    push_time = Column(DateTime)
    comment_content = Column(Text)
