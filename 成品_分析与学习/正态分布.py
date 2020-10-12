# #
# # 本文以某一批产品的长度为数据集
# # 在此数据集的基础上绘制直方图和正态分布曲线
# #
#
# import pandas as pd  # pandas是一个强大的分析结构化数据的工具集
# import numpy as np  # numpy是Python中科学计算的核心库
# import matplotlib.pyplot as plt  # matplotlib数据可视化神器
#
# # 正态分布的概率密度函数
# #   x      数据集中的某一具体测量值
# #   mu     数据集的平均值，反映测量值分布的集中趋势
# #   sigma  数据集的标准差，反映测量值分布的分散程度
# def normfun(x, mu, sigma):
#     pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
#     return pdf
#
# if __name__ == '__main__':
#
#     data = pd.read_csv('./le.csv') # 载入数据文件
#     print(data)
#     length = data['length'] # 获得长度数据集
#     mean = length.mean() # 获得数据集的平均值
#     std = length.std()   # 获得数据集的标准差
#
#     # 设定X轴：前两个数字是X轴的起止范围，第三个数字表示步长
#     # 步长设定得越小，画出来的正态分布曲线越平滑
#     x = np.arange(3613, 2553, 0.1)
#     # 设定Y轴，载入刚才定义的正态分布函数
#     y = normfun(x, mean, std)
#     # 绘制数据集的正态分布曲线
#     plt.plot(x, y)
#
#     # 绘制数据集的直方图
#     plt.hist(length, bins=12, rwidth=0.9, density=True)
#     plt.title('Length distribution')
#     plt.xlabel('Length')
#     plt.ylabel('Probability')
#
#     # 输出正态分布曲线和直方图
#     plt.show()