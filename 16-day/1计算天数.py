def sum_day(date):  #定义天数函数
	all_day = 0   #定义一个天数总和的变量
	year = int(date[0:4])  #进行切片确定年的位置
	month = int(date[4:6])	#切片确定月的位置
	day = int(date[6:])		#切片确定日的位置
	flag = 0 #假设是平年
	if (year%4 == 0 and year%100 != 0) or year%400 == 0:	#条件
		flag = 1	#如果是闰年
	big_month = [1,3,5,7,8,10,12]	#大月是
	small_month = [4,6,9,11]	#小月是
	for i in range(1,month):	#遍历一到指定月
		if i in big_month:		#如果是大月则是31天
			all_day+=31			
		elif i in small_month:	#如果是小月则是30天
			all_day+=30	
		if i==2 and flag==1:	#如果是闰年的2月则是29天
			all_day+=29
		elif i==2:				#否则即平年的2月是28天
			all_day+=28
	all_day+=day				#最后再加剩余的几天
	print("天数是%d"%all_day)	#打印
sum_day("20180603")				#调用函数并添加参数即要算的日期

