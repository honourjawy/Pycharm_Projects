import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def normfun(x, pingjun, biaozhuncha):
    f = 1 / (biaozhuncha * np.sqrt(2 * np.pi))*(np.exp(-((x - pingjun) ** 2) / (2 * (biaozhuncha ** 2))))
    return f
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