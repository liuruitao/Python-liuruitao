def koujue():
	for i in range(1,10):
		for x in range(1,i+1):
			print('%d*%d=%d '%(i,x,x*i),end = '')
		print('')
koujue()
