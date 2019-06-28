print(1+2)
print(1-2)
print(1*2)
print(1/2)
print(1//2)
print(1%2)
print(1**2)

print(2**1)
print(2**2)
print(2**3)
print(2**4)
print(2**5)
print(2**6)
print(2**7)
print(2**8)
print(2**9)
print(2**10)

a = 10
b = 20
a += b     # a = a + b
print(b)

# and  并且的意思. 当左右两端同时为真。 运算的结果才能是真
# or   或者的意思. 有一个为真。 结果就是真
# not  非真即假， 非假即真.
#
print(2 > 3 and 4 < 6)
print(10 < 6  or  9 > 7 or 5 > 8)
print(not 5 > 6)
# 面试题
# 运算顺序 () =>           not   =>   and =>   or
print(1 > 2 and 3 < 6 or 5 > 7 and 7 > 8 or 5 < 1 and 6 > 3)

print(3 > 4 or 4<3 and 1 == 1)     # False
print(1 < 2 and 3 < 4 or 1 > 2)  # True
print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)    # True
print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)   # False
print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)     # False
print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)     # False


print(0 or 1 and 2) #2
# x or y 如果x为0 则返回y， 否则。 返回x   (0 or y)->y , (x or y)->x  前or      (0 and y)->0 , (x and y)->y  后and
print(1 or 2)  # 1
print(1 or 2)  # 1
print(0 or 2)  #2
print(1 or 2)  #1
print(0 or 6)  #6
print(1 or 2 or 0 or 3 or 5) #1,顺序来
# and和or相反。
print(1 or 2 and 3) #1
print(1 > 2 and 3 or 5 and 4 > 6 ) # False   所以not->and->or 得:(无0)后and前or,True: 1,False: 0
# True: 1
# False: 0

print(1 or 1 > 2 and 3 or 5 and 4 > 6) # 1

