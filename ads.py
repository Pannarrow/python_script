
'''
修改项目中资源文件夹中的ads.json文件:
1.下载json中的网络图片
2.将路径改为本地
'''

import json
import os
import requests

baseUrl = 'http://zxbank.mtiny.cn:8555/api/file/'

def adsImg():
    print('=====开始执行ads.json=====')
    f = open('data/ads.json','r',encoding='utf-8')
    jsonObj = json.load(f)
    f.close()
    for  i in range(len(jsonObj)):
        item = jsonObj[i]
        if 'advImage' in item:
            url = baseUrl+item['advImage']
            print('下载地址:'+url)
            path = 'file:///'+downloadFile('mainApp/image/ads',url)
            print(path)
            jsonObj[i]['advImage'] = path

    fw = open('data/ads2.json','w',encoding='utf-8')
    json.dump(jsonObj,fw,indent=4,ensure_ascii=False)
    fw.close()
    print('=====结束ads.json=====')

def appImg():
    print('=====开始执行app.json=====')
    f = open('data/app.json','r',encoding='utf-8')
    jsonObj = json.load(f)
    f.close()
    items = jsonObj.items()
    for key,item in items:
        if 'dataInfos' in item:
            dataInfos = item['dataInfos']
            for i in range(len(dataInfos)):
                url = dataInfos[i]['thumbnailUrl']['default']
                print('下载地址:'+url)
                path = 'file:///'+downloadFile('mainApp/image/micro/'+key,url)
                print(path)
                jsonObj[key]['dataInfos'][i]['thumbnailUrl']['default'] = path
    fw = open('data/app2.json','w',encoding='utf-8')
    json.dump(jsonObj,fw,indent=4,ensure_ascii=False)
    fw.close()
    print('=====结束app.json=====')

def allAppImg():
    print('=====开始执行allApp.json=====')
    f = open('data/allApp.json','r',encoding='utf-8')
    jsonObj = json.load(f)
    f.close()
    if 'allApp' in jsonObj:
        allApp = jsonObj['allApp']
        if 'dataInfos' in allApp:
            dataInfos = allApp['dataInfos']
            for i in range(len(dataInfos)):
                dataInfo = dataInfos[i]
                if 'data' in dataInfo:
                    data = dataInfo['data']
                    for j in range(len(data)):
                        dataItem = data[j]
                        url = dataItem['thumbnailUrl']['default']
                        print('下载地址:'+url)
                        path = 'file:///'+downloadFile('mainApp/image/micro/allApp',url)
                        print(path)
                        jsonObj['allApp']['dataInfos'][i]['data'][j]['thumbnailUrl']['default'] = path
    fw = open('data/allApp2.json','w',encoding='utf-8')
    json.dump(jsonObj,fw,indent=4,ensure_ascii=False)
    fw.close()
    print('=====结束allApp.json=====')

def downloadFile(downloadDir,downloadUrl,fileName = None):
    if downloadUrl=='':
        return
    try:
        if fileName == None:
            fileName = downloadUrl[downloadUrl.rfind("/")+1:]
        if not os.path.exists(downloadDir):
            os.makedirs(downloadDir)
        filePath = os.path.join(downloadDir,fileName)
        r = requests.get(downloadUrl,verify=False)
        with open(filePath, "wb") as code:
            code.write(r.content)
        return filePath
    except Exception as e:
        print(str(downloadUrl)+'下载失败:'+str(e))
        exit()

adsImg()
appImg()
allAppImg()