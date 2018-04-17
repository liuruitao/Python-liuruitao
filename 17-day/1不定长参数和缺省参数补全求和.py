
def sum1(a,b,*args,**kwargs):
	all_sum = 0
	c = a+b
	print(a)
	print(b)
	print(args)
	print(kwargs)
	all_sum+=c
	return c
	for i in args:
		all_sum+=i
	for j in kwargs.values():
		all_sum+=j
	print(all_sum)
t = (3,4,5)
d = {"age":22}
sum1(1,2,*t,**d)




def sum3(a,b):
	c=a+b
	print(c)
def sum4(a,b,*args,**kwargs):
	all_sum=0
	c=a+b
	print(args)
	print(kwargs)
	for i in args:
		all_sum+=i
	for i in kwargs.values():
		all_sum+=i
	print(all_sum)
sum3(1,2)
sum4(1,2,3,4,5,age=22)
