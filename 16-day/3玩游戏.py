import time
def play():
	for i in range(5):
		print("fire")
		time.sleep(1)
	print("你爸爸来了")
	result = babalai()
	if result == "打扁了":
		print("死翘翘")
	else:
		print("还差一点")
def babalai():
	print("小兔崽子打游戏不叫我，削死你！")
	print("你妈妈也来了")
	mamalai()
	return "打扁了"


def mamalai():
	print("男女混合双打")



play()
