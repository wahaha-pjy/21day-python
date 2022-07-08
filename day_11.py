
"""
json ⇄字典
"""
#json→dict
a={'name':'zhangsan','sex':'male','age':30}
b=json.dumps(a)
print("b={},类型是{}".format(b,type(b)))
#dict→json
a='{"name":"zhangsan","sex":"male","age":30}'
b=json.loads(a)
print("b={},类型是{}".format(b,type(b)))