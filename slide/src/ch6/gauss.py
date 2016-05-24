import math
import matplotlib.pyplot as plt

sigma = 2
sigma2 = 4
X = []
Y = []
Y2 = [] 
x = -5
while x < 5:
    x = x+0.01
    y = 1/math.sqrt(sigma*2*math.pi)*math.exp(-x*x/(2*sigma^2))
    y2 = 1/math.sqrt(sigma2*2*math.pi)*math.exp(-x*x/(2*sigma2^2))
    X.append(x)
    Y.append(y)
    Y2.append(y2)

plt.plot(X, Y)
plt.plot(X,Y2)
plt.show()
