'''
获取gitlab上某个文件的内容
'''


import gitlab
import subprocess
import os

token = 'iwtJM7hqVWCtH7z5cafy'
url = 'http://e-git.yfb.sunline.cn'
projectName = 'management-platform-shell'

gl = gitlab.Gitlab(url, private_token=token)
projects = gl.projects.list(search=projectName)
if len(projects)>0:
    for project in projects:
        raw_content = project.files.raw(file_path='tiny3.0/res/tinyPackage.json', ref='master')
        print(raw_content)
        fw = open('tinyPackage.json', 'wb')
        fw.write(raw_content)