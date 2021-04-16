# coding=utf-8
import json
import urllib2

import read_config

HEAD = "http://"
MACHINE1 = "127.0.0.1:8514"
MACHINE2 = "testgrowth.busi.inkept.cn"
API = "/api/push/template/list"


def httpGet(url):
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    response = res_data.read()
    return json.loads(response)


def buildURI(api, params):
    return api + "?" + params


def visitURL(name, uri):
    url = HEAD + name + uri
    resp = httpGet(url)
    return resp


def save_data(line, filepath):
    with open(filepath, 'a') as f:
        f.write(line + '\n')


def compareResult(machine1, machine2):
    params = read_config.read()
    uri = buildURI(API, params)
    httpresp1 = visitURL(machine1, uri)
    httpresp2 = visitURL(machine2, uri)
    result = httpresp1 == httpresp2
    logmessage = "\n" + str(result) + " " + str(uri) + "\n" + str(machine1) + ":" + str(httpresp1) + "\n" + str(
        machine2) + ":" + str(httpresp2) + "\n"
    # print(logmessage)

    save_data(logmessage, 'compare_result.log')
    return result


def test():
    result = compareResult(MACHINE1, MACHINE2)
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(10):
        test()
