i = 10
if i>5:
    """如果i>5，打印i的值"""
    print('i=',i)

if i<5:
    """如果i<5，打印i<5"""
    print('i<5')


i=3
if i>5:
    """如果i>5,打印i的值"""
    print('i=', i)
else:
    """如果i<5，打印i<5"""
    print('i<5')

i=3
if i>5:
    """如果i>5,打印i的值"""
    print('i=', i)
elif i==5:
    """如果i=5，打印你好"""
    print('你好')
else:
    """如果i<5，打印i<5"""
    print('i<5')

i=30
if i<10:
    if i>5:
        print(i,'大于5小于10')
    else:
        print(i,'小于或等于5')
elif i>10:
    if i<20:
        print(i, '大于10小于20')
else:
    print('所以i是什么鬼')