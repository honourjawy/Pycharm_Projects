# int  主要用于计算   + - * /
# 不同的进制之间的转换。10进制，2进制。


# 二进制转换成十进制
# 0001 1010    ----->   26
# 42           ----->   0010 1010

b = 1 * 2**4 + 1 * 2**3 + 0 * 2**2 + 1 * 2**1 + 0 * 2**0
print(b)                  # 26


# int
# bit_lenth 有效的二进制的长度
i = 4
print(i.bit_length())        # 3
i = 5
print(i.bit_length())        # 3
i = 42
print(i.bit_length())        # 4



# bool  <---> int
# True    1   False     0
# 非零即True    0 是 False
i = 5
print(bool(i))            # True
print(int(False))         # 0



# str   <--->   int
s1 = 10
print(int(s1))              # 必须是数字组成
i = 100
print(str(i))



# str ---> bool
# 非空即True
s8 = '965'
s5 = '0'
s6 = ' '            # 一个空格
s9 = ''             # 无空格
print(bool(s8))     # True
print(bool(s5))     # True
print(bool(s6))     # True
print(bool(s9))     # False



# bool  --?--> str       # 可以,但无意义
print(str(True))         # True为字符串


# 实现直接回车,实现-->没有输入任何内容
s = input('输入内容:')
if s:
    print('有内容')
else:
    print('没有输入任何内容')

