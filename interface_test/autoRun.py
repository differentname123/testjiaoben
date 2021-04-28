# coding=utf-8
import os
import sys


# 找到当前目录及子目录 name文件 并返回绝对路径
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
    file = open(path, 'r')
    i = 0
    try:
        while True:
            text_line = file.readline()
            if text_line:
                print text_line
                text_line = text_line.split('\n')
                text_line = text_line[0]

                # 删除之前的日志信息
                errPath = findFileBao(text_line + '.error')
                logPath = findFileBao(text_line + '.log')
                if logPath != "":
                    os.remove(logPath)
                if errPath != "":
                    os.remove(errPath)

                pyPath = findFile(text_line + '.py')
                if pyPath == "":
                    continue
                print pyPath
                os.system("python {0}".format(pyPath))

            else:
                break
    finally:
        file.close()


def test():
    autoRun(sys.path[0] + '/' + 'autoRun.txt')


if __name__ == '__main__':
    test()
