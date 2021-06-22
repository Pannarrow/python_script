'''
环境配置：
安装python3,下载地址:https://www.python.org/
安装python库selenium,cmd控制台运行命令:pip install selenium
安装chrome浏览器
安装与浏览器对应版本的chromeDriver,下载地址:http://npm.taobao.org/mirrors/chromedriver/, 
解压压缩包,找到chromedriver.exe复制到chrome的安装目录（其实也可以随便放一个文件夹）。复制chromedriver.exe文件的路径并加入到电脑的环境变量中去

使用说明：
第一步cmd控制台运行命令:python test_buy.py
第二步会自动打开商城链接，需要10s内登录，建议使用二维码快速登录
第三步会自动打开所需抢购的商品链接，建议先选择好款式再复制链接，填写到productUrl
第四步会在指定时间点自动点击立即购买按钮，生成订单，此时需要自己付款

'''
#商城链接
mallUrl = 'https://www.taobao.com'
#商品链接
productUrl = 'https://chaoshi.detail.tmall.com/item.htm?spm=a1z0d.6639537.1997196601.3.700d7484lzpcWX&id=20739895092&skuId=4227830352490'
#抢购时间
buyTime = '2020-10-17 20:00:00.000000'


from selenium import webdriver
import datetime
import time
 
# driver = webdriver.Chrome(executable_path='C://Users//Administrator//Desktop//chromedriver.exe')
driver = webdriver.Chrome()
 
 
def login():
    # 打开淘宝登录页，并进行扫码登录
    driver.get(mallUrl)
    time.sleep(3)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()
 
    print("请在10秒内完成扫码")
    time.sleep(10)
    # 这里写你需要抢购商品的链接地址
    driver.get(productUrl)
    time.sleep(1)
 
 
def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now >= buytime:
            if driver.find_element_by_link_text("立即购买"):
                driver.find_element_by_link_text("立即购买").click()
                break
        else :
            print(now)
            # print("刷新新页面")
            # driver.refresh()
        time.sleep(0.0001)
    while True:
        try:
            if driver.find_element_by_link_text("提交订单"):
                driver.find_element_by_link_text("提交订单").click()
        except:
            time.sleep(1)
        print(now)
        time.sleep(0.0001)
 
 
if __name__ == "__main__":
    login()
    buy(buyTime)