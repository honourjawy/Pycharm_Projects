# # for 成员运算
# s1 = '老男孩edu'
# print('老' in s1)             # True
# print('老男' in s1)           # True
# print('老ed' in s1)           # False    # 必须挨着的(整体)!!!
# print('老ed' not in s1)       # True


# s1 = '老男孩教育最好的讲师：太白'     # 如何变成如下形式内容呢 ?
# '''
# 老      s1[0]
# 男      s1[1]
# 孩      s1[2]
# 教      s1[3]
# 育      ....
# 最
# ...
# '''
# 0~12位
# len :获取可迭代对象的元素总个数
# s1 = '老男孩教育最好的讲师：太白'
# print(len(s1))       # 13
#
# # 方法一:
# index = 0
# while index < 13:
#     print(s1[index])
#     index += 1
# # 方法二:   (引入len)
# index = 0
# while index < len(s1):
#     print(s1[index])
#     index += 1






# for 循环    ( 有限循环 )
#
# for 变量 in iterable:
#     pass
#
# s1 = '老男孩教育最好的讲师：太白'
# for i in s1:
#     print(i)
#
# s1 = '老男孩教育最好的讲师：太白'
# for i in s1:
#     print(i)
#     if i == '好':
#         break
#
# break continue
# for else  与  while else用法一样(break)


#
# fruits = ['banana', 'apple',  'mango']
# print(len(fruits))      # 3
#
# fruits = ['banana', 'apple',  'mango']
# for index in range(len(fruits)):
#    print('当前水果 :', fruits[index])
# # 运行结果:
# # 当前水果 : banana
# # 当前水果 : apple
# # 当前水果 : mango

# a = ['banana', 'apple',  'mango']
# for i in range(3):
#    print('当前水果 :', a[i])
#    # # 运行结果:
#    # 当前水果: banana
#    # 当前水果: apple
#    # 当前水果: mango