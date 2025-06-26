import numpy as np
import matplotlib.pyplot as plt

B = (10, np.array((11, 11)))  # Безрисковая облигация: цена сегодня и в двух состояниях в будущем
S = (10, np.array((20, 5)))   # Акция: цена сегодня и в двух состояниях в будущем
M = np.array((B[1], S[1])).T  # Матрица будущих цен (2 состояния x 2 актива)

M0 = np.array((B[0], S[0]))

M
# array([[11, 20],
#        [11,  5]])

R = M / M0 - 1
# array([[ 0.1,  1. ],
#        [ 0.1, -0.5]])

P = np.array((0.5, 0.5))  # Оба состояния равновероятны

np.dot(P, R)
# array([0.1 , 0.25])

s = 0.55
phi = (1-s, s)  # Веса: облигация и акция

mu = np.dot(phi, np.dot(P, R))
# 0.1825

sigma = s * R[:, 1].std()
# 0.4125

values = np.linspace(0, 1, 25)
mu = [np.dot(((1-s), s), np.dot(P, R)) for s in values]
sigma = [s * R[:, 1].std() for s in values]

plt.figure(figsize=(10, 6))
plt.plot(values, mu, lw=3.0, label='$\\mu_p$')
plt.plot(values, sigma, '--', lw=3.0, label='$\\sigma_p$')
plt.legend(loc=0)
plt.xlabel('$s$')

plt.figure(figsize=(10, 6))
plt.plot(sigma, mu, lw=3.0, label='risk-return')
plt.legend(loc=0)
plt.xlabel('$\\sigma_p$')
plt.ylabel('$\\mu_p$')
plt.show()