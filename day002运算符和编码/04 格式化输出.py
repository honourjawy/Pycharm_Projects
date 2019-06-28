s = "alex是一个很愚蠢的人"
print(s)

s1 = "wusir是一个很山炮的人"
print(s1)




name = "小白"
xingrong = "六"
s2 = name+"是一个很"+xingrong+"的人"      # 这句话就是一个格式
print(s2)





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




