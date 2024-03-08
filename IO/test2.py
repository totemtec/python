# -*- coding: UTF-8 -*-

try:
    f = open('E:/Projects/python/IO/test2.py', 'r', encoding='utf-8')
    for line in f.readlines():
        print(line) # 把末尾的'\n'删掉
finally:
    if f:
        f.close()
