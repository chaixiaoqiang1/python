from bs4 import BeautifulSoup

# soup = BeautifulSoup(open("index.html"))
# print(soup)

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b

print(tag)
print(type(tag))