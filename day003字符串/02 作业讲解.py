print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
print(8 or 3 and 4 or 2 and 0 or 9 and 7)
print(0 or 2 and 3 and 4 or 6 and 0 or 3)


print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)




while True:
    n = 66
    num = int(input("请猜:"))
    if num > n:
        print("猜大了")
    elif num < n:
        print("猜小了")
    else:
        print("猜对了")
        break


from random import  randint
count = 1
n = randint(1, 100)
while count <= 3:
    num = int(input("请猜:"))
    if num > n:
        print("猜大了")
    elif num < n:
        print("猜小了")
    else:
        print("猜对了")
        break
    count = count + 1
else:
    print("太笨了")


# count = 1
# while count <= 10:
#     if count != 7:
#         print(count)
#     count += 1

# count = 1
# while count <= 10:
#     if count == 7:
#         count += 1
#         continue # 停止当前本次循环. 继续执行下一次循环
#     print(count)
#     count += 1


# count = 1
# sum = 0
# while count <= 100:
#     sum += count
#     count += 1
# print(sum)

# count = 2
# while count <= 100:
#     print(count)
#     count += 2

# count = 1
# while count <= 100:
#     if count % 2 == 0:
#         print(count)
#     count += 1


# 1+3+5+7+9....+99 - 2-4-6-8-10
#
# sum = 0
# count = 1
# while count <= 100:
#     if count % 2 == 1: # 奇数
#         sum += count
#     else: # 偶数
#         sum -= count
#     count += 1
# print(sum)





# count = 1
# while count <= 3:
#     # 让用户输入用户名和密码
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#     if username == 'alex' and password == '123':
#         print("恭喜你, 登录成功!")
#         break
#     else:
#         print("用户名或密码错误!")
#     print("当前登录了%s次, 剩余%s次" % (count, 3-count))
#     count = count + 1



ads = input("请输入你的广告标语:")
if "最" in ads or "第一" in ads or "稀缺" in ads or "国家级" in ads:
    print("不合法的广告")
else:
    print("合法的广告")
