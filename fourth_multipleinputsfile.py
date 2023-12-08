import matplotlib.pyplot as plt
import numpy as np
files = 'file1.txt'
x = np.linspace(-10, 10, 400)
plt.figure(figsize=(6, 4))
with open(files, 'r') as file:
  for i, line in enumerate(file):
    a, b, c = map(float, line.split())
    y = a*x**2 + b*x + c
    plt.plot(x, y, label=f'Line {i+1}: {a}x^2 + {b}x + {c}')
plt.title('Plot of the quadratic functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()