# coding=utf-8
from common.cmopare import TotalFun, PostTotalFun, PostSingle, PostDouble

MACHINE1 = "127.0.0.1:8514"
MACHINE2 = "testgrowth.busi.inkept.cn"
API = "/api/push/task/resume"
CONFIGNAME = "task_resume_config.ini"
BODYCONFIG = "task_resume.ini"

if __name__ == '__main__':
    for i in range(100):
        print(i)
        PostDouble(BODYCONFIG, CONFIGNAME, API, MACHINE1, MACHINE2)