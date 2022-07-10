"""
定义函数
语法：def 函数名(位置参数，默认参数，不定长参数):
        函数体
        return 返回值
调用函数
语法：函数名(参数)
"""

"""
位置参数：调用函数时按照声明时的位置顺序依次传入的参数
"""
def fun1(a,b):
    return print("a是{}，b是{}".format(a,b))

"""
默认参数：默认参数没有传入时，则被认为是默认值；有传入时，则是传入的值
"""
def fun2(a,b=2):
    return print("a是{}，b是{}".format(a, b))


"""
不定长参数：传入的参数个数是可变的。
*arg:可变参数，接收的是一个tuple
**kw：关键字参数，接收的是一个dict
"""
def fun3(*args):
    sum=0
    for n in args:
        sum = sum + n * n
    return print("sum=",sum)

def fun4(**kwargs):
    return print(kwargs)
dict1={"name":"zhangsan","age":20,"sex":"male"}


def func(a,b):
    print(a+b)

def func1(a,b=2):
    print(a+b)

def func2(*args):
    print(args)
    print(args[0])

def func3(x,**kwargs):
    print(x)
    print(kwargs)
    print('总共有 %d 个参数'%len(kwargs))
    print('这些参数分别为：',kwargs)


if __name__ == '__main__':
    func3(20,name='rose',age=18)
    fun1(1,2)
    fun1(2,1)
    fun2(1)
    fun2(1,3)
    fun3(1)
    fun3(1, 2, 3)
    fun3(*(1, 2, 3))
    fun4(**dict1)
    fun1(b=1, a=2)

#    func(1, 2)
#    func1(1)
#    func1(1, 4)
#    func2('P','y','t','h','o','n')
#    func2('Python','123','爬虫')
#    func2(*(1,2,3))



















