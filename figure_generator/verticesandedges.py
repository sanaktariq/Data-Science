import matplotlib.pyplot as plt

#starting parameters:
"""origin = (0,0)
height = 5
width = 10
radius = 5"""

def fig_gen(shape, origin, width, height):
    if shape == "rectangle":
        give = [
                [origin[0], origin[1]], 
                [origin[0] + width, origin[1]], 
                [origin[0], origin[1] + height], 
                [origin[0] + width, origin[1]+ height]
                ]
    else:
        print("Invalid Entry")
    
    return give

x = fig_gen("rectangle", [2,2], 10, 5) 
print(x)
#print(x, x[2])

import numpy as np
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

# create 3x3 grid to plot the artists
grid = np.mgrid[0.2:0.8:3j, 0.2:0.8:3j].reshape(2, -1).T
fig, ax = plt.subplots()
patches = []

rectangle = mpatches.Rectangle([2,2], 10, 5, angle=0.0)
patches.append(rectangle)

collection = PatchCollection(patches, alpha=0.3)
ax.add_collection(collection)

plt.axis('equal')

plt.show()

