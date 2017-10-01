import my_module(同一目录下的文件名)
my_module.func()

# 包下面的模块引入方式  两种方式 一种是包下某个模块  一个是包下所有模块
from bao import mokuai
from 模块名(即目录名) import *(即包目录下的文件名,*代表目录下全部文件)

# 这个是来自my_module下的类
x = my_module.Complex(3.0, -4.5)
print(x.r, x.i)  # 输出结果：3.0 -4.5

# self 相当于PHP类中的this
b = my_module.Test()
b.prt()

c = my_module.people('苹果', 20, '香蕉')
c.speak()


# import my_module
#
# my_module.func()
# print(dir(my_module))
