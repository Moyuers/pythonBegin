'''
用户身份验证
'''
username=input('请输入用户名：')
password=input('请输入密码：')
# 用户名是admin且密码是123456则验证成功，否则验证失败
if username == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')