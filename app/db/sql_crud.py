#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :sql_crud.py
# @Time      :2023/1/30 11:14
# @Author    :liuguanghong
import logging

from .get_db import get_sql_session
from datetime import date
from app.models.std import *
from app.models.model import *


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
