# coding=utf-8

ORIGIN = u'touch_type=2&user_id=&template_type=15&body=&title=o&system_id=58&app_id=9&start_page=1&page_size=13&ticket=STXkNgDuDREBRrqSAIYZDAoQsmkgkwPWETo'
REQUEST = u'app_id=1&ticket=STXkNgDuDREBRrqSAIYZDAoQsmkgkwPWETo&system_id=39'
BODY = u'"app_id":1,"template_title":"if you see this","template_body":"qpaeg","touch_type":1,"template_type":"hlu"'


def repalceBodyValue(body, key, value):
    body = dealBody(body)
    body[key] = value
    body = produceBody(body)
    return body


# 将request格式的key对应的值替换成为value
def repalceValue(origin, key, value):
    origin = dealRequest(origin)
    origin[key] = value
    origin = produceQuary(origin)
    return origin

# 将request格式 增加一个newkey  值为oldKey的值
def addKey(origin, oldKey, newKey):
    origin = dealRequest(origin)
    origin[newKey] = origin.get(oldKey)
    origin = produceQuary(origin)
    return origin

# 将body格式转化为字典  不加加上""
def dealBodyNull(req):
    dic = dict()
    req = req.replace('"', '')
    slicetemp = req.split(',')
    for temp in slicetemp:
        finalslice = temp.split(':')
        if finalslice[1] != "":
            key = finalslice[0]
            value = finalslice[1]
            dic[key] = value
    return dic

# 将body格式转化为字典  加上""
def dealBody(req):
    dic = dict()
    req = req.replace('"', '')
    slicetemp = req.split(',')
    for temp in slicetemp:
        finalslice = temp.split(':')
        if finalslice[1] != "":
            key = '\"' + finalslice[0] + '\"'
            value = finalslice[1]
            dic[key] = value
    return dic

# 将url格式转化为字典 保留空字段
def dealRequestNull(req):
    dic = dict()
    slicetemp = req.split('&')
    for temp in slicetemp:
        finalslice = temp.split('=')
        key = finalslice[0]
        value = finalslice[1]
        dic[key] = value
    return dic

# 将url格式转化为字典  去除空字段
def dealRequest(req):
    dic = dict()
    slicetemp = req.split('&')
    for temp in slicetemp:
        finalslice = temp.split('=')
        if finalslice[1] != "":
            key = finalslice[0]
            value = finalslice[1]
            dic[key] = value
    return dic


# 以右边字典更新左边字典拥有的字段的值
def produceFinal(origin, mergerequest):
    for dic1 in origin.keys():
        if mergerequest.has_key(dic1):
            origin[dic1] = mergerequest.get(dic1)
    print (origin)
    return origin


# 向左合并字典
def mergeDict(request, body):
    for dic1 in body.keys():
        if request.has_key(dic1):
            print ""
        else:
            value = body.get(dic1)
            request[dic1] = value
    return request


# 字典转成body格式
def produceBody(dic):
    result = ""
    flag = 0
    for key in dic.keys():
        value = dic.get(key)
        temp = str(key) + ':' + str(value)
        flag = flag + 1
        if flag == 1:
            temp = temp
        else:
            temp = ',' + temp
        result += temp
    return result


# 字典转成request格式
def produceQuary(dic):
    result = ""
    flag = 0
    for key in dic.keys():
        value = dic.get(key)
        temp = str(key) + '=' + str(value)
        flag = flag + 1
        if flag == 1:
            temp = temp
        else:
            temp = '&' + temp
        result += temp
    return result


# 将request格式和body格式合并成 一个字典并返回
def mergeRequestBody(request, body):
    request = dealRequest(request)
    body = dealBodyNull(body)
    result = mergeDict(request, body)
    return result


# 以右边字典更新左边request查询语句 得到两个参数的集合
def updateQuery(origin, mergerequest):
    origin = dealRequestNull(origin)
    for dic1 in mergerequest.keys():
            origin[dic1] = mergerequest.get(dic1).replace(' ', '+')
    result = produceQuary(origin)
    return result


# 通过本来的查询参数 加上保存给到的参数 生成新的查询参数
def produce(origin, request, body):
    origin = dealRequest(origin)
    body = dealBody(body)
    request = dealRequest(request)
    mergerequest = mergeDict(request, body)
    finaldic = produceFinal(origin, mergerequest)
    produceQuary(finaldic)


if __name__ == '__main__':
    produce(ORIGIN, REQUEST, BODY)
