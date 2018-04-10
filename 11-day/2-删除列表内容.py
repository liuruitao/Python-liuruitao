"""
list = [1,2,3,4,5,6,7,8,9]
while range(len(list)):
	list.pop(0)
print(list)
"""
"""
list = [1,2,3,4,5,6,7,8,9]
for i in range(len(list)-1,-1,-1):
	list.pop(i)
print(list)
"""

list2 = [1,2,3,4,5,6,7,8,9]
new_list = list2[ : ]
for i in new_list:
	list2.remove(i)
print(list2)
