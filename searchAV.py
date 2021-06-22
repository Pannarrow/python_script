import requests
import re
from lxml import etree
requests.packages.urllib3.disable_warnings() 

searchText = '30人'

# baseUrl = 'https://www.ijg30zftssadg9ih.com'
# listUrl = '/home/vodlist/25/1032-1.html'

baseUrl = 'https://g52k4d7ncmg1zrzq.com'
listUrl = '/home/vodlist/7/721-1.html'

def search(searchText,baseUrl,listUrl,listCount):
    headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.ijg30zftssadg9ih.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36'
    }
    i = 0
    while i < listCount:
        i += 1
        url = baseUrl+listUrl.replace('1.html','')+'%s.html'%(i)
        r = requests.get(url,headers=headers,verify=False)
        html=r.content
        html_doc=str(html,'utf-8')#解决乱码问题
        # print(html_doc)
        # print('page number:'+str(i))
        lxmlParser(i,html_doc,searchText)

def lxmlParser(pageIndex,page,searchText):
    doc = etree.HTML(page)
    allDiv = doc.xpath('//div[@class="bodylist"]')
    if len(allDiv)==0:
        allDiv = doc.xpath('//div[@class="vodlist dylist"]')
    for row in allDiv:
        allDivItem = row.xpath('.//div[@class="body"]')
        if len(allDivItem)==0:
            allDivItem = row.xpath('.//div[@class="listpic"]')
        for a in allDivItem:
            url = a.xpath('./a/@href')[0]
            titleElements = a.xpath('.//p[@class="name"]')
            if len(titleElements)==0:
                titleElements = a.xpath('.//div[@class="vodname"]')
            title = titleElements[0].text
            if searchText in title:
                #如果能直接收到则跳出当前循环
                print('page %s,matching content:'%(pageIndex))
                print('\t'+title)
                print('\t'+baseUrl+url)
                break
            chs = list(searchText)
            n = len(chs)
            matchCount = 0
            #如果不能搜到则拆分字符串单个匹配
            for ch in chs:
                if ch in title:
                    matchCount += 1
            if matchCount>2:
                print('page %s,matching content:'%(pageIndex))
                print('\t'+title)
                print('\t'+baseUrl+url)    
                break



if __name__ == "__main__":
    # search(searchText,baseUrl,listUrl,75)
    search(searchText,baseUrl,listUrl,82)
    
