#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 11:23
# @Author  : Xinghai
# @FileName: dd.py
# @Software: PyCharm

if __name__ == '__main__':
    # num = int(input())
    # str_ = "Hello World"
    # if num == 0:
    #     print(str_)
    # elif num > 0:
    #     for i in range(len("Hello World")):
    #         if i % 2 == 0:
    #             print(str_[i],end="")
    #         else:
    #             print(str_[i])
    # else:
    #     for i in str_:
    #         print(i)
    # str_ = input()
    # print("{:.2f}".format(eval(str_)))
    # tempstr = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
    # str_ = input()
    # s=""
    # for i in str_:
    #     print(i)
    #     tp = tempstr[int(i)]
    #     s+=tp
    # print(s)
    str_ = input()
    if str_[:3] == "RMB":
        num = eval(str_[3:] )/ 6.78
        print("USD{:.2f}".format(num))
    else:
        num = eval(str_[3:] )* 6.78
        print("RMB{:.2f}".format(num))
