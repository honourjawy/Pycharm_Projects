# # 列表的创建
# 方式一
l1 = [1, 2, 'Alex']
print(l1)   # [1, 2, 'Alex']

# 方式二
l2 = list()
l3 = list('fhsaf')
print(l2)   # []
print(l3)   # ['f', 'h', 's', 'a', 'f']

# 方式三：列表推导式 后面讲



# # # 增删改查

# case1:    append 追加的意思
l1 = ['太白', '女神', 'xiao','吴老师', '闫龙']
l1.append('xx')
print(l1)                   # ['太白', '女神', 'xiao', '吴老师', '闫龙', 'xx']
print(l1.append('xx'),type(l1.append('xx')))      # None <class 'NoneType'>     # 不能打印它,是个命令

# 举例：
l1 = ['太白', '女神', '吴老师', 'xiao', '闫龙']
while 1:                        # True就是 1
    name = input('请输入新员工姓名：(Q或者q退出程序):')
    if name.upper() == 'Q':
        break                   # 不能用exit
    l1.append(name)
print(l1)

# case2:    insert 插入
l1 = ['太白', '女神', 'xiao','吴老师', '闫龙']
l1.insert(2,'wusir')
print(l1)       # ['太白', '女神', 'wusir', 'xiao', '吴老师', '闫龙']

# case3:    extend 迭代着追加
l1 = ['太白', '女神', 'xiao','吴老师', '闫龙']
l1.extend('abcd')
print(l1)       # ['太白', '女神', 'xiao', '吴老师', '闫龙', 'a', 'b', 'c', 'd']
l1.extend(['alex'])
print(l1)       # ['太白', '女神', 'xiao', '吴老师', '闫龙', 'alex']
l1.extend(['alex', 1, 3])
print(l1)       # ['太白', '女神', 'xiao', '吴老师', '闫龙', 'alex', 1, 3]
l1.extend(['alex', 1, 3,[8,9]])
print(l1)         # ['太白', '女神', 'xiao', '吴老师', '闫龙', 'alex', 1, 3, [8, 9]]

# # 删
# case1:    pop 按照索引位置删除
l1 = ['太白', '女神', '吴老师', 'xiao', '闫龙']
l1.pop(-2)            # 按照索引删除 （返回的是删除的元素!!!）
print(l1.pop(-2))     # 吴老师      （返回的是删除的元素!!!）
print(l1)             # ['太白', '女神', '闫龙']

a1 = ['太白', '女神', '吴老师', 'xiao', '闫龙']
a1.pop()              # 默认删除最后一个
print(a1)             # ['太白', '女神', '吴老师', 'xiao']


# case2:    remove  指定元素删除, 如果有重名元素，默认删除从左数第一个
l1 = ['xiao', '太白', '女神', '吴老师', 'xiao', '闫龙','xiao' ]
l1.remove('xiao')   # 有重名元素，默认删除从左数第一个
print(l1)           # ['太白', '女神', '吴老师', 'xiao', '闫龙', 'xiao']
# l1.remove('xia')    # 只能是元素,所以运行错误
# print(l1)           # 运行错误

# case3:    clear(了解)
l1 = ['太白', '女神', '吴老师', 'xiao', '闫龙']
l1.clear()     # 清空,注意所有元素删除,只剩下躯壳
print(l1)      # []


# case4:    del可以按照索引删除,也可以按照切片(步长)删除
# # 按照索引删除
l1 = ['太白', '女神', '吴老师', 'xiao', '闫龙']
del l1[-1]
print(l1)    # ['太白', '女神', '吴老师', 'xiao']
# # 按照切片(步长)删除
del l1[::2]
print(l1)    # ['女神', 'xiao']




# 改
#
# 按照索引改值
l1 = ['太白', '女神', '吴老师', 'xiao', '闫龙']
l1[0] = '男神'
print(l1)     # ['男神', '女神', '吴老师', 'xiao', '闫龙']

l2 = ['太白', '女神', '吴老师', 'xiao', '闫龙']
l2[-2] = '周杰伦'
print(l2)     # ['太白', '女神', '吴老师', '周杰伦', '闫龙']

# 按照切片改（了解）
l1 = ['太白', '女神', '吴老师', 'xiao', '闫龙']
l1[2:] = 'fsdag'    # 迭代的方式
print(l1)           # ['太白', '女神', 'f', 's', 'd', 'a', 'g']

# 按照切片（步长）（了解）
l1 = ['太白', '女神', '吴老师', 'xiao', '闫龙']
l1[::2] = 'abc'
print(l1)       # ['a', '女神', 'b', 'xiao', 'c']

l2 = ['太白', '女神', '吴老师', 'xiao', '闫龙']
l2[::2] = 'abcd'
print(l2)         # 放不进去了, 必须一一对应, 运行错误

# 查：
# 索引，切片（步长）
l3 = ['太白', '女神', '吴老师', 'xiao', '闫龙']
for i in l3:
    print(i)

