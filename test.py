# 爬虫的小试验 看来是成功了  好开心
import urllib.request

conn = urllib.request.urlopen("http://www.baidu.com")
html_doc = conn.read().decode("utf-8")


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.p.contents[0].string)
print(soup.title.string) #获取标题内容
# for link in soup.find_all('a'):
#     print(link.get('href'))
#
