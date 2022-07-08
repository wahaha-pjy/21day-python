#生成器,创建方式1：将一个列表推导式的[]改成()
g= (i**2 for i in range(1,11))
print(type(g))

for i in g:
    print("g=",next(g))
