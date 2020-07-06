#!/usr/bin/python
# -*- coding: UTF-8- -*-



for i in range(3):             #
    wen = input("温度值： ")
    if wen[-1] in ['C', 'c']:
        f = 1.8 * float(wen[0:]) + 32
        print("温度为: %.2fF"%f)
    elif wen[-1] in ['F', 'f']:
        c = (float(wen[0:]) - 32) / 1.8
        print("温度为： %.2fC"%c)
    else:
         print("输入有误")





