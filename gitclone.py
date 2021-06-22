'''
clone指定group下的所有工程，并替文件夹名字

'''


import gitlab
import subprocess
import os
import shutil

git_url = 'http://20.208.15.208:8334/'
git_auth_token = 'B-r3W793Wpytt6KSC2yZ'
myGroup = 'micro_app'

def main():
    print('start...')
    rootPath = os.getcwd()#根目录
    groupDir = os.path.join(rootPath,myGroup)
    if not os.path.exists(groupDir):
        os.makedirs(groupDir)

    gl = gitlab.Gitlab(git_url, private_token=git_auth_token)
    groups = gl.groups.list(all=True)
    for group in groups:
        groupName = group.name
        groupDesc = group.description
        groupPath = group.path
        if groupName == myGroup:
            projects = group.projects.list()
            for project in projects:
                projectName = project.name
                projectDesc = project.description
                projectId = project.id
                projectUrl = project.http_url_to_repo
                projectUrl = projectUrl.replace('http://20.201.32.211/',git_url.replace('http://','http://hongpan:12345678@'))
                print('git地址:'+projectUrl)
                
                os.chdir(groupDir)
                if os.path.exists(projectName):
                    shutil.rmtree(projectName)
                #http://20.208.20.238:8334/zxbank/zxbank_app/main_app.git
                subprocess.call(['git clone -b %s %s %s'%('uat', projectUrl, projectName)],shell=True)
                print('%sclone完成'%(projectName))
    os.chdir(rootPath)
    print('end...')


def rename():
    jsonData = {
        "accountcenter": "9287d901-14bf-4d68-b2c5-e93da3740b48",
        "openaccount": "b2d59c5e-94fb-4fea-a0ef-1e868fec961d",
        "transactionhistory": "542cb601-4564-4dbe-9cd6-7104ef79055d",
        "receivepaycode": "0db14a37-b973-4a51-aca4-2b4854496098",
        "transfer": "890530ac-2a35-445e-ae57-ecb9b44cfcab",
        "cashsweep": "e0693752-38b9-4618-bb87-79612d0e9cfd",
        "scancode": "e48b138c-3ae3-45cb-b088-bcc3f0cfbb24",
        "consumerloans": "804e2273-db09-41d1-a73a-1dad024aa791",
        "financial": "d370f94b-4e76-4488-84e8-915c4ae495b4",
        "deposit": "4d3a0ff9-1ad0-472b-9bdc-cc143505a9a5",
        "theme": "489c841f-0da7-454a-a1b7-23b582b489a3",
        "feedback": "bf6fdc5f-42b1-4561-a5ed-89b94cfc45f3",
        "rightcenter": "d7bcf1c6-28be-4954-8b63-e1f94b91b4ab",
        "msgcenter": "7b334eee-371a-4c63-919e-ecb455617dca",
        "helpcenter": "f1f6b855-20a7-46ff-a1ce-8c5aa3a8a3a8",
        "signup": "da4869b3-281d-4c2b-9244-8088a640a45a",
        "securitycenter": "a945ff95-edca-4d62-af33-ea62721c5c51",
        "share": "b377618c-4e2c-441b-bf24-ee1c18e14100",
        "banklist": "c1e10131-02c1-4df4-b92a-28372252b2cf"
    }

    for dirName in os.listdir(myGroup):
        for key,value in jsonData.items():
            if key in  dirName:
                print(dirName+':'+value)
                oldname = os.path.join(myGroup, dirName)      # 老文件夹的名字
                newname = os.path.join(myGroup, value)     # 新文件夹的名字
                os.rename(oldname, newname)


if __name__ == '__main__':
    main()
    # rename()

