"""
map(函数，序列)：使用序列中的每个元素作为参数调用函数，返回每次调用函数的结果组成的迭代器
"""
def fun(x):
    """计算平方数"""
    return x ** 2
list1=[1,2,3,4,5]

#求list1中每个数的平方
g = map(fun,list1)

print("g-",g)
list2=list(g)
print("list2=",list2)

"""
lamba函数
语法：lamba [参数] ：表达式
"""
sum = lambda x,y : x+y
print("1+2=",sum(1,2))

"""
map()+lambda函数
"""
list1=[1,2,3,4,5]
#求list1内元素的平方
g1 = map(lambda n: n**2,list1)
print("g1=",list(g1))