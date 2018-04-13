def jisuanqi(x,y,z):#形参
	if l == 1:
		z=x+y
		print("两数之和是:%.02f"%z)
	elif l == 2:
		z=x-y
		print("两数之差是:%.02f"%z)
	elif l == 3:
		z=x*y
		print("两数之积是:%.02f"%z)
	elif l == 4:
		if y != 0:
			z=x/y
			print("两数之商是:%.02f"%z)
		else:
			print("输入不合法!")
	elif l == 5:
		z=x**y
		print("%d的%d次幂是:%.02f"%(x,y,z))
while True:
	x = int(input("请输入一个数字:"))
	y = int(input("请再输入一个数字:"))
	l = int(input("请选择一种运算方式:1.+ 2.- 3.* 4./ 5.**"))
	jisuanqi(x,y,l)#实参
