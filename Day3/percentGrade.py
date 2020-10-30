'''
百分制成绩转换为等级制
'''
score=float(input('请输入成绩：'))
if score<0 or score>100:
    print('成绩不合法')
elif score>=90:
    grade='A'
elif score>=80:
    grade='B'
elif score>=70:
    grade='C'
elif score>=60:
    grade='D'
else:
    grade='E'
print('对应的等级是：',grade)
