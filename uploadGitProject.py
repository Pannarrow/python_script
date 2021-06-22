'''
创建gitlab工程 修改文件 并提交
'''

import gitlab
import subprocess
import os


git_url = "http://20.5.133.31:8432"
git_auth_token = "My3pQfh7rphtkLjysp8G"
git_user = "likuangyu"
git_password = "oooo1234"
groupId = "13" #13是ios的framework
workpsace = '/Users/sunline/Desktop/Tiny3.0/framework'
# groupId = "14" #14是ios的podspec
# workpsace = '/Users/sunline/Desktop/Tiny3.0/tiny-spec'

def main(workspace):
    dirlist = os.listdir(workspace)
    for dirName in dirlist:
        dirPath = os.path.join(workspace,dirName)
        if os.path.isdir(dirPath):
            print(dirPath)

            projectId,url = searchProject(dirName,groupId)
            gitUrl = ''
            if projectId == -1:
                gitUrl = createNewProject(groupId,dirName)
                print('>仓库创建成功,提交工程',gitUrl)

                gitUrl = gitUrl.replace('http://20.201.35.70','http://20.5.133.31:8432')
                gitUrl = gitUrl.replace('://','://%s:%s@'%(git_user,git_password))
                eidtGitAdress(dirPath)
                subprocess.call(['git clone %s tempDir'%(gitUrl)],shell=True)
                subprocess.call(['rm -rf %s/.git'%(dirPath)],shell=True)
                subprocess.call(['mv tempDir/.git %s'%(dirPath)],shell=True)
                pushProject(dirPath)
            else :
                gitUrl = url
                print('>仓库已存在,无需创建',gitUrl)

                # gitUrl = gitUrl.replace('http://20.201.35.70','http://20.5.133.31:8432')
                # gitUrl = gitUrl.replace('://','://%s:%s@'%(git_user,git_password))
                # subprocess.call(['git clone %s tempDir'%(gitUrl)],shell=True)
                # tempDirPath = os.path.join('/Users/sunline/Desktop/Tiny3.0/','tempDir')
                # eidtGitAdress(tempDirPath)
                # pushProject(tempDirPath)
                
            
            


def searchProject(projectName,groupId):
    '''
    查找工程Id
    '''
    gl = gitlab.Gitlab(git_url, private_token=git_auth_token)
    projects = gl.projects.list(search=projectName)
    if len(projects)>0:
        for project in projects:
            if project.http_url_to_repo.lower().find('/tiny-spec/') > 0 and groupId == '14':
                return project.id,project.http_url_to_repo
            if project.http_url_to_repo.lower().find('/framework/') > 0 and groupId == '13':
                return project.id,project.http_url_to_repo
    return -1,''


def createNewProject(groupId, projectName):
    '''
    创建工程
    '''
    projectArgv = {
        'name': projectName, 
        'namespace_id': groupId
    }
    gl = gitlab.Gitlab(git_url, private_token=git_auth_token)
    project = gl.projects.create(projectArgv)
    fileArgv = {
        'file_path': 'README.md',
        'branch': 'master',
        'content': "脚本创建工程:"+projectName,
        'author_email': 'hongpan@sunline.cn',
        'author_name': 'hongpan',
        'commit_message': 'README.md'
    }
    f = project.files.create(fileArgv)
    return project.http_url_to_repo


def pushProject(projectPath):
    '''
    提交工程
    '''
    rootPath = os.getcwd()
    os.chdir(projectPath)#切换到配置文件存放目录
    subprocess.call(['git add .'],shell=True)
    subprocess.call(['git commit -m 脚本创建工程提交'],shell=True)
    subprocess.call(['git push origin master'],shell=True)
    os.chdir(rootPath)#切换到原始目录
    subprocess.call(['rm -rf tempDir'],shell=True)


def eidtGitAdress(projectPath):
    '''
    replace old to new
    '''
    old  = 'http://e-git.yfb.sunline.cn/TinyBuilder/tiny-app/tiny-ios-framework'
    old2 = 'http://p.mtiny.cn:8000/iOS-test'
    new = 'http://20.5.133.31:8432/framework'
    for parent, dirnames, filenames in os.walk(projectPath):
        for filename in filenames:
            if filename.find('.podspec') > 0:
                specFile = os.path.join(parent,filename)
                print(specFile)
                fr = open(specFile,'r')
                content = fr.read()
                fr.close()
                content = content.replace(old,new).replace(old2,new)
                fw = open(specFile,'w')
                fw.write(content)
                fw.close()



main(workpsace)