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

#define the fig_gen function, which takes the argument shape
def fig_gen(shape):
  if shape == "Circle": #to generate a circle"
    circle = mpatches.Circle(grid[1], 0.1, ec="none")
    patches.append(circle)
    
  elif shape == "Rectangle": #to generate a rectangle
    rectangle = mpatches.Rectangle(grid[1] - [0.025, 0.05], 0.05, 0.1, ec="none")
    patches.append(rectangle) 
    
  elif shape == "Ellipse": #to generate an ellipse
    ellipse = mpatches.Ellipse(grid[1], 0.2, 0.1)
    patches.append(ellipse)
    
  elif shape == "Polygon": #to generate a polygon
    polygon = mpatches.RegularPolygon(grid[1], 5, 0.1)
    patches.append(polygon)
  
  collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3)
  ax.add_collection(collection)

  plt.axis('equal')

fig_gen("Polygon")



