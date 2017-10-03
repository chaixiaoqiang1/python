import urllib.request
import re

with urllib.request.urlopen('http://www.python.org/') as f:
    rs = f.read()


cp = re.compile(r'<img.*src=.*.png')
data = cp.search(str(rs))
print(data.group())

