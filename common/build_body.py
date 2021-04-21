# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import urllib2
# coding=utf-8
import random

import configparser

import sys

INTTYPE = u'"int"'
STRINGTYPE = u'"string"'
FIXEDTYPE = u'"fixed"'
LISTTYPE = u'"list"'

RANDRATE = 10


class paramStruct:  # 定义一个类people
    def __init__(self):
        self.type = ""
        self.range = 0
        self.is_necessary = ""
        self.is_wrap = ""
        self.param = ""


def ProduceString(paramRange):
    result = ""
    maxsize = int(paramRange)
    size = random.randint(1, maxsize)
    temp = random.sample('qwertyuiopasdfghjklzxcvbnm', size)
    for ch in temp:
        result += ch
    return result


def ProduceList(paramRange):
    temp = paramRange.split("-")
    index = random.randint(0, len(temp) - 1)
    return temp[index]


def wrap(paramRange):
    return "\"" + paramRange + "\""


def ProduceFix(paramRange):
    return paramRange


def ProduceInt(paramRange):
    result = 1
    start, end = paramRange.split("-")
    start = int(start)
    end = int(end)
    result = random.randint(start, end)
    # print(result)

    return result


def dealParam(paramstruct):
    value = ""
    flag = 0
    paramName = paramstruct.param
    paramType = paramstruct.type
    paramRange = paramstruct.range
    is_wrap = paramstruct.is_wrap

    result = wrap(paramName)
    if paramstruct.is_necessary == u'1':
        flag = 1
    else:
        temp = random.randint(0, 100)
        if temp < RANDRATE:
            flag = 1

    if flag == 1:
        if paramType == INTTYPE:
            value = str(ProduceInt(paramRange))
        elif paramType == FIXEDTYPE:
            value = ProduceFix(paramRange)
        elif paramType == LISTTYPE:
            value = ProduceList(paramRange)
        elif paramType == STRINGTYPE:
            value = ProduceString(paramRange)

    if is_wrap == u'1':
        value = wrap(value)
    result += ":" + str(value)

    return result


def readbody(param_config):
    paramstruct = paramStruct
    result = ""
    flag = 0
    cf = configparser.ConfigParser()
    cf.read(sys.path[0] + "/" + param_config)  # 拼接得到config.ini文件的路径，直接使用

    params = cf.sections()

    for param in params:
        flag = flag + 1
        # 解析每一个参数并放入相应的类
        paramstruct.param = param
        paramstruct.type = cf.get(param, "type")
        paramstruct.range = cf.get(param, "range")
        paramstruct.is_necessary = cf.get(param, "is_necessary")
        paramstruct.is_wrap = cf.get(param, "is_wrap")

        # 得到这个参数条件下的参数表达式
        temp = dealParam(paramstruct)
        if flag != 1:
            result += ',' + temp
        else:
            result += temp

    return result


if __name__ == '__main__':
    print(readbody('template_save.ini'))
