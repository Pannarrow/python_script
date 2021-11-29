import smtplib  
from email.mime.text import MIMEText


# 发送的内容
# packagetag = 'Affin'
# apkQrcode = 'http://img.jdzj.com/UserDocument/2013c/fangweibiao/Picture/201312895921.jpg'
# ipaQrcode = 'https://p.mtiny.cn:9442/resources/Affin/Android/20200529100154/affin.png'



# 邮件配置
mailto_list=["pannarrow@qq.com","zhengshupeng@sunline.cn","changhongwen@sunline.cn"] #设置收件人
mail_host="smtp.exmail.qq.com"  #设置服务器
mail_port=25  #设置服务器端口号
mail_user="hongpan@sunline.cn"    #用户名
mail_pass="aPan.417621"   #口令 
  
def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="hongpan@sunline.cn" #设置发件人
    msg = MIMEText(content,_subtype='html',_charset='gb2312')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        s = smtplib.SMTP()  
        s.connect(mail_host,mail_port)  #连接smtp服务器，端口号默认为25
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()  
        return True  
    except Exception as e:  
        print(str(e)) 
        return False  


def main(packagetag,apkQrcode,apkDownload,ipaQrcode,ipaDownload): 
    htmlText = \
    '<html>'\
    '<head>'\
    '    <title>%s</title>'\
    '    <meta charset="utf-8">'\
    '</head>'\
    '<body>'\
    '    <div style="dispdivlay: flex;align-items: center;flex-direction:column;">'\
    '        <label>Android</label>'\
    '        <div>'\
    '            <label>二维码</label>'\
    '            <label>%s</label>'\
    '        </div>'\
    '        <div>'\
    '            <label>APK</label>'\
    '            <label>%s</label>'\
    '        </div>'\
    '        <label>IOS</label>'\
    '        <div></div>'\
    '            <label>二维码</label>'\
    '            <label>%s</label>'\
    '        </div>'\
    '        <div>'\
    '            <label>IPA</label>'\
    '            <label>%s</label>'\
    '        </div>'\
    '    </div>'\
    '</body>'\
    '</html>'%(packagetag,apkQrcode,apkDownload,ipaQrcode,ipaDownload)
    print(apkQrcode)
    print(ipaQrcode)
    if send_mail(mailto_list,packagetag,htmlText):  
        print("发送成功" ) 
    else:  
        print("发送失败")
