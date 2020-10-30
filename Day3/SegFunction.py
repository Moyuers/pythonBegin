'''
分段函数求值
f（x）= 3x-5 (x>1)
        x+2 (-1<=x<=1)
        5x+3 (x<-1)
'''
x=float(input('请输入x的值：'))
if x>1:
    y=3*x-5
else:
    if x>=-1:
        y=x+2
    else:
        y=5*x+3
print('f(%.2f)=%.2f'%(x,y))