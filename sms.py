import os 
import pandas as pd 
import numpy as np 
import time
#群发短信，50个号码一发，读取表格中手机号，列名写“手机号”

content="短信内容"
mobiles=""
df = pd.read_excel('mobiles.xlsx')
#遍历表格，读取手机号
for index,row in df.iterrows():
    if index==len(df)-1:
        mobiles=mobiles+str(row['手机号'])
        os.popen("adb shell am start -a android.intent.action.SENDTO -d sms:{} --es sms_body {}".format(mobiles,content))
        time.sleep(2)
        #模拟发送
        os.popen("adb shell input keyevent 22")
        time.sleep(1)
        os.popen("adb shell input keyevent 66")
        time.sleep(120)
        os.popen("adb shell input keyevent 3")
    elif index % 50==0 and index!=0:

        mobiles=mobiles+str(row['手机号'])
        #打开短信，编辑短信
        os.popen("adb shell am start -a android.intent.action.SENDTO -d sms:{} --es sms_body {}".format(mobiles,content))
        time.sleep(2)
        #模拟发送
        os.popen("adb shell input keyevent 22")
        time.sleep(1)
        os.popen("adb shell input keyevent 66")
        time.sleep(120)
        os.popen("adb shell input keyevent 3")
        mobiles=""
    else:
        mobiles=mobiles+str(row['手机号'])+','