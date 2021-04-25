# coding=utf-8
import json
import sys
import time
import urllib2

from common import read_config, build_body
from common.build_query import produce, repalceValue, mergeRequestBody
from common.read_config import readandset

HEAD = "http://"
MACHINE1 = "127.0.0.1:8514"
MACHINE2 = "testgrowth.busi.inkept.cn"
API = "/api/push/template/list"
CONFIGNAME = "template_list_config.ini"


# 向一台机器发送一个post请求 并输出日志和返回日志和结果
def PostSingle(body_config_name, config_name, api, machine1, ):
    flag1 = 1
    params = read_config.readandset(config_name, 10)
    body1 = build_body.readbody(body_config_name)

    body = '{' + body1 + '}'

    uri = buildURI(api, params)
    path = ""
    flag = 0
    httpresp1 = visitBodyURL(machine1, body, uri)
    result = True
    if httpresp1['dm_error'] != 0 or result == False:
        flag1 = 0
    temp = api.split('/')
    for i in temp:
        if i != "":
            flag = flag + 1
            if flag == 1:
                path += str(i)
            else:
                path += '_' + str(i)
    nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    logmessage = "\n" + str(nowTime) + "  " + str(result) + " " + str(uri) + "\n" + str(body) + "\n" + str(
        machine1) + ":" + str(
        httpresp1) + "\n"
    save_data(logmessage, sys.path[0] + "/" + path + '.log')
    if flag1 == 0:
        save_data(logmessage, sys.path[0] + "/" + path + '.error')
    return flag1, logmessage, params, body1


# 向一台机器发送一个post请求 并输出日志和返回日志和结果
def SinglePost(body, config_name, api, machine1, ):
    flag1 = 1
    qiuqiuni = u""
    body = qiuqiuni + '{' + body + '}'
    params = read_config.readandset(config_name, 10)
    uri = buildURI(api, params)
    path = ""
    flag = 0
    httpresp1 = visitBodyURL(machine1, body, uri)
    result = True
    if httpresp1['dm_error'] != 0 or result == False:
        flag1 = 0
    temp = api.split('/')
    for i in temp:
        if i != "":
            flag = flag + 1
            if flag == 1:
                path += str(i)
            else:
                path += '_' + str(i)
    nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    logmessage = "\n" + str(nowTime) + "  " + str(result) + " " + str(uri) + "\n" + str(body) + "\n" + str(
        machine1) + ":" + str(
        httpresp1) + "\n"
    save_data(logmessage, sys.path[0] + "/" + path + '.log')
    if flag1 == 0:
        save_data(logmessage, sys.path[0] + "/" + path + '.error')
    return flag1, logmessage

def PostTotalFun(body_config_name, config_name, api, machine1, machine2, ):
    flag1 = 1
    body = build_body.readbody(body_config_name)
    body = '{' + body + '}'
    params = read_config.readandset(config_name, 10)
    uri = buildURI(api, params)
    path = ""
    flag = 0
    httpresp1 = visitBodyURL(machine1, body, uri)

    httpresp2 = visitBodyURL(machine2, body, uri)

    result = httpresp1 == httpresp2
    if httpresp1['dm_error'] != 0 or httpresp2['dm_error'] != 0 or result == False:
        flag1 = 0
    temp = api.split('/')
    for i in temp:
        if i != "":
            flag = flag + 1
            if flag == 1:
                path += str(i)
            else:
                path += '_' + str(i)
    nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    logmessage = "\n" + str(nowTime) + "  " + str(result) + " " + str(uri) + "\n" + str(body) + "\n" + str(
        machine1) + ":" + str(
        httpresp1) + "\n" + str(
        machine2) + ":" + str(httpresp2) + "\n"
    save_data(logmessage, sys.path[0] + "/" + path + '.log')
    if flag1 == 0:
        save_data(logmessage, sys.path[0] + "/" + path + '.error')
    return result


# 向指定机器machine1的指定api发送一个参数为pamas的get请求  并返回字典类型响应
def singleGet(params, api, machine1):
    flag1 = 1
    uri = buildURI(api, params)
    httpresp1 = visitURL(machine1, uri)
    return httpresp1


# 向两台机器发送一个get请求并做比较
def TotalFun(config_name, api, machine1, machine2, ):
    flag1 = 1
    params = read_config.read(config_name)
    uri = buildURI(api, params)
    path = ""
    flag = 0
    httpresp1 = visitURL(machine1, uri)
    httpresp2 = visitURL(machine2, uri)

    result = httpresp1 == httpresp2
    if httpresp1['dm_error'] != 0 or httpresp2['dm_error'] != 0 or result == False:
        flag1 = 0
    temp = api.split('/')
    for i in temp:
        if i != "":
            flag = flag + 1
            if flag == 1:
                path += str(i)
            else:
                path += '_' + str(i)
    nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    logmessage = "\n" + str(nowTime) + "  " + str(result) + " " + str(uri) + "\n" + str(machine1) + ":" + str(
        httpresp1) + "\n" + str(
        machine2) + ":" + str(httpresp2) + "\n"
    save_data(logmessage, sys.path[0] + "/" + path + '.log')
    if flag1 == 0:
        save_data(logmessage, sys.path[0] + "/" + path + '.error')
    return result


# get访问指定url 并返回json格式的响应
def httpGet(url):
    req = urllib2.Request(url)
    print (url + "\n")
    res_data = urllib2.urlopen(req)
    response = res_data.read()
    return json.loads(response)


# post访问指定url 并返回json格式的响应
def httpPost(url, body):
    req = urllib2.Request(url, body, {'Content-Type': 'application/json'})
    print ('\n' + url)
    print ('body: ' + body + "\n")
    res_data = urllib2.urlopen(req)
    response = res_data.read()
    return json.loads(response)


# 利用api和参数生成uri
def buildURI(api, params):
    return api + "?" + params


def visitBodyURL(name, body, uri):
    url = HEAD + name + uri
    resp = httpPost(url, body)
    return resp


def visitURL(name, uri):
    url = HEAD + name + uri

    resp = httpGet(url)
    return resp


def save_data(line, filepath):
    with open(filepath, 'a') as f:
        f.write(line + '\n')


def testbody():
    body = '{' + build_body.readbody("template_save.ini") + '}'
    params = read_config.read("template_save_config.ini")
    uri = buildURI("/api/push/template/save", params)
    httpresp1 = visitBodyURL(MACHINE1, body, uri)
    print(httpresp1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("cmpare")
