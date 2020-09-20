# while True:
#     content = input("请输入你要跟对方说的话或输入Q退出程序：")
#     if content == 'Q':
#         print(content)
#     break
# print("我去吃饭了啊")



# 有问题
# username = input('请输入姓名:')
# code = 'abcd'
# your_code = input('请输入密码:')
# if username == 'jawy':
#     if your_code == code:
#         if your_code != code:
#             print('密码错误')
#     print('登陆成功')
# else:
#     print('你的姓名有误!')


code = 'abcd'
username = input('请输入姓名:')
your_code = input('请输入密码:')
if username == 'jawy':
    if your_code == code:
        print('登陆成功')
    else:
        print('密码错误')
else:
    print('你的姓名有误!')