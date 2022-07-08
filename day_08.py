#string和int类型互转
"""
字符串转换整型
语法：int(x, base)，x表示字符串或数字，base表示进制数（默认十进制）
"""
a = '21'
b = int(a)      #10进制字符串转换
c = int(a,16)   #16进制字符串转换
print("b={},c={}".format(b,c))

"""
整型转换字符串
语法：
转换成10进制字符串：str(x)，x可以是：数字，字符串，列表，字典等对象
转换成16进制字符串：hex(x)
"""
a = 21
b = str(a)   #转换成10进制字符串
c = hex(a)  #转换成16进制字符串
print("b={},c={}".format(b,c))

list2=[ 'java','python','c++']
print(','.join(list2))

str1="hello world ！"
list1=list(str1)
print(list1)

list2=str1.split(" ")
print(list2)