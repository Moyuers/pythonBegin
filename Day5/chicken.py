'''
百钱百鸡问题
'''
for child in range(0,101,3):
    for m in range(101-child):
        f=100-child-m
        if child/3+m*5+f*3==100:
            print('公鸡%d只，母鸡%d只，小鸡%d只'%(m,f,child))
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))