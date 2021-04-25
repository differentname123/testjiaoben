# coding=utf-8
import sys

from common.build_body import readbody
from common.build_query import repalceValue, repalceBodyValue, mergeRequestBody, produceFinal, updateQuery, addKey
from common.cmopare import buildURI, visitURL, singleGet, PostSingle, SinglePost, save_data
from common.read_config import readandset

HEAD = "http://"
MACHINE1 = "127.0.0.1:8514"
MACHINE2 = "testgrowth.busi.inkept.cn"

SAVECONFIG = "template_save_config.ini"
SAVEBODY = "template_save.ini"
SAVEAPI = "/api/push/template/save"

QUERYCONFIG = "template_list_config.ini"
QUERYAPI = "/api/push/template/list"

DELETECONFIG = "template_delete_config.ini"
DELETEBODY = "template_delete.ini"
DELETEAPI = "/api/push/template/delete"


# 修复template查询的参数
def fixTemplateParams(originParams):
    originParams = addKey(originParams, 'template_body', 'body')
    originParams = addKey(originParams, 'template_title', 'title')  # 增加字段 title 值为 template_title 的值
    originParams = repalceValue(originParams, 'template_type', '')  # 将template_type 值设置为 空

    return originParams


def produceTemplateParams(originConfig, dic):
    originParams = readandset(originConfig, 0)
    originParams = updateQuery(originParams, dic)
    originParams = fixTemplateParams(originParams)
    return originParams


def templateDeleteSomething(machine, listAPI, originConfig, bodyConfig, deleteConfig, deleteAPI, originDic):
    flag1 = 0

    params = produceTemplateParams(originConfig, originDic)

    print ("查询:")
    httpresp1 = singleGet(params, listAPI, machine)
    logmessage = 'False\n' + str(params) + str(httpresp1)
    data = httpresp1.get('data')
    listTemp = data.get('list')
    size = len(listTemp)
    if size != 0:
        listTemp = listTemp[0]
        # 获取指定值
        template_id = listTemp.get('template_id')
        body_origin = readbody(bodyConfig)
        body = repalceBodyValue(body_origin, u'"template_id"', template_id)
        print ("删除:")
        flag1, logmessage = SinglePost(body, deleteConfig, deleteAPI, machine)
        return flag1, logmessage
    return flag1, logmessage


def saveAndDelete(SaveBodyConfig, SaveConfig, saveAPI, machine, queryAPI, queryConfig, deleteBody, deleteConfig,
                  deleteAPI):
    flag = 1
    print ("保存:")
    save_result, save_info, params, body = PostSingle(SaveBodyConfig, SaveConfig, saveAPI, machine)

    # 得到上传保存信息的参数
    dic = mergeRequestBody(params, body)

    save_data('save: ' + str(save_info), sys.path[0] + "/" + 'save_delete' + '.log')
    if save_result == 0:
        save_data('save: ' + str(save_info), sys.path[0] + "/" + 'save_delete' + '.error')
        print ("save fail and exit")
        flag = 0
    else:
        print ("save success")

        delete_result, delete_info = templateDeleteSomething(machine, queryAPI, queryConfig, deleteBody, deleteConfig,
                                                             deleteAPI, dic)
        save_data('delete: ' + str(delete_info), sys.path[0] + "/" + 'save_delete' + '.log')
        if delete_result == 0:
            save_data('delete: ' + str(delete_info), sys.path[0] + "/" + 'save_delete' + '.error')
            print ("delete fail and exit")
            flag = 0
        else:
            print ("detele success")
    return flag


if __name__ == '__main__':
    flag = 1
    for i in range(100):
        print(i)
        flag = saveAndDelete(SAVEBODY, SAVECONFIG, SAVEAPI, MACHINE2, QUERYAPI, QUERYCONFIG, DELETEBODY, DELETECONFIG,
                             DELETEAPI)
    print("cmpare")
