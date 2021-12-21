# -*- coding: utf-8 -*-

# 用于中间环节对数据的传递

class GlobalName:
    name = None


def set_name(name):
    GlobalName.name = name


def get_name():
    return GlobalName.name
