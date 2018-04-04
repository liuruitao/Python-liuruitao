a = 1
while a <= 9:
	print('1*%d=%d '%(a,a),end = '')
	b = 2
	while b <= a and b <= 9:		
		print("%d*%d=%d "%(a,b,a*b),end = '')
		b+=1
	print('')
	a+=1
