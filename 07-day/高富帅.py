height = int(input("请输入身高:"))
money = int(input("请输入身价:"))
ss = int(input("请输入颜值分:"))
if hieght >= 180 and money <10 and ss >=90:
	print("高帅")
elif hieght >= 180 and money > 1000000 and ss >= 90:
	print("高富帅！！！！")
elif hieght < 180 and money > 1000000 and ss >= 90:
	print("富帅~~")
elif height < 180 and money < 1000000 and ss >= 90:
	print("帅的连渣都不剩")
elif height < 160 and money < 100 and ss < 60:
	print("渣渣")
