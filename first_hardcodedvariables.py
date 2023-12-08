import matplotlib.pyplot as plt
import numpy as np
a = 1
b = -3
c = 2
x = np.linspace(-10, 10, 400)
y = a*x**2 + b*x + c
plt.figure(figsize=(6, 4))
plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
plt.title('Plot of the quadratic function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()