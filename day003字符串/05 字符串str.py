# s = '刘德华很帅但是张国荣更'
# print(s[2])
# print(s[11])
# print(s[-5]) # 倒数第一
# print(s[-4]+s[-3]+s[-2])

# 切片 s[start: end] 顾头不顾尾
# print(s[7:10])
# print(s[0:3])
# print(s[-4:-1])
# print(s[-1:-4]) # 默认的方向是从左往右切.
# 从德开始切. 切到结尾
# print(s[1:]) # 末尾
# print(s[:4]) # 开头
# print(s[:])

# s = "我要开始玩幺蛾子了你们怕不怕我很怕"
# print(s[1:5])
# print(s[5:1:-1])
# 第三个参数是步长
# print(s[1:5:3])
# print(s[4:8:2])
# print(s[::2]) # 02468
# print(s[-1:-6:-2])
# print(s[::-3])
# print(s[::-1])

# s = ""  # 回文
# s1 = s[::-1]
# if s == s1:
#     print("是回文")
# else:
#     print("不是回文")

# 切片: str[start : end : step]
# start: 起始位置
# end: 结束位置 顾头不顾尾
# step: 步长 默认是1. 从左往右取.   -1 从右往左取
