"""
string与bytes互转
"""
#string转bytes
a = "21 python"
b=a.encode("utf-8")
print("b={},类型是{}".format(b,type(b)))

#bytes转string
a=b'21 python'
b=a.decode("utf-8")
print("b={},类型是{}".format(b,type(b)))
