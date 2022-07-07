"""

"""


tuple1=('java','python','c++')
list2=list(tuple1)
print("list2={},类型是{}".format(list2,type(list2)))

dict1={'name':'张三','age':25,'sex':'male'}
list1=list(dict1.keys())
print('list1=',list1)
list2=list(dict1.values())
print('list2=',list2)

set1= {1, 2, 3, 4, 5}
list1=list(set1)
print("list1=",list1)
list1= [1, 2, 3, 4, 5]
tuple1=tuple(list1)
print("tuple1=",tuple1)

list1 = [1, 3, 4, 3, 2, 1]
set1=set(list1)
print("set1=",set1)

list1= ['name', 'age', 'sex']
list2= ['张三', 25, 'male']
dict1=dict(zip(list1,list2))
print("dict1=",dict1)