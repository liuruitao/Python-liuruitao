while True:
	x = int(input("请输入第一个数字:"))
	y = int(input("请输入第二个数字:"))
	sum = 0
	if x < y:
		for i in range(x,y+1):
			print(i)
			sum = sum+i
		print(sum)
		break
	else:
		print('第一个数字不能大于第二个数字！')
