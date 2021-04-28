# coding=utf-8
from common.cmopare import TotalFun, PostTotalFun, PostSingle, PostDouble
from common.read_config import getConfigValue

MACHINE1 = "127.0.0.1:8514"
MACHINE2 = "testgrowth.busi.inkept.cn"
API = "/api/push/task/resume"
CONFIGNAME = "task_resume_config.ini"
BODYCONFIG = "task_resume.ini"

if __name__ == '__main__':
    excuteTime = int(getConfigValue('excuteTime'))
    for i in range(excuteTime):
        print(i)
        PostDouble(BODYCONFIG, CONFIGNAME, API, MACHINE1, MACHINE2)