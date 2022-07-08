
L=[1,2,3,11,2,5,3,2,5,3]
print(L)
L1=L[0:2]#切片从下标0开始，数2位数
print(L1)

#列表转换集合
L=set(L)
print(L)

#集合转换列表
L=list(L)
print(L)

str='hi hello world'
list1=list(str)
print(list1)
list2=list(str.split(' '))
print(list2)
str1=','.join(list2)
print(str1)

dict1={'a':1,'b':2,'c':3}
print(dict1)
list3=list(dict1.keys())
print(list3)
