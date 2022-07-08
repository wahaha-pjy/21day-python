import json

#字符串与字典相互转换
"""
字符串转字典
"""
a="{'name':'idoxu','sex':'male','age':30}"
b=eval(a)
print("b={},类型是{}".format(b,type(b)))
str1="{'name':'张三','age':25}"
dict1=eval(str1)
print("dict1={},类型是{}".format(dict1,type(dict1)))


"""
字典转字符串
"""
a={'name':'idoxu','sex':'male','age':30}
b=str(a)
print("b={},类型是{}".format(b,type(b)))
dict1={'name':'张三','age':25}
str1=str(dict1)
print("str1={},类型是{}".format(str1,type(str1)))

"""
集合set
"""
list1=[1,2,3,4,5,4,3,2,1]
set1=set(list1)
print("set1=",set1)

set1= {1, 2, 3, 4, 5}
set2= {4, 5, 6, 7, 8, 9}
#求交集
set3=set1&set2
print("set3=",set3)
#求并集
set3=set1|set2
print("set3=",set3)
#求差集
set3=set1-set2
print("set3=",set3)
#求补集
set3=set1^set2
print("set3=",set3)

