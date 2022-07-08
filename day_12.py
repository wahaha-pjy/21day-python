#for循环
a=[]
for i in range(1,101):
    a.append(i)
print('a:',a)

#列表推导式
a=[i for i in range(1,11)]
print('a:',a)

#循环字符串
for i in "hello world":
    print(i)

#循环列表,默认取key
list1=['python','java','c++']
for i in list1:
    print("i=",i)

#循环字典
dict1={"name": "zhangsan", "sex": "male", "age": 30}
for i in dict1:
    print("i=",i)

#构建1-100的双数列表
b=[]
for i in range(1,11,2):
    b.append(i)
print(b)

