
msg = '''------------ info of 太白金星  -----------
Name  : 太白金星
Age   : 18
job   : Teacher
Hobbie: girl
------------- end -----------------'''

msg1 = '''------------ info of 德刚  -----------
Name  : 德刚
Age   : 73
job   : Teacher
Hobbie: boy
------------- end -----------------'''

# 制作一个公共的模板
# 让一个字符串的某些位置变成动态可传入的。
# 格式化输出
# % 占位符  s --> str  d  i  r
name = input('请输入你的姓名：')
age = input('请输入你的年龄：')
job = input('请输入你的工作：')
hobby = input('请输入你的爱好：')
msg = '''------------ info of %s  -----------
Name  : %s
Age   : %d
job   : %s
Hobbie: %s
------------- end -----------------''' % (name, name, int(age), job, hobby)
print(msg)





# 坑：在格式化输出中，如果想表示一个百分号，而不是占位符使用,需要再加 %
msg = '我叫%s,今年%s,学习进度1%%' % ('太白金星', 18)
print(msg)














s = "alex是一个很愚蠢的人"
print(s)

s1 = "wusir是一个很山炮的人"
print(s1)









# %s占位是占的字符串. 可以占位任何内容
name = "alex"
xingrong = "愚蠢"
s = "%s是一个很%s的人" % (name, xingrong)
print(s)





# 让用户输入 名字， 年龄， 爱好 。格式化输出成   我叫xxx，
# 我喜欢干xxxx。 我今年xxx大了
name = "alex"
age = 18
hobby = "佩奇"
print("我叫%s， 我喜欢干%s, 我今年%d岁了" % (name, hobby, age)) # %d 必须占位数字
# print("我叫%s， 我喜欢干%s, 我今年%s岁了" % (name, hobby, age)) # %s 都可以,简单

# print("我叫%s, 我已经学习python15%了" % ("刘伟"))  # 当字符串中出现了占位符。 那么想要使用%。 必须写%%
print("我叫%s, 我已经学习python15%%了" % ("刘伟"))
print("我们大家已经学习了15%的内容了")   # 当字符串中不出现占位符,那行了

print(2**32)

name = "小白"
xingrong = "六"
s2 = name+"是一个很"+xingrong+"的人"      # 这句话就是一个格式
print(s2)


print(6666)

