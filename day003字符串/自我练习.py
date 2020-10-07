# s111 = 'python全栈22期'
#
# s00 = s111[0:5]             # 顾头不顾屁股所以只能pytho
# s11 = s111[0:6]             # 顾头不顾屁股,必须5+1 ----> python
# s22 = s111[:6]              #  [0:6]   ---->   [:6]    若从开头取,则可省略0
# s33 = s111[6:-2]
# s99 = s111[6:]
# s77 = s111[6:0]
# s55 = s111[-2:5]
# s66 = s111[-2:0]
# s88 = s111[-2:]
#
# print(s00)          # pytho
# print(s11)          # py0thon
# print(s22)          # python
# print(s33)          # 全栈2
# print(s99)          # 全栈22期
# print(s77)          #
# print(s55)          #
# print(s66)          #
# print(s88)          #2期

# s1 = 'python全栈22期'
# s6 = s1[-1:-6:-3]      # 倒序
# print(s6)
# s7 =s1[-2:-7:-2]
# print(s7)
# s8 = s1[-3:-9:-1]      # 倒序
# print(s8)
# s9 = s1[-3:-9:-2]      # 倒序
# print(s9)
# s99 = s1[-3:-9:-3]     # 倒序
# print(s99)
# s1 = '社会符合本附件'
# print( s1 [-5 : : -1] )     # 符会社
# print( s1 [-5 : -1 : -1] )  #

#
# s3 = '社会符合本附件'
# print( s3 [ : : 1] )     #  社会符合本附件
# print( s3 [ :  : -1] )   #  件附本合符会社



#
# a = 'taiBAifdsa'
# print(a.endswith('a'))            # True
# print(a.endswith('asd'))          # False     # 注意方向
# print(a.endswith('fdsa'))         # True
# print(a.endswith('i',3,6))        # True      # 顾头不顾腚



# s6 = '太白 女神 吴超'
# s8 = '太白:女神:吴超'
# l = s6.split( )      # 默认按照空格分隔，返回一个'列表'
# m = s6.split()       # 默认按照空格分隔，返回一个'列表'
# print(l)              # ['太白', '女神', '吴超']
# print(m)              # ['太白', '女神', '吴超']
#
# a = s8.split( )        # 默认按照空格分隔，返回一个'列表'    # 也可以写成: a = s8.split( )
# b = s8.split()
#
# print(a)                # ['太白:女神:吴超']
# print(b)                # ['太白:女神:吴超']

#
# s99 = '太白:神:吴超'
# # l = s6.split(:)       # 错误语法
# m = s99.split()          # 默认按照空格分隔，返回一个'列表'
# e = s99.split(':')       # 默认按照空格分隔，返回一个'列表'
# print(m)                # ['太白:神:吴超']          # 注意区别
# print(e)                # ['太白', '神', '吴超']


#
# s999 = '太白 神 吴超'
# m = s999.split(' ')
# e = s999.split('  ')
# q = s999.split('   ')
# print(m)                   # ['太白', '神', '吴超']
# print(e)                   # ['太白 神 吴超']         # 注意m和e,空什么引号里放什么
# print(q)                   # ['太白 神 吴超']


#
# s8 = '太白:神:吴超'
# a = s8.split()        # 也可以写成: a = s8.split( )
# b = s8.split(' ')      # 默认按空格分，返回一个'列表'   # b = s8.split('')会报错
# c = s8.split(':')      # 默认按照空格分隔，返回一个'列表'
# d = s8.split(        )        # 默认按照空格分隔，返回一个'列表'
# print(a)       # ['太白:神:吴超']
# print(b)       # ['太白:神:吴超']
# print(c)       # ['太白', '神', '吴超']
# print(d)       # ['太白:神:吴超']           # 注意区别于列表



#
#
# l1 = ['太白', '女神', '吴超']
# s5 = ':'.join(l1)        # 太白:女神:吴超
# print(l1,type(l1))       # ['太白', '女神', '吴超'] <class 'list'>
# print(s5,type(s5))       # 太白:女神:吴超 <class 'str'>


#
# a = 100          # 可以input.....变量......
# msg = '我叫{name}今年{age}性别{sex}'.format(age=a,sex='男',name='大壮')
# # 可以不按照顺序
# print(msg)


#
# # is 系列：   al   num    pha    decimal
# name = 'taibai123'
# print(name.isnumal())         # 是否字符串由字母或数字组成?      # True
# # print(name.isnum())         # 是否字符串由字母或数字组成?      # True
# # print(name.ispha())         # 是否字符串由只由字母组成?        # False
# # print(name.isdecimal())       # 是否字符串由十进制组成?          # False


s1 = '老男孩教育最好的讲师：太白'
for i in s1:
    print(i)
