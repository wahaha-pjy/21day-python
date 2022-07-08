data_string='hello world!'

# 字符串的截取:str[start : end : step]
# str：要截取的字符串；
# start：表示要截取的第一个字符所在的索引（截取时包含该字符）。如果不指定，默认为 0，也就是从字符串的开头截取；
# end：表示要截取的最后一个字符所在的索引（截取时不包含该字符）。如果不指定，默认为字符串的长度；
# step：指的是从 start 索引处的字符开始，每 step 个距离获取一个字符，直至 end 索引出的字符。step 默认值为 1，当省略该值时，最后一个冒号也可以省略。

a=data_string[:]
print('data_string[:]=',a)
b = data_string[1:9]
print('data_string[1:9]=',b)
c = data_string[:-1]
print('data_string[:-1]=',c)
d=data_string[0:]
print('data_string[0:]=',d)
e=data_string[::-1]
print('data_string[::-1]=',e)

print(data_string+'你好，世界')
print(data_string*5)
print('占位符%s。'%data_string)
