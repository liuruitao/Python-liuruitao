h = float(input("请输入身高(cm):"))
w = float(input("请输入体重(斤):"))
BMI = w/h**2
if BMI < 18.5:
	print("过轻")
elif BMI >= 18.5 and BMI < 25:
	print("正常")
elif BML >= 25 and BMI < 28:
	print("过重")
elif BML >= 28 and BMI < 32:
	print("肥胖")
elif BML >= 32:
	print("严重肥胖")
