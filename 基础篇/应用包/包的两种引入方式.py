# 包的使用方法
# 第一种方式  from 包 import 模块
from urllib import request
resp = request.urlopen("http://www.baidu.com")
print(resp.read().decode('utf-8'))

# 第二种方式  import 包.模块
import urllib.request
conn = urllib.request.urlopen("http://www.baidu.com")
print(conn.read().decode('utf-8'))
