def register(phone,pwd): #定义注册函数
	result = condition(phone) #结果和条件对比
	if result == True:  #如果结果等于返回值
		print("注册成功")
	else:   #结果不等于返回值
		print("注册失败")
def logon(phone,pwd): #定义登录函数
	result = condition(phone)
	if result:
		print("登录成功")
	else:
		print("登录失败")
def condition(phone): #条件
	if phone.startswith("1") and len(phone) == 11: #如果手机号开头是1并且长度为11
		return True #符合条件返回真值
	else:
		return False #不符合条件返回假值
#调用注册和登录函数
phone = input("请输入手机号:")
pwd = input("请输入密码:")
register(phone,pwd)
logon(phone,pwd)

