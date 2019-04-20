import numpy as np
import matplotlib.pyplot as plt

def circle(radius):
    theta = np.linspace(0., 2*np.pi)
    x = radius*np.cos(theta)
    y = radius*np.sin(theta)
    return x,y


[a,b] = circle(50)
print([a,b])
plt.plot (a,b)
plt.show()
