'''
生成斐波那契数列前20个数
'''
for i in range(20):
    if i==0 or i==1:
        num=1
        a,b=1,1
        print('f%d=%d'%(i+1,num))
    else:
        num=a+b
        print('f%d=%d'%(i+1,num))
        a,b=b,num