
'''
修改webhooks
'''


url = 'http://e-git.yfb.sunline.cn'
groupId = 1382 #想要修改的group
token = 'GKkGrSGvzcswjQXknK3a' #有权限的token
headers = {
    'PRIVATE-TOKEN': token
}

import gitlab
import os
import shutil
import requests
import json

def changeHooks():
    # private token or personal token authentication
    gl = gitlab.Gitlab(url, private_token=token)

    # get the group with id == 2
    group = gl.groups.get(groupId)
    for project in group.projects.list(owned=True, all=True):
        name = project.name
        print(name)
        projectId = project.id
        # print(projectId)
        result = requests.get('%s/api/v4/projects/%s/hooks'%(url,projectId),headers=headers)
        hookjson = json.loads(result.text)
        if len(hookjson)==0:
            print(name)
            continue
        webhook = json.loads(result.text)[0]
        '''
        {
            "id":919,
            "url":"http://10.25.0.35/project/tinyguidepage-android",
            "created_at":"2020-07-23T01:37:38.327Z",
            "push_events":false,
            "tag_push_events":true,
            "merge_requests_events":false,
            "repository_update_events":false,
            "enable_ssl_verification":true,
            "project_id":2058,
            "issues_events":false,
            "confidential_issues_events":false,
            "note_events":false,
            "confidential_note_events":false,
            "pipeline_events":false,
            "wiki_page_events":false,
            "job_events":false,
            "push_events_branch_filter":""
        }
        '''
        hookId = webhook['id']
        # print(hookId)
        hookUrl = webhook['url']
        hookUrl = hookUrl.replace('10.25.0.35','10.25.0.188:8888')
        hookUrl = hookUrl.replace('10.25.0.188:8888','10.25.2.109:8888')
        webhook['url'] = hookUrl
        # print(hookUrl)
        
        result = requests.put('%s/api/v4/projects/%s/hooks/%s'%(url,projectId,hookId),headers=headers,data=webhook)
        print(name,hookUrl)

changeHooks()