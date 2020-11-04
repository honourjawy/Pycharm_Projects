li = [100, '太白', True, [1, 2, 3]]
# 索引
print(li[0], type(li[0]))      # 100 <class 'int'>
print(li[1],type(li[1]))       # 太白 <class 'str'>
print(li[-1],type(li[-1]))     # [1, 2, 3] <class 'list'>

# 切片 （顾头不顾腚）
print(li[:2])                  # [100, '太白']


# 练习题
l1 = [1, 3, 2, "a", 4, "b", 5, "c"]
# 通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
print(l1[:3])
# 通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
print(l1[3:6])
print(l1[3:-2])       # 或者 先定去屁股位置 ,Right可逆向取
# # 通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
print(l1[1:-2:2])
# 通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
print(l1[-3::-2])
print(l1[-3:-8:-2])    # 或者 先定去屁股位置 ,Right可逆向取

