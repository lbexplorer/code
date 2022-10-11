import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-5, 5, 50)
y = 2433*x ** 4 + 10000 * x ** 3 + 80000  # 一元四次函数f(x)=x^4+6x^2-60x+36

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('2433*x ** 4 + 10000 * x ** 3 + 80000  ')
plt.grid(True)
plt.show()
