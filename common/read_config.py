# coding=utf-8
import random

import configparser

import sys

INTTYPE = u'"int"'
STRINGTYPE = u'"string"'
FIXEDTYPE = u'"fixed"'
LISTTYPE = u'"list"'

RANDRATE = 10


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


def NecessaryProduceParam(paramName, paramType, paramRange):
    result = ""
    value = ""
    result += paramName
    # paramType = str(paramType)+""
    if paramType == INTTYPE:
        value = str(ProduceInt(paramRange))
    elif paramType == FIXEDTYPE:
        value = ProduceFix(paramRange)
    elif paramType == LISTTYPE:
        value = ProduceList(paramRange)
    elif paramType == STRINGTYPE:
        value = ProduceString(paramRange)

    result += "=" + str(value)

    return result


def UnnecessaryProduceParam(paramName, paramType, paramRange):
    result = ""
    value = ""
    result += paramName
    temp = random.randint(0, 100)
    if temp < RANDRATE:
        if paramType == INTTYPE:
            value = str(ProduceInt(paramRange))
        elif paramType == FIXEDTYPE:
            value = ProduceFix(paramRange)
        elif paramType == LISTTYPE:
            value = ProduceList(paramRange)
        elif paramType == STRINGTYPE:
            value = ProduceString(paramRange)

    result += "=" + str(value)

    return result


def readandset(param_config, rate):
    # 改变机率
    global RANDRATE
    RANDRATE = int(rate)
    result = ""
    flag = 0
    temp = ""
    temp1 = ""
    cf = configparser.ConfigParser()
    cf.read(sys.path[0] + "/" + param_config)  # 拼接得到config.ini文件的路径，直接使用

    params = cf.sections()

    for param in params:
        flag = flag + 1
        paramType = cf.get(param, "type")
        paramRange = cf.get(param, "range")
        is_necessary = cf.get(param, "is_necessary")
        if is_necessary == u'1':
            temp = NecessaryProduceParam(param, paramType, paramRange)
        else:
            temp = UnnecessaryProduceParam(param, paramType, paramRange)

        if flag != 1:
            result += '&' + temp
        else:
            result += temp

    return result


def read(param_config):
    RANDRATE = 10
    result = ""
    flag = 0
    temp = ""
    temp1 = ""
    cf = configparser.ConfigParser()
    cf.read(sys.path[0] + "/" + param_config)  # 拼接得到config.ini文件的路径，直接使用

    params = cf.sections()

    for param in params:
        flag = flag + 1
        paramType = cf.get(param, "type")
        paramRange = cf.get(param, "range")
        is_necessary = cf.get(param, "is_necessary")
        if is_necessary == u'1':
            temp = NecessaryProduceParam(param, paramType, paramRange)
        else:
            temp = UnnecessaryProduceParam(param, paramType, paramRange)

        if flag != 1:
            result += '&' + temp
        else:
            result += temp

        # print(temp + "\n")

    # print("\n" + result)
    return result


if __name__ == '__main__':
    read()
