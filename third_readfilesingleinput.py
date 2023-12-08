import matplotlib.pyplot as plt
import numpy as np
with open('input.txt', 'r') as file:
    a, b, c = map(float, file.readline().split())
x=np.linspace(-10, 10, 400)
y=a*x**2 + b*x + c
plt.figure(figsize=(6, 4))
plt.plot(x, y, label=f'File single input')
plt.title('Plot of the quadratic function')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.show()
