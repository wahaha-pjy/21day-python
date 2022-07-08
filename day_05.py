data_list = [21,'day','python']
print('data_list[0]=',data_list[0])     #=21
print('data_list[-1]=',data_list[-1])    #=python
print('data_list[:-1]=',data_list[:-1])     #=[21,'day']
print('data_list[::-1]=',data_list[::-1])   #=['python','day',21]
data_list.append("hello world")     #=[21, 'day', 'python', 'hello world']
print(data_list)
data_list=data_list*2   #
print(data_list)
data_list[1:2]= 'may'
print(data_list)
data_list[1:2]= ['may']
print(data_list)
list1=[1,2,3,4,5]
print(list1[0],list1[1],list1[-1])
list1[1]=0
print(list1)
list2=[ 'java','python','c++']
list2.append('vb')
print(list2)
del list2[-1]
print(list2)
print(list1+list2)
print(list1[:-1])
print(list1[::2])

#在指定位置插入元素
list2.insert(1,'go')
print(list2)
#删除列表指定位置的值，删除的值可被访问
p=list2.pop(1)
print(p,list2)