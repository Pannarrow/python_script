'''
遍历文件夹，找到文件名相同，内容不同的文件
'''
import os

def diff(rootPath):
    for parent, dirnames, filenames in os.walk(rootPath):
        for filename in filenames:
            return