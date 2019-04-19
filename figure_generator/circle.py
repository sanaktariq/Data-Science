import numpy as np
import matplotlib.pyplot as plt

def circle_segment(res, i, radius):
    return np.array([np.cos(((2 * np.pi) / res) * i) * radius,
                     np.sin(((2 * np.pi) / res) * i) * radius])

seg_result = circle_segment(100, 50, 5)
print(seg_result)

def circle(radius, res=100):
    return np.array([circle_segment(res, i, radius) for i in range(0, res + 1)])

cir_result = circle(50, res=100)
print(cir_result)

