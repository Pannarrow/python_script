token = 'QKY6yzjJafNPib2coRHX'
git_base_url = 'http://git.mtiny.cn:8334/'
git_user = 'yujian'
git_password = '12345678'
targetDir = 'temp/tiny-spec'
groupid = '135'

import gitlab
import os
import shutil
import subprocess

def changeGit():
    gl = gitlab.Gitlab(git_base_url, private_token=token)
    rootPath = os.getcwd()
    group = gl.groups.get(groupid)
    for project in group.projects.list(owned=True, all=True):
        giturl = project.http_url_to_repo
        giturl = giturl.replace('http://20.201.35.70',git_base_url)
        giturl = giturl.replace('http://','http://%s:%s@'%(git_user,git_password))
        name = project.name
        print(giturl)
        gitDir = os.path.join(rootPath,targetDir,name)
        subprocess.call(['git clone --depth 1 %s %s'%(giturl,gitDir)],shell=True)
        eidtGitAdress(gitDir)
        os.chdir(gitDir)
        subprocess.call(['git add .'],shell=True)
        subprocess.call(['git commit -m "更换podspec地址"'],shell=True)
        subprocess.call(['git push origin master'],shell=True)





def eidtGitAdress(projectPath):
    '''
    replace old to new
    '''
    old  = 'http://zhangxl:Sunline300348@git.mtiny.cn:8333/zxbank/tiny_ios/tiny_ios/framework'
    new =  'http://zhangxl:Sunline300348@git.mtiny.cn:8334/zxbank/zxbank_app/tiny_ios/framework'
    for parent, dirnames, filenames in os.walk(projectPath):
        for filename in filenames:
            if filename.find('.podspec') > 0:
                specFile = os.path.join(parent,filename)
                print(specFile)
                fr = open(specFile,'r')
                content = fr.read()
                fr.close()
                content = content.replace(old,new)
                fw = open(specFile,'w')
                fw.write(content)
                fw.close()



if __name__ == "__main__":
    eidtGitAdress('temp/tiny-spec')