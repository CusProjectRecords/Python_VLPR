# -*- coding: utf-8 -*-


# 用于中间环节对数据的传递
class GlobalVar:
    name = None


def set_name(name):
    GlobalVar.name = name


def get_name():
    return GlobalVar.name
