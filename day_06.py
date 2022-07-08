tuple1=('张三',33,[1,2])

data_tuple=(21,'day','python')
#索引
print('data_tuple[0]=',data_tuple[0])
print('data_tuple[-1]=',data_tuple[:-1])
#切片
print('data_tuple[:-1]=',data_tuple[:-1])
print('data_tuple[::-1]=',data_tuple[::-1])
#
tuple2=(1,)
print('一个元素的元组需要加逗号：tuple1=',tuple2)
#拆包
data_1,data_2,data_3=data_tuple
print('data1={0},data2={1},data3={2}'.format(data_1,data_2,data_3))
print('元组和列表的区别：列表可修改值、长度，元组不可修改')

#可变元组
tuple3=('a', 'b', ['X', 'Y'])
tuple3[2][0]='A'
tuple3[2][1]='B'
print(tuple3)