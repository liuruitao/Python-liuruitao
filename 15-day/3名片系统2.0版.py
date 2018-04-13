cards = []
def print_menu():
	print("名片系统v1.0版本".center(30,"*"))
	print("1:新增名片".center(30," "))
	print("2:查找名片".center(30," "))
	print("3:修改名片".center(30," "))
	print("4:删除名片".center(30," "))
	print("5:全部名片".center(30," "))
	print("6:退出程序".center(30," "))
def input_fun():
	while True:
		fun_num = int(input("请选择功能:"))
		if fun_num == 1:
			add_card()
		elif fun_num == 2:
			find_card()
		elif fun_num == 3:
			update_card()
		elif fun_num == 4:
			del_card()
		elif fun_num == 5:
			all_card()
		else:
			break
def add_card():#新增名片
	card = {}
	name = input("请输入名字:")
	job = input("请输入职位:")
	company = input("请输入公司:")
	phone = input("请输入手机号:")
	card["name"] = name
	card["job"] = job
	card["company"] = company
	card["phone"] = phone
	cards.append(card)
	print("添加成功")
	#rint(cards)

def find_card():#查找名片
	name = input("请输入要查找的名字:")
	flag = 0
	for temp in cards:
		if name == temp["name"]:
			flag = 1
			print("名字:%s\n职位:%s\n公司:%s\n电话:%s\n"%(temp["name"],temp["job"],temp["company"],temp["phone"]))
	if flag == 0:
		print("查无此人")
def update_card():#修改名片
	name = input("请输入要修改的名片:")
	flag = 0
	for temp in cards:
		if name == temp["name"]:
			flag = 1
			print("1:修改名字")
			print("2:修改职位")
			print("3:修改公司")
			print("4:修改电话")
			update_num = int(input("请输入要修改的选项"))
			if update_num == 1:
				new_name = input("请输入新的名字:")
				temp["name"] = new_name
			elif update_num == 2:
				new_job = input("请输入新的职位:")
				temp["job"] = new_job
			elif update_num == 3:
				new_company = input("请输入新的公司:")
				temp["company"] = new_company
			elif update_num == 4:
				new_phone = input("请输入新的手机号:")
				temp["phone"] = new_phone
			else:
				print("输入有误")
	if flag == 0:
		print("查无此人")
def del_card():#删除名片
	name = input("请选择要删除的名字:")
	flag = 0
	for temp in cards:
		if name == temp["name"]:
			flag = 1
			sure_num = int(input("0--确认删除  1--取消删除"))
		if sure_num == 0:
			cards.remove(temp)
			print("删除成功")
	if flag == 0:
		print("查无此人")
def all_card():#打印名片
	print("名字\n职位\n公司\n手机号")
	for temp in cards:
		print("%s\n%s\n%s\n%s"%(temp["name"],temp["job"],temp["company"],temp["phone"]))
def end_card():
	print("感谢使用")
print_menu()
input_fun()
end_card()
