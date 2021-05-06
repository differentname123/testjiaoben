# coding=utf-8
import os
import sys


# 找到当前目录及子目录 name文件 并返回绝对路径
import this


def findFile(name):
    return search(os.path.abspath('.'), name)

def findFileBao(name):
    return searchBao(os.path.abspath('.'), name)

def search(a, b):
    result = ""
    for file in os.listdir(a):
        if os.path.isfile(a + '/' + file):
            if b == file:
                result = a + '/' + file
                return result

        else:
            result = search(a + '/' + file, b)
            if result != "":
                return result
    return result

def zhixing(pyPath):
    os.system("python {0}".format(pyPath))

def searchBao(a, b):
    result = ""
    for file in os.listdir(a):
        if os.path.isfile(a + '/' + file):
            if b in file:
                result = a + '/' + file
                return result

        else:
            result = searchBao(a + '/' + file, b)
            if result != "":
                return result
    return result


def autoRun(fileName):
    path = fileName
    threads = []
    file = open(path, 'r')
    i = 0
    try:
        while True:
            text_line = file.readline()
            if text_line:
                print text_line
                text_line = text_line.split('\n')
                text_line = text_line[0]

                pyPath = findFile(text_line + '.py')
                if pyPath == "":
                    continue

                # 删除之前的日志信息
                errPath = findFileBao(text_line + '.error')
                logPath = findFileBao(text_line + '.log')
                if logPath != "":
                    os.remove(logPath)
                if errPath != "":
                    os.remove(errPath)
                # import threading
                # p1 = threading.Thread(target=os.system, args=("python {0}".format(pyPath),))
                # threads.append(p1)
                os.system("python {0}".format(pyPath))

            else:
                break
    finally:
        file.close()
    # for t in threads:
    #
    #     t.start()
    #
    # for t in threads:
    #
    #     t.join()


# 改程序位置只能与要执行的脚本平行或更上面 ， 不能单独的在某一脚本下面
def test():
    autoRun(sys.path[0] + '/' + 'taskGET.txt')


if __name__ == '__main__':
    test()
