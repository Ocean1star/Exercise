import random
import math

history={}
max_try_num = math.log2(1024)
def guess_num(name,answer):
    if name not in history:
        history[name]=[]
    try_num = 0
    while try_num<2:
        try:
            number = int(input("请输入一个数字："))
        except:
            number = int(input("该数字不合法，请重新输入数字："))
        if number<answer:
            print("你猜测的数字小了")
        elif number==answer:
            print("猜测正确")
            history[name].append("成功")
            break
        else:
            print("你猜测的数字大了")
        try_num+=1
    else:
        print("猜测次数过多")
        history[name].append("失败")

def start():
    name = str(input("请输入游戏玩家名字："))
    answer = random.randint(0, 1024)
    guess_num(name,answer)

def show_histoary():
    if len(history)==0:
        print("无用户进行过游戏")
    else:
        tplt_l = "{0:^5}\t{1:^8}\t"
        print(tplt_l.format("玩家", "记录"))
        for n in history:
            res = ','.join(history[n])
            tplt = "{0:^5}\t{1:^8}\t"
            print(tplt.format(n,res))

if __name__ == '__main__':
    select_dict = {'1':show_histoary,'2':start,'3':exit}
    while True:
        select = input('1.历史记录\n2.继续游戏\n3.退出游戏\n请输入数字选择：')
        try:
            select_dict.get(select)()
        except:
            select = input('1.历史记录\n2.继续游戏\n3.退出游戏\n请保证数字正确，从上述列表中选择：')
            select_dict.get(select)()
