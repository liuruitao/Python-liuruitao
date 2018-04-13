list = []
def add_hero(hero):
	list.append(hero)
while True:
	if len(list) == 5:
		print(list)
		break
	name = input("请输入一个英雄:")
	add_hero(name)
