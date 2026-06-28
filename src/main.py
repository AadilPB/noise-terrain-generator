import numpy as np
import matplotlib.pyplot as plt
from value_noise import * 



input = np.linspace(0, 10, 100)
result_y = np.zeros(100)
x = np.linspace(0, 10, 100)
for k in range(100):
    result_y[k] = value_1D(input[k])

plt.figure(0)
plt.plot(x, result_y)
plt.fill_between(x, np.zeros(100), result_y, color = "brown")
plt.fill_between(x, result_y, np.ones(100), color = "blue")
plt.show()

grid_x, grid_y = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, 10, 100))

result = np.zeros((100, 100))

for i in range(100):
    for j in range(100):
        result[i, j] = value_2D(np.array([grid_x[i, j], grid_y[i, j]]))

plt.figure(1)
plt.imshow(result, cmap='gray')
plt.show()
