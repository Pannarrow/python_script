
# .git/config
# https://p.mtiny.cn:9443/TinyAndroid3.0
# to
# http://e-git.yfb.sunline.cn/groups/hzcl/tinyapp/tiny_android

import os

#遍历修改git地址
def traverseDir(rootPath,findStr,tStr):
    for parent, dirnames, filenames in os.walk(rootPath):
        for dirname in dirnames:
            if dirname == '.git':
                gitConfig = os.path.join(parent,dirname,'config')
                fw = open(gitConfig,'r')
                t_list=[]
                for lineStr in fw.readlines(): 
                    if lineStr.find(findStr)>0:
                        lineStr = lineStr.replace(findStr,tStr)
                        print('修改文件:'+gitConfig)
                    t_list.append(lineStr)
                fw.close()
                content = ''.join(t_list)
                fr = open(gitConfig,'w')
                fr.write(content)
                fr.close()
            else:
                continue


if __name__ == "__main__":
    rootPath = '/Users/pan/Documents/sunline/tiny/Tiny3.0'
    findStr = 'https://p.mtiny.cn:9443/TinyAndroid3.0'
    tStr = 'http://e-git.yfb.sunline.cn/hzcl/tinyapp/tiny_Android'

    # rootPath = '/Users/pan/Documents/sunline/'
    # findStr = 'https://p.mtiny.cn:9443/TinyiOS3.0'
    # tStr = 'http://e-git.yfb.sunline.cn/hzcl/tinyapp/tiny_iOS'

    traverseDir(rootPath,findStr,tStr)