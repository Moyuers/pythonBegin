'''
打印不同的三角形
'''
row=int(input('输入行数：'))
for i in range(row):
    for j in range(i+1):
        print('*',end='')
    print()
for i in range(row):
    for j in range(row):
        if(j<row-i-1):
            print(' ',end='')
        else:
            print("*",end='')
    print()
for i in range(row):
    for j in range(row-i-1):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    print()