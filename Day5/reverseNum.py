'''
将一个正整数逆转
'''
num=int(input("num="))
reverseNum=0
while num>0:
    reverseNum=reverseNum*10+num%10
    num//=10
print(reverseNum)