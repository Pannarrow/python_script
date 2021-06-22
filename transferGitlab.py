import gitlab
import subprocess
import os
import shutil

git_url = 'http://git.mtiny.cn:8333/'
git_auth_token = 'knFJayE8G5E9Kw7pbGfm'
git_user = 'hongpan'
git_password = '12345678'

git_url2 = 'http://20.208.7.100:8777/'
git_auth_token2 = 'QKY6yzjJafNPib2coRHX'


'''



## 这种方式适合单向同步，git迁移；由于该种方式会完全替换目标的工程，不适合双向同步的
## 从源gitlab克隆镜像到本地
git clone --mirror http://git.mtiny.cn:8333/zxbank/tiny_ios/tiny_ios/framework/tinysaveshareimg
## 进入克隆的镜像目录
cd tinystepview
## 将克隆的镜像推送至目标
git push --mirror http://20.208.7.100:8777/zxbank/zxbank_app/tiny_ios/framework/tinysaveshareimg.git

'''

def main():
    gl = gitlab.Gitlab(git_url, private_token=git_auth_token)
    gl2 = gitlab.Gitlab(git_url2, private_token=git_auth_token2)
    #从原git获取分组
    groups = gl.groups.list(all=True)
    for group in groups:
        groupName = group.name
        groupDesc = group.description
        groupPath = group.path
        print(groupName+','+groupDesc+','+groupPath)
        if groupName == 'zxbank' or groupName == 'tiny_Android':
            continue
        try:
            newGroup = gl2.groups.get(142)
            print('新git存在同名分组，直接获取')
        except Exception as err:
            print(err)

        #从原分组获取工程
        projects = group.projects.list()
        for project in projects:
            projectName = project.name
            projectDesc = project.description
            projectId = project.id
            
            #在新git上创建项目
            newProjectList = newGroup.projects.list(search=projectName)
            if len(newProjectList) == 0:
                projectArgv = {
                    'name': projectName, 
                    'namespace_id': newGroup.id
                }
                print('newGroup.id:'+str(newGroup.id))
                newProject = gl2.projects.create(projectArgv)
                newProject.description = projectDesc
                newProject.save()
                print('在新git创建工程成功' + projectName)
            else:
                newProject = newProjectList[0]
                print('新git存在同名工程，直接获取')

            projectUrl = project.http_url_to_repo
            projectUrl = projectUrl.replace('http://20.201.35.78/',git_url.replace('http://','http://hongpan:12345678@'))
            newProjectUrl = newProject.http_url_to_repo
            newProjectUrl = newProjectUrl.replace('http://20.201.32.211/',git_url2.replace('http://','http://yujian:12345678@'))
            print('git地址:'+projectUrl)
            print('新git地址:'+newProjectUrl)

            rootPath = os.getcwd()
            groupDir = os.path.join(rootPath,'temp',groupName)
            if not os.path.exists(groupDir):
                os.makedirs(groupDir)
            os.chdir(groupDir)
            if os.path.exists(projectName):
                shutil.rmtree(projectName)
            subprocess.call(['git clone --mirror ' + projectUrl +' '+ projectName],shell=True)
            os.chdir(projectName)
            subprocess.call(['git push --mirror ' + newProjectUrl],shell=True)
            os.chdir(rootPath)





if __name__ == '__main__':
    main()
    