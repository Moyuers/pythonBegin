'''
Craps赌博游戏
设定玩家开始游戏时有1000元赌注
游戏结束的条件是玩家输光所有的赌注
'''
from random import randint
money=1000
while money>0:
    print("你的资产为：",money)
    goon=False
    while True:
        debt=int(input('请下注：'))
        if 0<debt<=money:
            break
    first=randint(1,6)+randint(1,6)
    print('第一次摇出了%d点'%first)
    if first==7 or first==11:
        print('玩家胜')
        money+=debt
    elif first==2 or first==3 or first==11:
        print('庄家胜')
        money-=debt
    else:
        goon=True
    while goon:
        goon=False
        dot=randint(1,6)+randint(1,6)
        print('摇出了%d点'%dot)
        if dot==7:
            print("庄家胜")
            money-=debt
        elif dot==first:
            print('玩家胜')
            money+=debt
        else:
            goon=True
print('余额不足，游戏结束')