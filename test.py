
import matplotlib.pyplot as plt
import numpy as np

a = 1
b = -.01

x = []
for iii in range(1, 35):
    x.append(iii)

y = a + b * np.log(x)
print(y)
plt.plot(y)
plt.show()



