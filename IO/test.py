
"""
try:
    f = open('E:/Projects/python/IO/test.py', 'r')
    print(f.read())
finally:
    if f:
        f.close()
"""


with open('E:/Projects/python/IO/test2.py', 'r') as f:
    print(f.read())