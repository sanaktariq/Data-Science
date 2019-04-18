#Write a function that takes a shape and then plots it.

#import relevant libraries
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

# create 3x3 grid to plot the artists
grid = np.mgrid[0.2:0.8:3j, 0.2:0.8:3j].reshape(2, -1).T
fig, ax = plt.subplots()
patches = []

#print(grid)

#define the fig_gen function, which takes the argument shape
def fig_gen(shape):
  if shape == "circle": #to generate a circle"
    ret = mpatches.Circle(grid[1], 0.1, ec="none")
    #print(ret)

  elif shape == "rectangle": #to generate a rectangle
    ret = mpatches.Rectangle(grid[1] - [0.025, 0.05], 0.05, 0.1, ec="none")
    #print(ret)
    
  elif shape == "ellipse": #to generate an ellipse
    ret = mpatches.Ellipse(grid[1], 0.2, 0.1)
    #print(ret)
    
  elif shape == "polygon": #to generate a polygon
    ret = mpatches.RegularPolygon(grid[1], 5, 0.1)
    #print(ret)

  return ret

x = fig_gen("polygon")
print(str(x))

cond = str(x) == "Circle(xy=(0.2, 0.5), radius=0.1)"
print(cond)

def plot(arg):
  patches.append(arg)
  collection = PatchCollection(patches, alpha=0.3)
  ax.add_collection(collection)

plt.axis('equal')

shapelist = ["circle", "rectangle", "ellipse", "polygon"]
for n in shapelist:
  i = fig_gen(n)
  #print(i)
  plot(i)

