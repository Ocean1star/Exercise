
def input_str(TempStr):
    if TempStr[-1] in ['F','f']:
        C = (eval(TempStr[0:-1])-32)/1.8
        print("转换后的温度为：{:.2f}C".format(C))
    elif TempStr[-1] in ['C','c']:
        F = eval(TempStr[0:-1])+32
        print("转换后的温度为：{:.2f}F".format(F))
    else:
        print("输入格式错误")

if __name__ == '__main__':
    TempStr = input("请输入带符号的温度值：")
    input_str(TempStr)