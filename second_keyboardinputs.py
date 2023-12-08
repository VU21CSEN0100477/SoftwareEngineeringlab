import matplotlib.pyplot as plt
import numpy as np
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
x=np.linspace(-10, 10, 400)
y = a*x**2+b*x+c
plt.figure(figsize=(6, 4))
plt.plot(x, y, label=f'User input function')
plt.title('Plot of the quadratic function')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.show()
