import sys
import smtplib  
from email.mime.text import MIMEText
import requests
import json

# 邮件配置
mailto_list="pannarrow@qq.com;chenyan1@sunline.cn" #设置收件人
mail_host="smtp.exmail.qq.com"  #设置服务器
mail_port=25  #设置服务器端口号
mail_user="hongpan@sunline.cn"    #用户名
mail_pass="aPan.417621"   #口令 

#发送邮件
def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="hongpan@sunline.cn" #设置发件人
    msg = MIMEText(content,_subtype='html',_charset='gb2312')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = to_list  
    try:  
        s = smtplib.SMTP()  
        s.connect(mail_host,mail_port)  #连接smtp服务器，端口号默认为25
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list.split(';'), msg.as_string())  #发送邮件
        s.close()  
        return True  
    except Exception as e:  
        print(str(e)) 
        return False  

#生成邮件内容
def generatedMail(title,branch,versionName,apkQRCodeURL,ipaQRCodeURL,to_list,email_content): 
    
    htmlText  = '<html>'
    htmlText += '<head>'
    htmlText += '    <title>%s</title>'%(title)
    htmlText += '    <meta charset="utf-8">'
    htmlText += '</head>'
    htmlText += '<body>'
    htmlText += '    <div style="display: flex; align-items: flex-start;flex-direction:column;">'
    htmlText += '       <label>%s</label>'%(email_content)
    htmlText += '       <label>%s的最新app安装包:</label>'%(branch)
    if apkQRCodeURL != None:
        htmlText += '        <label>Android %s</label>'%(versionName)
        htmlText += '        <img src="%s" />'%(apkQRCodeURL)
    if ipaQRCodeURL != None:
        htmlText += '        <label>IOS %s</label>'%(versionName)
        htmlText += '        <img src="%s" />'%(ipaQRCodeURL)
    htmlText += '    </div>'
    htmlText += '</body>'
    htmlText += '</html>'
    if send_mail(to_list,title,htmlText):  
        print("发送成功" ) 
    else:  
        print("发送失败")

#上传蒲公英
def upload(filePath,uKey,_api_key):
    commitUrl = 'https://www.pgyer.com/apiv2/app/upload'
    data = {
        "uKey":uKey,
        "_api_key":_api_key
    }
    headers = {
        "enctype":"multipart/form-data"
    }
    fileData = {
        "file":open(filePath,"rb")
    }
    res = requests.post(url=commitUrl,data=data,headers=headers,files = fileData)
    result = []
    try:
        result = json.loads(res.text)
    except Exception as e:  
        print('请求失败1:'+str(e)) 
        print(result)
        sys.exit(1)
    if 'data' in result and 'buildQRCodeURL' in result['data']:
        print('安装包路径上传成功')
        print(result['data'])
        appQRCodeURL = result['data']['buildQRCodeURL']
        return appQRCodeURL
    else:
        print('请求失败2:' + str(result))
        sys.exit(1)

def doUpload(title,branch,versionName,srcApkPath,srcIpaPath,uKey,_api_key,to_list,email_content):
    apkQRCodeURL = None
    if srcApkPath != 'None':
        apkQRCodeURL = upload(srcApkPath,uKey,_api_key)
    ipaQRCodeURL = None
    if srcIpaPath != 'None':
        ipaQRCodeURL = upload(srcIpaPath,uKey,_api_key)
    generatedMail(title,branch,versionName,apkQRCodeURL,ipaQRCodeURL,to_list,email_content)




if __name__ == "__main__":
    title = sys.argv[1]
    branch = sys.argv[2]
    versionName = sys.argv[3]
    srcApkPath = sys.argv[4]
    srcIpaPath = sys.argv[5]
    uKey = sys.argv[6]
    _api_key = sys.argv[7]
    to_list = sys.argv[8]
    email_content = sys.argv[9]

    doUpload(title,branch,versionName,srcApkPath,srcIpaPath,uKey,_api_key,to_list,email_content)

# python3 -u /Users/sunline-mac/Documents/jenkinsShell/uploadtool.py SME_APP origin/fat3App 1.0.0 /Users/sunline-mac/Documents/workspace/sme_app/Android/helloTiny/build/outputs/apk/release/helloTiny-release_crc.apk None 5b402b50ee49dffdbf79ddcf81b10784 3faeda05d0df08dda9f4e33ecb09a7c2 chenyan1@sunline.cn
    
