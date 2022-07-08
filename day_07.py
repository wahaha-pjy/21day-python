#字典dict
data_dict={'location':'shenzhen','province':'guangzhou','age':'25'}
#访问字典内的值
print("data_dict['age']=",data_dict['age'])
#修改字典内的值
data_dict['sex']=1
print(data_dict)
data_dict["sex"]="女"
print(data_dict)
#删除字典内的值
del data_dict['sex']
print(data_dict)

dict1={'name':'张三', 'age': 25}
print("name=",dict1["name"])
print("name=",dict1.get("name"))

print("dict1.keys()=",dict1.keys())
print("dict1.values()=",dict1.values())

for i in dict1.keys():
    print(i)

for i in dict1.values():
    print(i)

for key,value in dict1.items():
    print(key,value)

#清空字典的值
#dict1.clear()
print(dict1)