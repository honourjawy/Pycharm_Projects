import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def normfun(x, pingjun, biaozhuncha):
    fx = 1 / (biaozhuncha * np.sqrt(2 * np.pi))*(np.exp(-((x - pingjun) ** 2) / (2 * (biaozhuncha ** 2))))
    return fx
if __name__ == '__main__':
    data = pd.read_csv('jawy.csv')
    length = data['length']
    mean = length.mean()
    std = length.std()
    x = np.arange(3622, 3656, 0.1)
    y = normfun(x, mean, std)
    plt.plot(x, y)
    plt.hist(length, bins=16, rwidth=0.75,facecolor='blue', density=True)
    plt.title('Normal distribution')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
else:
    print('运行错误')



#
# import math
# import numpy as np
# import matplotlib.pyplot as plt
# b = 5                 # 求取均值μ
# a = math.sqrt(0.6)    # 标准差δ
# x_zhou = np.linspace(b - 3*a, b + 3*a, 50)   # 在指定的间隔内返回均匀间隔的数字。
# y_zhou = np.exp(-(x_zhou - b) ** 2 /(2* a **2))/(math.sqrt(2*math.pi)*a)   #正态密度
# plt.plot(x_zhou, y_zhou, "r-", linewidth=4)   #图形设置
# plt.grid(True)
# plt.show()    # 作图形




# import numpy as np
# import matplotlib.pyplot as plt
# import math
# u = 4
# sig = math.sqrt(0.6)
# x = np.linspace(u - 3 * sig, u + 3 * sig, 1000)
# y_sig = np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig)
# plt.plot(x, y_sig, "r-", linewidth=2)
# plt.grid(True)
# plt.title('Normal distribution')
# plt.show()



