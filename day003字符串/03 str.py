# 字符串从左至右是有顺序，即有下标，即索引
# 对字符串进行索引，切片出来的数据都是字符串类型。
# 按照索引取值:
# Sequence[left:right:step]：
# step缺省时为1
# left:right-->以坐标序排,否则缺省
#
# 1，若step为正，则表示从索引left开始取，直到索引right为止，但不包括索引right.
#      如果left >= right(先转化,转化后,比如,如下-2即为9,是一个位置),结果为空；
#      如果left缺省，默认为0；
#      如果right缺省，默认为len(Sequence)

# 2，若step为负，则表示从索引left开始取，直到索引right为止，但不包括索引right.
#      如果left <= right,结果为空；
#      如果left缺省，默认为len(Sequence)-1；
#      如果right缺省，默认为-1（好吧，我承认这个-1是我自己安排的）；


# s1 = 'python全栈22期'
# s2 = s1[0]
# s3 = s1[2]
# s4 = s1[-1]
# s5 = s1[10]
# s6 = s1[-6]
# print(s2,type(s2))         # p <class 'str'>
# print(s3)                  # t
# print(s4)                  # 期
# print(s5)                  # 期
# print(s6)                  # n


# # 按照切片取值,   注意:step缺省时为1
# # [要:到谁不要谁]
# s111 = 'python全栈22期'
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
# print(s00)                  # pytho
# print(s11)                  # python
# print(s22)                  # python
# print(s33)                  # 全栈2
# print(s99)                  # 全栈22期
# print(s77)                  #
# print(s55)                  #
# print(s66)                  #
# print(s88)                  # 2期





# # 切片步长(  先left与right划出范围(且要清楚索引不包括right)   然后以-1为基准跳步长    )
# # step缺省时默认为1
# s1 = 'python全栈22期'
# print(s1[:5:2])          # pto
# print(s1[2:7:5])         # t         (先选上left,step为5----->中间夹4个走,跳出区域这无)
# print(s1[2:7:4])         # t全       (先选上left,step为4----->中间夹3个走,跳出区域这无)
# print(s1[2:7:3])         # tn        (先选上left,step为3----->中间夹2个走,跳出区域这无)
# print(s1[2:7:2])         # to全       (先选上left,step为2----->中间夹1个走)
# print(s1[2:7:1])         # thon全
# # print(s1[2:7:0])       # 报错,step不可为0
# # step为-1时,但是left -----> right方向应为为逆向,否则成 空
# print('分隔符-----------引入倒序1--------------')
# print(s1[:5:-2])          # 期2全     (这时,看作0---->-6)
# print(s1[:-6:-2])         # 期2全     (为什么这样可改,下面不行呢?)
# print(s1[2:7:-5])         #
# print(s1[2:7:-4])         #
# print(s1[2:7:-3])         #
# print(s1[2:7:-2])         #
# print(s1[2:7:-1])         #
# print('分隔符-----------引入倒序2--------------')
# print(s1[-1:-5])          #
# print(s1[6:1])            #
# print(s1[-1:-5:-1])       # 期22栈
# print(s1[-1:-6:-1])       # 期22栈全
# print(s1[-1:-6:-2])       # 期2全





# 按索引：s1[index]
# 按照切片： s1[start_index: end_index+1]
# 按照切片步长： s1[start_index: end_index+1:2]
# 反向按照切片步长： s1[start_index: end_index后延一位:2]
# 思考题：倒序全部取出来？


s = 'taiBAifdsa'
# 字符串的常用操作方法
# 不会对原字符串进行任何操作，都是产生一个新的字符串
# upper lower
# s1 = s.upper()
# # s1 = s.lower()
# print(s1,type(s1))

# 应用：
# username = input('用户名')
# password = input('密码')
# code = 'QweA'
# print(code)
# your_code = input('请输入验证码：不区分大小写')
# if your_code.upper() == code.upper():
#     if username == '太白' and password == '123':
#         print('登录成功')
#     else:
#         print('用户名密码错误')
# else:
#     print('验证码错误')
#

# startswith endswith
# print(s.startswith('t'))  ***
# print(s.startswith('taiBAi'))  ***
# 了解
# print(s.startswith('B',3,6))


# replace
msg = 'alex 很nb,alex是老男孩教育的创始人之一，alex长得很帅'
# msg1 = msg.replace('alex','太白')          # 默认全部替换
# msg1 = msg.replace('alex','太白',2)
# print(msg)
# print(msg1)


# strip:空白：空格，\t \n
# s4 = '  \n太白\t'
# # print(s4)
# s5 = s4.strip()
# print(s5)
# 了解
# 可以去除指定的字符
# s4 = 'rre太r白qsd'
# s5 = s4.strip('qrsed')
# print(s5)

# split  非常重要
# 默认按照空格分隔，返回一个列表
# 指定分隔符
# str ---> list
# s6 = '太白 女神 吴超'
# s6 = '太白:女神:吴超'
# l = s6.split(':')
# print(l)
# 了解：
# s6 = ':barry:nvshen:wu'
# # print(s6.split(':'))
# print(s6.split(":",2))

# join 非常好用
# s1 = 'alex'
# s2 = '+'.join(s1)
# print(s2,type(s2))
# l1 = ['太白', '女神', '吴超']
# # 前提：列表里面的元素必须都是str类型
# s3 = ':'.join(l1)
# print(s3)

# count
# s8 = 'sdfsdagsfdagfdhgfhgfhfghfdagsaa'
# print(s8.count('a'))


# format: 格式化输出
# # 第一种用法：
# msg = '我叫{}今年{}性别{}'.format('大壮',25,'男')
# 第二种用法：
# msg = '我叫{0}今年{1}性别{2}我依然叫{0}'.format('大壮', 25,'男')
# print(msg)
# 第三种用法：
# a = 100
# msg = '我叫{name}今年{age}性别{sex}'.format(age=a,sex='男',name='大壮')
# print(msg)

# is 系列：
# name = 'taibai123'
# name = '100①'
# # print(name.isalnum()) #字符串由字母或数字组成
# # print(name.isalpha()) #字符串只由字母组成
# print(name.isdecimal()) #字符串只由十进制组成

# s1 = input('请输入您的金额：')
# if s1.isdecimal():
#     print(int(s1))
# else:
#     print('输入有误')


