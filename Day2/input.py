'''
通过键盘输入两个整数来实现对其算数运算
'''
a=int(input('a='))
b=int(input('b='))
print('%d+%d=%d'%(a,b,a+b)) # %d是整数的占位符
print('%d-%d=%d'%(a,b,a-b))
print('%d*%d=%d'%(a,b,a*b))
print('%d/%d=%d'%(a,b,a/b))
print('%d/%d=%f'%(a,b,a/b)) # %f是浮点数的占位符
print('%d//%d=%d'%(a,b,a//b))
print('%d%%%d=%d'%(a,b,a%b)) # %%代表%，由于%代表了占位符
print('%d**%d=%d'%(a,b,a**b))