print("你是不是傻")
print("下路支援,你不来")


'''
while循环
while 条件:
    代码块
流程： 判断条件是否为真。 如果真， 执行代码块。
    然后再次判断条件是否为真 。如果真继续执行代码块。。。。
     直到条件变成了假。 循环退出 
'''
# 死循环: 永远都停不下来的
while True:
    print("!@#$%^&*")

# 喷10次
count = 1
while count <= 10000:     # 当count小于等于10的时候。 喷
    print("!@#$%^&*")
    count = count + 1     # count的作用：1. 计数  2.控制循环范围

# 从1-100
count = 1
while count <= 100:
    print(count)
    count = count + 1

# 求1+2+3+4+5+....+100 = ?
count = 1
sum = 0 # 最终的结果
while count <= 100:
    sum = sum + count   # 累加运算的思想
    count = count + 1
print(sum)




# 让用户输入喷的内容. 不停的喷*******
while True:
    content = input("请输入你要跟对方说的话(输入Q退出程序)：")
    if content == 'Q':
        exit(0) # 这个是彻底的退出程序,下面不执行。
        break # 打断的是当前本"层循环"->位置不一样,效果不一样  终止掉循环, 毁灭性的
        continue # 停止当前'本次'循环。 继续执行下一次循环 暂时性的,过滤无效的
    print(content)
print("我去吃饭了")


# count = 1
# while count <= 10:
#     print(count)
#     if count == 3:
#         break
#     count = count + 1
# else:  # 当条件不成立的时候执行
#     print("刘伟") # ???


content = input("请输入你的评论信息:")
if "金三胖" in content:  # xxx是否出现在xxx中
    print("对不起. 你的评论包含敏感词汇")
else:
    print("OK")
