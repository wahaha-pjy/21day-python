import random
import string

"""
string.ascii_letters:生成所有字母，从a-z和A-Z
string.digits:生成所有数字0-9.
"""
d=string.ascii_letters
print("d=",d)
f=string.digits
print("f=",f)

"""
random.sample的用法，多用于截取序列指定长度的随机数，但是不会改变序列本身的排序
random.sample(x,n)：x可以是：列表，元组，字符串，集合。n=长度
"""
list1=[1,2,3,4,5]
c=random.sample(list1,2)
print("c=",c)

"""
"指定字符". join()：将序列中的元素以指定的字符连接生成一个新的字符串
"""
list2=['hello','world','!']
e="&".join(list2)
print(e)

"""
写出6位的包含大小写在内的随机字符串
"""
a="".join(random.sample(string.ascii_letters,6))
print("a=",a)

"""
写出8位的包含数字的随机数字
"""
b="".join(random.sample(string.digits,8))
print("b=",b)
g="".join(random.sample(string.digits+string.ascii_letters,8))
print("g=",g)