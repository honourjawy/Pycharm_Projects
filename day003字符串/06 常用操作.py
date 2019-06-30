# s = "太白金星"
# s2 = s[::-1]
# print(s)

# s = "alex is not a good man! Tory is a good man"
# # s1 = s.capitalize()  # 首字母大写
#
# s1 = s.lower()
# s2 = s1.upper() # 转化成大写字母. 要求记住. 使用场景: 忽略大小写的时候需要
#
# print(s2)

# while True:
#     content = input("请输入你要喷的内容(输入Q退出):")
#     if content.upper() == 'Q': # 当用户输入q或者Q的时候退出. 这里要忽略大小写
#         break
#     print(content)


# s = "alex is not a good man! Tory is a good man"
# s1 = s.swapcase()  # 大小写互换
# print(s1)

# s2 = "БBß" # 俄美德
# print(s2)
# print(s2.lower())
# print(s2.casefold()) # 都转化成小写. 支持的文字比lower多


# s = "class app_le banana ora1nge pear alex wusir"
# s1 = s.title() # 标题.把单词的首字母大写
# print(s1)


# s = "刘伟"
# s1 = s.center(4,"*") # 把字符串拉长成4个单位 用*扩充
# print(s1)


# s = " \t       你好啊. 我叫赛利亚       "
# print(s)
# s1 = s.strip() # 去掉空白
# print(s1)

# 模拟登陆
# 用户输入的内容是无法保证合法的. 需要进行处理和判断
# username = input("请输入用户名:").strip()
# password = input("请输入密码:").strip()
# if username == "alex" and password == "123":
#     print("成功")
# else:
#     print("失败")


# s = "刘伟很帅刘伟"
# print(s.strip("伟"))


# s = "alex_wusir_ritian_taibai_evaj_eggon"
# # s1 = s.replace("taibai", "taihei")
# s1 = s.replace("i", "SB", 2)
# print(s1)

# s = "alex_wusir_ritian_taibai_evaj_eggon"
# lst = s.split("_") # 刀有多宽 就要损失掉多少
# print(lst)

# print("周润发\n周星驰周笔畅周杰伦")  # \n 是换行

# s = "周润发周星驰周笔畅周杰伦"
# lst = s.split("周润发周星驰周笔畅周杰伦")  # 切割的内容在边上. 会出现空字符串
# print(lst)

# 格式化输出
# print("我叫%s, 我今年%d岁了, 我喜欢干%s" % ("alex", 18, "python"))
# print("我叫{}, 我今年{}岁了, 我喜欢干{}".format("alex", 18, "python"))
# print("我叫{0}, 我今年{1}岁了, 我喜欢干{2}".format("alex", 18, "python"))
# print("我叫{name}, 我今年{age}岁了, 我喜欢干{hobby}".format(name="alex", age=18, hobby="python"))

# s = "今天的内容非常简单.你们信吗? 作业也很容易. 就是整理不太好"
# print(s.startswith("太好了"))
# print(s.endswith("太好了"))
#              啤酒
# s = "胡辣汤炸鸡啤酒烤鸭酱肘锅包肉炸鸡炸鸡炸鸡"
# # print(s.count("炸鸡")) # 计数
# print(s.find("疙瘩汤")) # 如果找不到返回-1  用这个
# print(s.index("疙瘩汤")) # 如果找不到报错.


# s = "一二壹贰叁肆萬两"
# print(s.isnumeric())

# s = "我是上帝, 你也是上帝"
# print(len(s)) # 内置函数len(字符串) 返回给你字符串的长度

