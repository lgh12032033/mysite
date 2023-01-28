#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :yaml_load.py
# @Time      :2023/1/28 15:37
# @Author    :liuguanghong


import yaml


def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
    return result

