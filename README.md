包安装方式【pip install 包模块名称】
python安装下载的源码包【python setup.py install】
删除包的方式 【pip uninstall 包模块名称】 | 还有一种方式是找到包手动删除

# 【目录】(包下载：https://pypi.python.org/pypi)

1、基础篇记录数据库操作,测试过的可以正常使用的包。
2、爬虫学习(http://python.jobbole.com/77878/)
gitbook
3、基础学习网站(https://wiki.python.org/moin/BeginnersGuide/Programmers)
4、for in循环(js是键，py是值)  exit()退出代码执行  open()打开文件 pass关键字(空语句,保持代码的完整性)
5、包的两种引入方式(基础篇\应用包\包的两种引入方式)



# 【编辑器】
1、自动换行(设置->编辑器->选项->自动换行)

模块就是文件,但是必须在同一目录下就可以import引入，引入名就是文件名
包就是目录 from 包 import 模块 | 使用方式：模块.(函数或类)

字符串连接符是‘+’

爬虫利用的包有(urllib、BeautifulSoup、pdfminer3k、pymysql)
requests、urllib2

self相当于php的this,多态(同一类人对同一件事有不同的看法)
python类没有继承任何类的情况下最好继承object类（python3已解决这个问题）


Python | 用Pyinstaller打包发布exe应用

-F 表示生成单个可执行文件
-w 表示去掉控制台窗口，这在GUI界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧！
-p 表示你自己自定义需要加载的类路径，一般情况下用不到
-i 表示可执行文件的图标