import random
com_num = random.randint(1,100)
for i in range(1,10):
	number = int(input("请输入:"))
	if number > com_num:
		print("大了")
	elif number < com_num:
		print("小了")
	else:
		print("对了%d"%number)
	break
