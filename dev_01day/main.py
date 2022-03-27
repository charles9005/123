def welcome():
    print("*************欢迎进入图书管理系统***************")
    print("1.显示所有图书\n2.添加图书\n3.删除图书\n4.修改图书\n5.退出")
    print("********************************************")


def get_choose_number():
    choose_number = input("请输入菜单编号:")
    if not choose_number.isdigit() or choose_number not in ["1","2","3","4","5"]:
        return -1
    return int(choose_number)

def main():
    while True:
        welcome()
        number = get_choose_number()
        if number == 1:
            pass
        elif number == 2:
            pass
        elif number == 3:
            pass
        elif number == 4:
            pass
        else:
            break




if __name__ == '__main__':
    main()