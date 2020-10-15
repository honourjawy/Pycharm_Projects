# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# def normfun(x, pingjun, biaozhuncha):
#     fx = 1 / (biaozhuncha * np.sqrt(2 * np.pi))*(np.exp(-((x - pingjun) ** 2) / (2 * (biaozhuncha ** 2))))
#     return fx
# if __name__ == '__main__':
#     data = pd.read_csv('jawy.csv')
#     length = data['length']
#     mean = length.mean()
#     std = length.std()
#     y = normfun(x, mean, std)
#     plt.plot(x, y)
#     plt.hist(length, bins=16, rwidth=0.75,facecolor='blue', density=True)
#     plt.title('Normal distribution')
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.show()
# else:
#     print('运行错误')
#     x = np.arange(3622, 3656, 0.1)



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


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


# 正态分布的概率密度函数。可以理解成 x 是 mu（均值）和 sigma（标准差）的函数
def normfun(x, mu, sigma):
    pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return pdf


# u = 66
# B = 0.9
# x = np.linspace(u - 3 * sigma, u + 3 * sigma, 50)
# y_sig = np.exp(-(x - u) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
# plt.plot(x, y_sig, "r-", linewidth=2)
# plt.vlines(u, 0, np.exp(-(u - u) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma), colors="c",
#            linestyles="dashed")
# plt.vlines(u + sigma, 0, np.exp(-(u + sigma - u) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma),
#            colors="k", linestyles="dotted")
# plt.vlines(u - sigma, 0, np.exp(-(u - sigma - u) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma),
#            colors="m", linestyles="dotted")
# plt.xticks([u - sigma, u, u + sigma], ['μ-σ', 'μ', 'μ+σ'])
# plt.xlabel('X_axis')
# plt.ylabel('Y_axis')
# plt.title('zhengtaifenbutu: $\mu = %.2f, $sigma=%.2f' % (u, sigma))
# plt.grid(True)
# plt.show()




u = 66     # 平均数
B = 0.9    # 标准差
x = np.linspace(u - 3 * B, u + 3 * B, 50)
y_sig = np.exp(-(x - u) ** 2 / (2 * B ** 2)) / (math.sqrt(2 * math.pi) * B)
plt.plot(x, y_sig, "r-", linewidth=2)
plt.vlines(u, 0, np.exp(-(u - u) ** 2 / (2 * B ** 2)) / (math.sqrt(2 * math.pi) * B), colors="c",
           linestyles="dashed")
plt.vlines(u + B, 0, np.exp(-(u + B - u) ** 2 / (2 * B ** 2)) / (math.sqrt(2 * math.pi) * B),
           colors="k", linestyles="dotted")
plt.vlines(u - B, 0, np.exp(-(u - B - u) ** 2 / (2 * B ** 2)) / (math.sqrt(2 * math.pi) * B),
           colors="m", linestyles="dotted")
plt.xticks([u - B, u, u + B], ['μ-σ', 'μ', 'μ+σ'])
plt.xlabel('X_axis')
plt.ylabel('Y_axis')
plt.title('zhengtaifenbutu: $\mu = %.2f, $B=%.2f' % (u, B))
plt.grid(True)
plt.show()

