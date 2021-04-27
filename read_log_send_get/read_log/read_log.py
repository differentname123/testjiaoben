# coding=utf-8
import json
import sys
import time

from common.cmopare import visitURL, httpGet

HEAD = "http://"
MACHINE1 = "127.0.0.1:8514"
MACHINE2 = "testgrowth.busi.inkept.cn"


# 通过一条日志信息originStr ， 提取相应的请求 分别打向两台机器 并返回响应值
def compare(originStr, machine1, machine2):

    request1 = buildRequest(originStr, HEAD, machine1)
    request2 = buildRequest(originStr, HEAD, machine2)
    if request2 == "":
        return "", ""
    resp1 = httpGet(request1)
    resp2 = httpGet(request2)
    print resp1
    print resp2
    return resp1, resp2


# 解析日志数据 生成 请求
def buildRequest(originStr, head, machine):
    method = getValue(originStr, 'req_method')
    request = ""
    if method == 'GET':
        uri = getValue(originStr, 'req_uri')
        request = head + machine + uri
    return request


# 通过日志 originStr 得到与 uri 相关的名字
def buildPathName(originStr):
    uri = getValue(originStr, 'req_uri')
    temp = uri.split('?')
    if len(temp) > 0:
        temp = temp[0].split('/')
    else:
        return ""
    flag = 0
    path = ''
    for i in temp:
        if i != "":
            flag = flag + 1
            if flag == 1:
                path += str(i)
            else:
                path += '_' + str(i)
    return path


# 通过 日志信息 获取指定key的对应值
def getValue(originStr, key):
    dictData = json.loads(originStr)
    return dictData.get(key)


def save_data(line, filepath):
    with open(filepath, 'a') as f:
        f.write(line + '\n')


def saveLog(httpresp1, httpresp2, path, machine1, machine2):
    if httpresp1 == "" or httpresp2 == "":
        return 0
    flag1 = 1
    reload(sys)
    sys.setdefaultencoding('utf8')
    result = httpresp1 == httpresp2
    if httpresp1['dm_error'] != 0 or httpresp2['dm_error'] != 0 or result == False:
        flag1 = 0
    nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    logmessage = "\n" + str(nowTime) + "  " + str(result) + "\n" + str(machine1) + str(":") + str(
        httpresp1) + "\n" + str(
        machine2) + str(":") + str(httpresp2) + "\n"
    logmessage = logmessage.decode("unicode-escape")
    save_data(logmessage, sys.path[0] + "/" + path + '.log')
    if flag1 == 0:
        save_data(logmessage, sys.path[0] + "/" + path + '.error')


def ReadLogAndGet(logName, machine1, machine2):
    path = sys.path[0] + "/" + logName
    file = open(path, 'r')
    try:
        while True:
            text_line = file.readline()
            if text_line:
                path = buildPathName(text_line)
                result1, result2 = compare(text_line, machine1, machine2)
                saveLog(result1, result2, path, machine1, machine2)
                print(text_line)
            else:
                break
    finally:
        file.close()


if __name__ == '__main__':
    ReadLogAndGet('access-2021042615.log', MACHINE1, MACHINE2)
