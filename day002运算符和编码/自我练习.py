print("你好,请输入正确密码,密码错误3次,则系统结束")
count = 1
while count <= 3:
    s='123456'
    if s == input('请输入密码:'):
        print('密码输入正确')
    else:
        print('密码输入错误')
    count = count + 1