import unittest
import test_verticesandedges

class test_shape(unittest.TestCase):

    def test_rectangle(self):
        self.assertTrue("rectangle", "[[2, 2], [12, 2], [2, 7], [12, 7]]")
        
if __name__ == '__main__':
    unittest.main()
