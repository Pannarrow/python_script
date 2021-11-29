#coding=utf-8
import subprocess
import sys
import os
import zipfile
import json
import shutil

def zipEntryCRC(keystore, keyAlias, keyPassword, srcApkPath):
    #获取apk内容的CRC
    crcJson = {}
    z = zipfile.ZipFile(srcApkPath, "r")
    for info in z.infolist():
        if info.filename.endswith('.so') or info.filename.endswith('.dex') or info.filename.endswith('AndroidManifest.xml'):
            crcJson[info.filename] = info.CRC
    print('crc result:'+str(crcJson))
    #解压apk
    rindex = srcApkPath.rfind("/")
    if rindex < 0:
        rindex = 0
    dstDir = srcApkPath[:rindex]
    tempDir = os.path.join(dstDir,'tempDir')
    if os.path.exists(tempDir):
        shutil.rmtree(tempDir)
    # subprocess.call(['unzip -q %s -d %s' % (srcApkPath,tempDir)],shell=True)
    subprocess.call(['apktool -r d -f %s -o %s' % (srcApkPath,tempDir)],shell=True)
    print('解压到目录:'+tempDir)
    #修改crc.json
    crcPath = os.path.join(tempDir,'assets/crc.json')
    f = open(crcPath,'w',encoding='utf-8')
    json.dump(crcJson,f,indent=4,ensure_ascii=False)
    #压缩安装包
    newApkPath = srcApkPath.replace('.apk','_crc.apk')
    if os.path.exists(newApkPath):
        os.remove(newApkPath)
    # subprocess.call(['ditto -c -k --sequesterRsrc %s %s' % (tempDir,newApkPath)],shell=True)
    subprocess.call(['apktool b %s -o %s' % (tempDir,newApkPath)],shell=True)
    print('压缩到目录:'+newApkPath)
    #重新签名
    subprocess.call(['apksigner sign --ks %s --ks-key-alias %s --ks-pass pass:%s %s' % (keystore,keyAlias,keyPassword,newApkPath)],shell=True)
    subprocess.call(['rm -rf %s' % (tempDir)],shell=True)

        



if __name__ == "__main__":
    keystore = sys.argv[1]
    keyAlias = sys.argv[2]
    keyPassword = sys.argv[3]
    srcApkPath = sys.argv[4]

    zipEntryCRC(keystore, keyAlias, keyPassword, srcApkPath)


# zipEntryCRC("debug2.keystore", "androiddebugkey", "android", "SME-App_fat3App_fat3App_1.0.35.apk")