import numpy as np

#first model

S = np.array((20, 5))
K = 15
C = np.maximum(S-K, 0)
print(C)

#second model
