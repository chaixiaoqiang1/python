import re
data = re.search(r'hello','hello world')
print(data)
print(data.span())
print(data.end())
print(data.string)
print(data.group())
