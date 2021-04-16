# -*- coding:utf-8 -*-

import sys, os
import json
import urllib2


def httpGet(url):
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    response = res_data.read()
    return json.loads(response)


def httpPost(url, data):
    request = urllib2.Request(url, data=data)
    request.add_header('Content-Type', 'application/json')
    res_data = urllib2.urlopen(request, json.dumps(data))
    response = res_data.read()
    return json.loads(response)


def save_data(line, filepath):
    with open(filepath, 'a') as f:
        f.write(line + '\n')


def getLocalLogid(uri):
    url = 'http://localhost:9998/api/v2/base/abtest/logid?' + uri
    resp = httpGet(url)
    if resp['dm_error'] != 0:
        return ''
    return resp['data']['logid']


def getLogid(uri):
    # url = 'http://ali-e-bpc-gtd-gray01.bj:9998/api/v2/base/abtest/logid?' + uri
    url = 'http://ali-e-bpc-gtd-gray01.bj:9998/api/v2/base/abtest/logid?' + uri
    resp = httpGet(url)
    if resp['dm_error'] != 0:
        return ''
    return resp['data']['logid']


def diffLogid(logid1, logid2):
    # print 'logid1:', logid1
    # print 'logid2:', logid2
    set1 = set(logid1.split(','))
    # setd = {'200101','200102','200190','200191','200192','200701','200801','200901'}
    # setd.update({'202801','202802','202803','202804','202805','202806','202807','202808','202809'})
    # setd.update({'202901','202902','203001','203002','203301','203401','203402','203403','203404','203701','203702'})
    # set1 = set1- setd
    set2 = set(logid2.split(','))
    result = list(set1.symmetric_difference(set2))
    result = map(int, result)
    result.sort()
    return result


def deal(line):
    # if 'uid=0' in line :
    #     print 'IGNORE', line
    #     return
    # item = line.split()
    # if len(item) < 14:
    #     print 'ERROR len(item) < 14'
    #     return
    # date = item[0]
    # time = item[1]
    # uri0 = item[3]
    # host = item[4]
    # code = item[5]
    # resp = item[8]
    p1 = json.loads(line)
    m = p1["req_method"]
    if m != "GET":
        return
    respBody = p1["resp_body"].replace("\\n", "")
    # print respBody
    # body = json.loads(respBody)
    # body1 = json.loads(body)
    # logid1 = body1["data"]["logid"]
    uri0 = p1["req_uri"]
    if uri0.find("logid_batch") > 0:
        return

    buf = uri0.split('?')
    if len(buf) < 2:
        print
        'ERROR len(buf) < 2'
        return
    uri = buf[1]
    print
    uri
    date = p1["time"]
    # resp = json.loads(resp.decode('string_escape').strip('" '))
    # if resp['dm_error'] != 0:
    #     print 'ERROR resp["dm_error"] != 0'
    #     return
    # logid1 = resp['response']
    if len(uri) == 0:
        return
    logid1 = getLocalLogid(uri)
    logid2 = getLogid(uri)

    result = diffLogid(logid1, logid2)
    if result == None or len(result) == 0:
        l = '%s %s %s %s %s' % (date, 'SUCCESS', 'N', logid1, uri)
    else:

        l = '%s %s %s %s %s %s' % (date, 'FAILED', ','.join(map(str, result)), logid1, logid2, uri)
    save_data(l, 'compare_result.log')


def main():
    param = sys.argv[1:]
    if len(param) == 0:
        return
    line = param[0]
    deal(line)


if __name__ == "__main__":
    main()
