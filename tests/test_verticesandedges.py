import unittest
import sys 
import os
sys.path.append(os.path.abspath("."))
import figure_generator.verticesandedges as verticesandedges

class test_fig_gen(unittest.TestCase):

    def test_fig_gen(self):
        self.assertEqual(verticesandedges.fig_gen(("rectangle"), (2,2), (10), (5)), [[2, 2], [12, 2], [2, 7], [12, 7]])
        self.assertEqual(verticesandedges.fig_gen(("rectangle"), (0,0), (100), (50)), [[0, 0], [100, 0], [0, 50], [100, 50]])
        self.assertEqual(verticesandedges.fig_gen(("rectangle"), (-5,-5), (4), (2)), [[-5, -5], [-1, -5], [-5, -3], [-1, -3]])
        self.assertEqual(verticesandedges.fig_gen(("rectangle"), (50, 50), (1000), (500)), [[50, 50], [1050, 50], [50, 550], [1050, 550]])
        self.assertEqual(verticesandedges.fig_gen(("rectangle"), (50, 50), (1000), (500)), [[50, 50], [1050, 50], [50, 550], [1050, 550]])

if __name__ == '__main__':
    unittest.main()
