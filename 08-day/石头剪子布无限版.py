#1----石头
#2----剪刀
#3----布
import random
while True:
	computer = random.randint (1,3)
	player = int(input("请出拳:1----石头    2----剪刀    3----布"))
	if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
		print("赢的人最帅")
	elif player == computer:
		print("再来一局")
	else:
		print("输啦！大娄碧！！")

