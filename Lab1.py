import numpy as np
import matplotlib.pyplot as plt


# Задание 1
def mhm(x):
    return np.log((np.e ** (1 / (np.sin(x) + 1)) / (1.25 + 1 / (x ** 15))) / np.log(1 + (x ** 2)))


print(mhm(1), mhm(10), mhm(100))

# Задание 2
x = np.arange(-5, 5, 0.01)
plt.plot(x, (x ** 2 - x - 6))
plt.show()

# Задание 3
x = np.arange(-5, 5, 0.01)
plt.plot(x, np.log((x ** 2 + 1) * (np.exp((-abs(x)) / 10))) / np.log(1 + np.tan(1 / (1 + (np.sin(x)) ** 2))))
plt.show()

# Задание 4
inp = input()
x = np.arange(-5, 5, 0.01)
with plt.xkcd():
    plt.plot(x, eval(inp))
plt.show()

#Задание 5
x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
x_com = np.arange(1, 5, 0.01)
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
plt.grid()
p1, v1 = np.polyfit(x, y, deg=1, cov=True)
p2, v2 = np.polyfit(x, y, deg=2, cov=True)
p1_f = np.poly1d(p1)
p2_f = np.poly1d(p2)
plt.plot(x, y, x_com, p1_f(x_com), x_com, p2_f(x_com))
plt.show()