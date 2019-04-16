import unittest
import test_shapefunction
import numpy as np
import matplotlib.pyplot as plt

class TestShape(unittest.TestCase):

    def test_circle(self):
        self.assertTrue(circle, mpatches.Circle(grid[1], 0.1, ec="none", "Circle")
    
    def test_rectangle(self):
        self.assertTrue(rectangle, mpatches.Rectangle(grid[1] - [0.025, 0.05], 0.05, 0.1, ec="none", "Rectangle")
        #self.assertFalse()

    def test_ellipse(self):
        self.assertTrue(rectangle,mpatches.Ellipse(grid[1], 0.2, 0.1, "Ellipse")
        #self.assertFalse()

    def test_rectangle(self):
        self.assertTrue(polygon, mpatches.RegularPolygon(grid[1], 5, 0.1), "Polygon")
        #self.assertFalse()

if __name__ == '__main__':
    unittest.main()
