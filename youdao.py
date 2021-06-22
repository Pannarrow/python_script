import time
import hashlib
import random
import requests

# ts = 1595926050165
ts = int(time.time()*1000)
# print(ts)

# bv = 111da8c77c20f554a622d3632e1e051e
appVersion = '5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
bv = hashlib.md5(appVersion.encode("utf8")).hexdigest()
# print(bv)

# salt = 15959260501656
salt = ts + int(random.random()*10)
# print(salt)

# sign = 837cc5a0b4e647a185d82172ef18b862
word = '好的'
sign = hashlib.md5(("fanyideskweb" + word + str(salt) + "mmbP%A-r6U3Nw(n]BjuEU").encode("utf8")).hexdigest()
# print(sign)

data = {
    'i': word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'ts': ts,
    'bv': bv,
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION'
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '255',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=809374519.2120816; OUTFOX_SEARCH_USER_ID="-1233903585@10.108.160.19"; _ga=GA1.2.1218700643.1591259937; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcBKL26h_IO78iulJuox; _ntes_nnid=4c3527439e4de881bbb98a5c2a6e0d34,1595925157675; ___rl__test__cookies=1595925472788',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/?keyfrom=dict2.top',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

result = requests.post(url,headers = headers,data = data)
print(result.text)