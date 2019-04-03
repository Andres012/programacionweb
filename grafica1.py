import numpy as np
import matplotlib.pyplot as plt

plt.ion() 

y = [] 

while True:
    y.append(np.random.randn(1)) 
    if len(y) <= 10:
        plt.plot(y)
    else:
        plt.plot(y[-10:])

    plt.pause(0.05) 
    plt.cla() 
