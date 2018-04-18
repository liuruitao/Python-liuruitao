list = [1,5,6,7,8,12,30,45,60,62,75,80,90]
key = 75
center = int(len(list)/2)
if key in list:
	while True:	
		if list[center] < key:
			center = center + 1
		elif list[center] > key:
			center = center - 1
		elif list[center] == key:
			print("在数组的索引为%s的位置"%(center))
			break
list = [1,2,5,6,9,12,15,18,26,35,65,84,95]
print(list)
num = int(input("请数如数组里的一个数组:"))
center = int(len(list)/2)
if num in list:
	while True:
		if list[center] < num:
			center = center + 1
		elif list[center] > num:
			center = center - 1
		elif list[center] == num:
			print("该数在数组的索引为:%s"%center)
			break
else:
	print("该数不在数组内")

