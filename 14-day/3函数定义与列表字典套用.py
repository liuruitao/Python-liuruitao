def xxx():
	list = [{"biejiang":{"mianji":1290,"renkou":123123},"shamghai":{"mianji":12331,"renkou":123124}}]
	for i in list:
		#遍历列表
		print(i)
		for k,v in i.items():#遍历大字典
 			#遍历键值对时后要跟.items
			print(k)
			print(v)
			for j,l in v.items():#遍历小字典
				#v还是一个字典，遍历v的键值对
				print(k,j,l)
xxx()
