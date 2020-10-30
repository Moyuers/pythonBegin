'''
找出10000以内的完美数
'''
for i in range(2,10001):
    sum=0
    for j in range(i-1,0,-1):
        if i%j==0:
            sum+=j
    if sum==i:
        print(i)