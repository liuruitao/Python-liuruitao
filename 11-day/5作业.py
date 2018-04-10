list = []#设一个空列表放所有信息
name_list = []#设一个空列表放所有输入过的信息
count = 0#输入的次数
while True:
	if count == 3:#如果输入次数等于三次
		break#则跳出循环
	dict = {}#设一个空的字典
"""
	for i in list:
		name_list.append(i.get("名字"))
"""
	#输入：
	name = input("请输入名字:")
	age = int(input("请输入年龄:"))
	sex = input("请输入性别:")
	qq = int(input("请输入QQ号:"))
	weight = float(input("请输入体重:"))
	#给字典赋值
	if name not in name_list:#如果输入的名字不在第二个列表记录的名字里
		dict["名字"] = name
		dict["年龄"] = age
		dict["性别"] = sex
		dict["QQ号"] = qq
		dict["体重"] = weight
		list.append(dict)#将第一个放所有信息的列表放入字典
		name_list.append(name)#将第一个列表输入过的名字放入第二个列表并记录

		print(list)#打印第一个列表
		count+=1
	else:#如果输入的名字在第二个列表记录的名字里
		print("名字重复!")#则打印重复
age_sum = 0
#遍历第一个所有信息的列表
for i in list:
	age_sum = age_sum+i.get("年龄")
	print(i)
print("年龄平均值是:%d"%(age_sum/len(list)))
