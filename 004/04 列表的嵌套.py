l1 = [1, 2, 'taibai', [1, 'alex', 3,]]
# 1, 将l1中的'taibai'变成大写并放回原处。

print(l1[2].upper(),type(l1[2].upper()))    # TAIBAI <class 'str'>

l1[2] = l1[2].upper()     #  l1[2].upper()  即为  'TAIBAI'
print(l1)                 # [1, 2, 'TAIBAI', [1, 'alex', 3]]


# 2，给小列表[1,'alex',3,]追加一个元素--->'老男孩教育'
print(l1[-1])               # 先找到小列表   # [1, 'alex', 3]
l1[-1].append('老男孩教育')   # 这时的 l1, '老男孩教育'加进去了没有?
print(l1)                   # [1, 2, 'taibai', [1, 'alex', 3, '老男孩教育']]


# 3，将列表中的'alex'通过字符串拼接的方式在列表中变成'alexsb'
print(l1[-1][1])       # 先找到小列表   # alex

new_str = l1[-1][1] + 'sb'
l1[-1][1] = new_str
print(l1)              # [1, 2, 'taibai', [1, 'alexsb', 3, '老男孩教育']]

l1[-1][1] = l1[-1][1] + 'sb'    # 简化形式
print(l1)                       # [1, 2, 'taibai', [1, 'alexsb', 3]]

# 另外一种简便方法,回顾count = count + 1   ----->   # count += 1
l1[-1][1] += 'sb'
print(l1)               # [1, 2, 'taibai', [1, 'alexsb', 3]]




# 练习:
lis = [2, 30, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 将列表lis中的"tt"变成大写（用两种方式）
lis[3][2][1][0] = 'TT'
print(lis)          # [2, 30, 'k', ['qwe', 20, ['k1', ['TT', 3, '1']], 89], 'ab', 'adv']

lis[3][2][1][0] = lis[3][2][1][0].upper()
print(lis)            # [2, 30, 'k', ['qwe', 20, ['k1', ['TT', 3, '1']], 89], 'ab', 'adv']

