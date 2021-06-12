import LAB7_VAR6 as module
import numpy as np
import matplotlib.pyplot as plt
x_sets, y_set = module.plot_CTFs([0, 0.2], 
                                 [0, 1], 
                                 [0, 5], 
                                 [-2, 0.5])
array1 = [1, 2]
array2 = [1, 3]
N = 1000
data = np.random.normal(loc=10, scale=10, size=N)
x = np.sort(data)
y = np.arange(N)/float(N)
# for i in range(len(x_sets)):
#   plt.plot(x_sets[i], y_set)

# plt.show()
