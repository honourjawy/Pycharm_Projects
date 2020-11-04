r = range(10)    # 就像[0,1,2,3,4,5,6,7,8,9]列表的容器
                 # 顾头不顾腚
                 # 0 可以默认不写
print(r)       # range(0, 10)
for i in r:
    print(i)   # 0 1 2 3 4 5 6 7 8 9  # 顾头不顾腚

# 索引（了解）
print(r[1])     # 1

for i in range(1, 101):    # 打印1---100数
    print(i)        # 0 1 2 3....100    # 顾头不顾腚

for i in range(2,101,2):   # 引入步长,打印偶数
    print(i)        # 2 4....100    # 顾头不顾腚

for i in range(100,0,-1):   # 引入步长,打印偶数 (倒取)
    print(i)        # 100 99...1

# # 例如:
# 利用for循环，利用range将l1列表的所有索引依次打印出来
l1 = [1, 2, 3, 'alex', '太白']
for i in range(len(l1)):
    print(i)

# 结果:

# 0
# 1
# 2
# 3
# 4



l1 = [1, 2, 3, 'alex', '太白']
for i in range(3):   # 和上面的l1无关,已经数出来了
    pass             # range(3)是0~2, 顾头不顾腚
print(i)      # 2