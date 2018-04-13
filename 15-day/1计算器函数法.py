def jisuanqi(x,y,l):#形参
	if l == 1:
		z=x+y
	elif l == 2:
		z=x-y
	elif l == 3:
		z=x*y
	elif l == 4:
		if y != 0:
			z=x/y
		else:
			return "输入有误"
	elif l == 5:
		z=x**y
		return z
while True:
	x = int(input("请输入一个数字:"))
	y = int(input("请再输入一个数字:"))
	l = int(input("请选择一种运算方式:1.+ 2.- 3.* 4./ 5.**"))
	jisuanqi(x,y,j)#实参
