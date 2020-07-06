for i in range(3):
    str1 = input("请输入要转换的温度：")

    if str1[-1] in ['F', 'f']:
        C = (eval(str1[0:-1])-32)/1.8
        print("{:.2f}C".format(C))
    elif str1[-1] in ['C', 'c']:
        F = eval(str1[0:-1])*1.8+32
        print("{:.2f}".format(F))
    else:
        print("输入格式错误，请重新输入：")







