#字符串格式化

#不指定位置
print("我叫{}，今年{}岁。".format('张三',33))
#指定位置
print("我叫{1}，今年{0}岁。".format(33,'张三'))
#设置参数
print('我叫{name}，今年{age}岁。'.format(name='张三',age=33))
#通过元组设置参数
info=('张三',33)
print('我叫{0}，今年{1}岁。'.format(*info))
#通过列表设置参数
infolist=['张三',33]
infolist2=['李四',34]
print('我叫{0[0]},今年{0[1]}岁，{1[0]}是我哥。'.format(infolist,infolist2))
#通过字典设置参数
infos={'name':'张三','age':33}
print('我叫{name}，今年{age}岁。'.format(**infos))
"""
我叫张三，今年33岁。
"""


