'''
删除git指定工程的tag
'''


import gitlab
import subprocess
import os

token = 'xtQaT4tt6ss6kunoZfpn'
url = 'http://20.5.133.31:8432'
projectName = '工程名'

gl = gitlab.Gitlab(url, private_token=token)
projects = gl.projects.list(search=projectName)
if len(projects)>0:
    for project in projects:
        tags = project.tags.list()
        for tag in tags:
            print(tag.name)
            tag.delete()
        