print("学生成绩管理系统".center(30,"*"))
print("1:新增名片".center(30," "))
print("2:查找名片".center(30," "))
print("3:修改名片".center(30," "))
print("4:删除名片".center(30," "))
print("5:退出程序".center(30," "))
cards = [] #定义一个空列表保存记录输入的名字
while True:
    fun_number = int(input("请选择功能:"))
    if fun_number == 1:
        print("新增")
        flag = 0 #默认值，0表示输入的名字不在列表里面保存过
        card = {} #定义空字典
        name = input("请输入名字:")
        for temp in cards:  #遍历
            if name == temp["name"]:
                flag = 1 #1表示输入的名字在列表里面存在了
                break
        if flag == 1: #如果输入的名字存在了
            print("名字重复了!")
            continue
        job = input("请输入职位:")
        job = input("请输入职位:")
        phone = int(input("请输入手机号:"))
        company = input("请输入公司名字:")
        address = input("请输入公司地址:")

        card["name"] = name
        card["job"] = job
        card["phone"] = phone
        card["company"] = company
        card["address"] = address
        cards.append(card)
        print("新增成功")
    elif fun_number == 2:
        print("查找")
        name = input("请输入要查找的人:")
        flag = 0 #假设不在里面
        count = 0 #默认找到0次
        for temp in cards:
            if name == temp["name"]:
                count+=1
                flag = 1
                break
        if flag == 0:
            print("查无此人")
        else:
            print("姓名:%s\n职位:%s\n手机号:%s\n公司:%s\n地址:%s\n"%(cards[count-1]["name"],cards[count-1]["job"],cards[count-1]["phone"],cards[count-1]["company"],cards[count-1]["address"]))
    elif fun_number == 3:
        print("修改")
        name = input("请输入要修改的人员:")
        for temp in cards:
            if name == temp["name"]:
                print("1:修改名字".center(32,'*'))
                print("2:修改职位".center(32,'*'))
                print("3:修改手机号".center(31,'*'))
                print("4:修改公司名字".center(30,'*'))
                print("5:修改公司地址".center(30,'*'))
                change_num = int(input("请输入修改内容:"))
                if change_num == 1:
                    name = input("请输入新的名字:")
                    temp["name"] = name
                elif change_num == 2:
                    job = input("请输入新的职位:")
                    temp["job"] = job
				elif change_num == 3:
					phone = input("请输入新的手机号:")
					temp["phone"] = phone
                elif change_num == 4:
                    company = input("请输入新的公司名字:")
                    temp["company"] = company
                elif change_num == 5:
                    address = input("请输入新的公司地址:")
                    temp["address"] = address
                else:
                    print("输入有误!")
    elif fun_number == 4:
        print("删除")
        name = input("请输入要删除的名字:")
        for temp in cards:
            if name == temp["name"]:
                    flag = 1#找到了
                    sure_num = int(input("0--确认删除 1--返回"))
            if sure_num == 0:
                cards.remove(temp)#删除
                print("删除成功")
            break
        if flag == 0:
            print("查无此人")
    elif fun_number == 5:
        print("再见宝贝儿！")
        break                              
