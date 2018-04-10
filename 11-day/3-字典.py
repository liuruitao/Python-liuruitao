Id_Card = {"name":"刘瑞涛","age":'18',"height":177,"weight":120}
print(Id_Card)
Id_Card['mingzu'] = '汉'
print(Id_Card)
Id_Card.pop('name')
print(Id_Card)
Id_Card['age'] = '20'
print(Id_Card)
print(Id_Card['age'])
for i in Id_Card:
	print('%s:%s'%(i,Id_Card[i]))
