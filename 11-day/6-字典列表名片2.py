print("名片系统v1.0版本".center(30,"*"))
print("1:新增名片".center(30," "))
print("2:查找名片".center(30," "))
print("3:修改名片".center(30," "))
print("4:删除名片".center(30," "))
cards = [] #定义一个空列表保存记录输入的名字
while True:
	fun_number = int(input("请选择功能:"))
	if fun_number == 1:
		print("新增")
		flag = 0 #默认值，0表示输入的名字不在列表里面保存过
		card = {} #定义空字典
		name = input("请输入名字:")
		for temp in cards:  #遍历
			if name == temp["name"]:
				flag = 1 #1表示输入的名字在列表里面存在了
				break
		if flag == 1: #如果输入的名字存在了
			print("名字重复了!")
			continue
		job = input("请输入职位:")
		phone = int(input("请输入手机号:"))
		company = input("请输入公司名字:")
		address = input("请输入公司地址:")

		card["name"] = name
		card["job"] = job
		card["phone"] = phone
		card["company"] = company
		card["address"] = address
		cards.append(card)
		print("新增成功")
	elif fun_number == 2:
		print("查找")


	elif fun_number == 3:
		print("修改")
	elif fun_number == 4:
		print("删除")

