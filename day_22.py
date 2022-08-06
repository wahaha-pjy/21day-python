#i = 0
#while i < 5:    #当i<7执行循环体内容
#  i += 1         #等同i=i+1
#  if i == 3:        #如果i=3，则跳过此次循环，开始下个循环
#    continue
#  print(i)


list1=[1,2,3,4,5]
for i in list1:
    if i == 3:     #如果i=3
        break    #跳过此次循环(print(i))，开始下个循环(i=4→for...)
    print(i)



n = 0
while n < 5:
  n += 1
  if n == 3:     #如果i=3，退出循环
    break
  print(n)
g= (i**2 for i in range(1,11))
print("g的类型是：",type(g))


def intNum():
  print("开始执行")
  for q in range(5):
    yield q
    print("继续执行")
num = intNum()
print("num的类型是",type(num))