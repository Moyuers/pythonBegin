'''
猜数字游戏
'''
import random
answer=random.randint(1,100)
count=0
while True:
    count+=1
    number=int(input('请输入（1-100）：'))
    if number<answer:
        print('大一点')
    elif number>answer:
        print('小一点')
    else:
        print('恭喜你猜对了！')
        break
print('你总共猜了%d次'%count)
if count>7:
    print('你的智商余额不足')