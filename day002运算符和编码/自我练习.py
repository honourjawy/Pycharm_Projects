print("你好,请输入正确密码,密码错误3次,则系统结束")
count = 1
while count <= 3:
    s='123456'
    if s == input('请输入密码:'):
        print('密码输入正确')
    else:
        print('密码输入错误')
    count = count + 1




# 让用户输入 名字， 年龄， 爱好 。格式化输出成   我叫xxx，
# 我喜欢干xxxx。 我今年xxx大了
name = input('请输入姓名:')
age = input('请输入年龄:')
hobby = input('请输入爱好:')
print("我叫%s， 我喜欢干%s, 我今年%d岁了" % (name, hobby, int(age)))             # %d 必须占位数字
# print("我叫%s， 我喜欢干%s, 我今年%s岁了" % (name, hobby, age))           # %s 都可以,简单







# 当字符串中出现了占位符。 那么想要使用%。 必须写%%
# 这句话是错的,请找出来并在下面改正:    print("我叫%s, 我已经学习python15%了" % ("刘伟"))
print("我叫%s, 我已经学习python15%%了" % ("刘伟"))
print("我们大家已经学习了15%的内容了")                    # 当字符串中'不出现占位符',那行了



