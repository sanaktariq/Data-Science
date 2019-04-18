import unittest
import test_shapefunction

class TestShape(unittest.TestCase):

    def test_circle(self):
        self.assertTrue("circle", "Circle(xy=(0.2, 0.5), radius=0.1)")
        
    def test_rectangle(self):
        self.assertTrue("rectangle", "Rectangle(xy=(0.175, 0.45), width=0.05, height=0.1, angle=0)")
        
    def test_ellipse(self):
        self.assertTrue("ellipse", "Ellipse(xy=(0.2, 0.5), width=0.2, height=0.1, angle=0)")

    def test_polygon(self):
        self.assertTrue("polygon", "RegularPolygon((0.2, 0.5), 5, radius=0.1, orientation=0)")

if __name__ == '__main__':
    unittest.main()
