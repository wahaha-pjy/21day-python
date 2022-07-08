"""整数int，允许用_分隔"""
a =2
b = 9_999_000

"""浮点数：小数。"""
c = 2.22

"""字符串：以引号括起来的任意文本。转义符\;用r''括起来的字符串默认不转义 """
d = 'Hello world!'
e = '\"Hello world!\"'

"""给变量赋值a=1：解释器线创建整数1和变量a，并把a指向整数1"""
"""除法"""
f = 10/3    #除法
g = 10//3   #只取结果的整数部分
h = 10%3    #只取结果的余数部分

"""print(a,b,c,d,e)
print(f,g,h)"""

"""list是一种有序的集合，可以随时添加和删除其中的元素。"""
list1=['yi','er','san']
y=list1[1]  #list[索引]：访问列表元素，索引从0开始，-1表示倒数第一的元素
list1.append('si')  #.append('元素')：在列表末尾追加元素
list1.insert(1,'二') #.insert(索引,'元素')：在指定索引位置插入元素
list1.pop(1)    #.pop(索引)：删除列表指定位置的元素，可接着使用被删元素的值
l=len(list1)    #len(列表)：获取列表的长度
print(y,list1,l)

"""tuple元组：初始化后就不能修改"""
t=(1,2)
print(t)

"""
dict字典：使用键-值（key-value）存储，具有极快的查找速度。
和list比较，dict有以下几个特点：
查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：
查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
"""
di = {'key1':'value1','key2':'value2','key3':'value3'}
v=di["key1"]    #dict[key]：获取key对应的值
k=di.get('key1')   #dict.get(key)：获取key对应的值
di['key4']='value4' #dict[key]=value：key不存在则添加key-value，存在则修改key对应的值
di.pop('key4')    #.pop(key)：删除键值对
print(v,k,di)

l=['h','e','l','l','o']
print(l)

d11={'key':'value','year':2022,'month':6,'day':21}
print(d11)

