# print("你好,请输入正确密码,密码错误3次,则系统结束")
# count = 1
# while count <= 3:
#     s='123456'
#     if s == input('请输入密码:'):
#         print('密码输入正确')
#     else:
#         print('密码输入错误')
#     count = count + 1



#
# # 让用户输入 名字， 年龄， 爱好 。格式化输出成   我叫xxx，
# # 我喜欢干xxxx。 我今年xxx大了
# name = input('请输入姓名:')
# age = input('请输入年龄:')
# hobby = input('请输入爱好:')
# print("我叫%s， 我喜欢干%s, 我今年%d岁了" % (name, hobby, int(age)))             # %d 必须占位数字
# # print("我叫%s， 我喜欢干%s, 我今年%s岁了" % (name, hobby, age))           # %s 都可以,简单







# 当字符串中出现了占位符。 那么想要使用%。 必须写%%
# 这句话是错的,请找出来并在下面改正:    print("我叫%s, 我已经学习python15%了" % ("刘伟"))
# print("我叫%s, 我已经学习python15%%了" % ("刘伟"))
# print("我们大家已经学习了15%的内容了")                    # 当字符串中'不出现占位符',那行了



# print(False and 3 or 6)

# yourname = 'jawy'
# yourpassword = '123'
# count = 1
# while count <= 3:
#     name = input('请输入姓名:')
#     password = input('请输入密码:')
#     if name == yourname:
#         if password == yourpassword:
#             print('成功登陆')
#             break
#         else:
#             print('密码错误')
#     else:
#         print('姓名输入错误')
#     count+=1


# count = 1
# while count <=3:
#     username = input('请输入名字:')
#     password = input('请输入密码:')
#     if password == '123456' and username == 'jawy':
#         print('登陆成功')
#         break
#     else:
#         print('密码输入错误,还剩下%s次机会' %(3-count))
#     count+=1
#




s111 = 'python全栈22期'
s00 = s111[0:5]        # 顾头不顾屁股所以只能pytho
s11 = s111[0:6]        # 顾头不顾屁股,必须5+1 ----> python
s22 = s111[:6]         #  [0:6]   ---->   [:6]    若从开头取,则可省略0
s33 = s111[6:-2]
s99 = s111[6:]
s55 = s111[-2:6]
s66 = s111[-2:0]
s88 = s111[-2:]


print(s55)          #
# print(s55)          #
# print(s66)          #2期
# print(s88)          #