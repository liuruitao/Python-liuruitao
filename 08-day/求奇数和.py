count = 1
Sum = 0
while count <= 100:
	if count%2 == 1:
		print("当前数字是:%d"%count)
		count+=2
		Sum = count + Sum
print("当前和是:%d"%Sum)
