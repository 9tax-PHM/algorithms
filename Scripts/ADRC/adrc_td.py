import math
import matplotlib.pyplot as plt
import numpy as np
from time import sleep

#fhan
def fhan(x1, x2, r, h):
    d = r*h
    d0 = h*d
    td_y = x1 + h*x2
    a0 = math.sqrt(d * d + 8 * r * math.fabs(td_y))

    if math.fabs(td_y) > d0:
        a = x2 + 0.5 * (a0 - d) * np.sign(td_y)
    else:
        a = x2 + td_y / h

    if math.fabs(a) > d:
        fhan = -r * np.sign(a)
    else:
        fhan = -r * a / d
    return fhan

#跟踪微分器
def td(x1, x2, v, h , r=9000):
    fh = fhan(x1 - v, x2, r, h)
    x1 = x1 + h * x2
    x2 = x2 + h * fh
    return x1, x2


#测试代码
if __name__ == '__main__':
    v = 1
    h = 0.01
    x1 = 0
    x2 = 0

    X = []
    X1 = []
    X2 = []
    for i in range(1000):
        v = math.sin(i * h)
        x1, x2 = td(x1,x2,v,h)
        print(x2)
        X.append(i*h)
        X1.append(x1)
        X2.append(x2)


    plt.figure()
    plt.grid()
    plt.plot(X,X1)
    plt.plot(X, X2)
    plt.show()

