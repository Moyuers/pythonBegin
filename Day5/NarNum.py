'''
打印所有水仙花数
'''
for i in range(100,1000):
    a=i%10
    b=i//100
    c=(i%100)//10
    if a**3+b**3+c**3==i:
        print(i)