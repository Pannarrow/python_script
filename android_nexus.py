import os
import shutil
import requests



import os

def main(rootPath,toDir):
    if os.path.exists(toDir):
        shutil.rmtree(toDir)
    for parent, dirnames, filenames in os.walk(rootPath):
        for filename in filenames:
            filePath = os.path.join(parent,filename)
            if '.DS_Store' == filename:
                os.remove(filePath)
            else:
                newDir = parent.replace(rootPath , toDir)
                newDir = newDir[0:newDir.rfind('/')]
                if not os.path.exists(newDir):
                    os.makedirs(newDir)
                newPath = os.path.join(newDir,filename)
                print(newPath)
                shutil.copy(filePath,newPath)
                


if __name__ == "__main__":
    rootPath = '/Users/pan/.gradle/caches/modules-2/files-2.1'
    toDir = '/Users/pan/Desktop/android'
    main(rootPath,toDir)