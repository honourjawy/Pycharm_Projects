print(2 ** 3)
print(10 //3)
print(10 % 3)



print(3 == 6)
print(3 != 9)
print(3 >= 9)


# count += 1
count = 1
count += 1   # 等同于count = count + 1
print(count)




# and or not
# 1 在没有()的情况下，优先级：not > and > or，同一优先级从左至右依次计算
# 情况1：两边都是比较运算
print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)    # print(True or False)
print(2 < 1 or 3 < 4 and 4 > 5)     # print(False or True and False)
# 情况2：两边都是整数
# x or y:   没有0则取左,有0则自看,
# x and y:  没有0则取右,有0则自看
print(1 or 2)
print(3 or 0)
print(4 or 2)
print(-1 or 2)
print(0 or 2)
print(0 or 0)
#
print(1 and 9)
print(3 and 6)
print(4 and 0)
print(-1 and 1)
print(0 and 2)
print(0 and 0)
# 比较运算符  >  逻辑运算符
print(1 > 2 and 3 or 6)


# str ---> int  : 只能是纯数字组成的字符串
s1 = '00100'
print(int(s1))
# int ----> str
i1 = 100
print(str(i1),type(str(i1)))

# int  ---> bool  : 非零即True ，0为False。
i = 0
print(bool(i))
# bool ---> int
print(int(True))  # 1
print(int(False))  # 0

# 面试题：
print(1 and 2 or 3 and 4)

# 思考题：
print(1 > 2 and 3 or 6)
print(2**32)
print(7.6 * 1024 * 1024 * 8)


















#
# a = 10
# b = 20
# a += b     # a = a + b
# print(b)
#
# # and  并且的意思. 当左右两端同时为真。 运算的结果才能是真
# # or   或者的意思. 有一个为真。 结果就是真
# # not  非真即假， 非假即真.
# #
# print(2 > 3 and 4 < 6)
# print(10 < 6  or  9 > 7 or 5 > 8)
# print(not 5 > 6)
# # 面试题
# # 运算顺序 () =>           not   =>   and =>   or
# print(1 > 2 and 3 < 6 or 5 > 7 and 7 > 8 or 5 < 1 and 6 > 3)
#
# print(3 > 4 or 4<3 and 1 == 1)     # False
# print(1 < 2 and 3 < 4 or 1 > 2)  # True
# print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)    # True
# print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)   # False
# print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)     # False
# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)     # False
#
#
# print(0 or 1 and 2) #2
# # x or y 如果x为0 则返回y， 否则。 返回x   (0 or y)->y , (x or y)->x  前or      (0 and y)->0 , (x and y)->y  后and
# print(1 or 2)  # 1
# print(1 or 2)  # 1
# print(0 or 2)  #2
# print(1 or 2)  #1
# print(0 or 6)  #6
# print(1 or 2 or 0 or 3 or 5) #1,顺序来
# # and和or相反。
# print(1 or 2 and 3) #1
# print(1 > 2 and 3 or 5 and 4 > 6 ) # False   所以not->and->or 得:(无0)后and前or,True: 1,False: 0
# # True: 1
# # False: 0
#
# print(1 or 1 > 2 and 3 or 5 and 4 > 6) # 1

