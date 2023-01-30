#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :sql_crud.py
# @Time      :2023/1/30 11:14
# @Author    :liuguanghong
import logging
import time

from .get_db import get_sql_session
from datetime import date
from app.models.std import *
from app.models.model import *
import math


def visit_log(visiter: Visiter):
    session = get_sql_session()
    try:
        session.add(Visiters(**visiter.dict()))
        session.commit()
    except Exception as e:
        logging.error(e)
        session.rollback()


#
def visit_total_log():
    session = get_sql_session()
    ret = session.query(CST).filter(CST.date == date.today()).first()
    ret.totady_visit += 1
    ret.total_visit += 1
    session.commit()


def login_log(ip, code):
    session = get_sql_session()
    try:
        alt = ALT()
        alt.login_ip = ip
        alt.code = code
        alt.login_time = datetime.fromtimestamp(time.time())
        session.add(alt)
        session.commit()
    except Exception as e:
        logging.error(e)
        session.rollback()


def create_flag(flag):
    session = get_sql_session()
    try:
        if session.query(Flag).filter(Flag.title == flag).first():
            return True
        else:
            _flag = Flag()
            _flag.title = flag
            _flag.createtime = datetime.fromtimestamp(time.time())
            session.add(_flag)
            session.commit()
    except Exception as e:
        logging.error(e)
        session.rollback()


def get_flags(ids):
    session = get_sql_session()
    rets = session.query(Flag).filter(Flag.id.in_(ids)).all()
    return rets


def cst():
    session = get_sql_session()
    return session.query(CST).order_by(CST.date.desc()).first()


def visiter_list(page):
    session = get_sql_session()
    total = session.query(Visiters).count()
    if math.ceil(total / 20) <= page:
        return total, session.query(Visiters).order_by(Visiters.visit_time.desc()).limit(
            20).offset((page - 1) * 20).all()
    else:
        return total, []
