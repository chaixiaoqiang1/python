# 1.测试url请求获取数据  以及利用pip 下载包
from urllib import request
resp = request.urlopen("http://www.baidu.com")
print(resp.read().decode('utf-8'))