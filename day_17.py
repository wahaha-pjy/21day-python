"""
filter(函数，序列)，
使用序列中的每个元素作为参数调用函数，返回每次调用函数的结果为true的值组成的迭代器
用list()转换成列表
"""

def odd(x):
    """判断是否是奇数"""
    return x % 2 == 1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = list(filter(odd, list1))
print("list2=", list2)

#与lambda函数结合
list2=list(filter(lambda x:x%2==1,range(10)))
print("list2=", list2)