def func():
    print('我的my_module模块下func函数')


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart



class Test:
    def prt(self):
        print(self)
        print(self.__class__)


#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))