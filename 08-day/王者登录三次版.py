account = input("请输入您的账号:")
pwd = input("请输入您的密码:")
cishu = 1
if account == "liuruitao" and pwd == "123456":
	print("登录成功")
	l = int(input("请选择英雄范围:0--ADC、1--肉、2--法师"))
	if l == 0:
		print("鲁班大师")
	elif l == 1:
		print("陈咬金")
	elif l == 2:
		print("王昭君")
else:
	while cishu <= 3:
		print("第%d次输入:"%cishu)
		account = input("请再次输入您的账号:")
		pwd = input("请再次输入您的密码:")
		cishu+=1
	print("账号已冻结")
