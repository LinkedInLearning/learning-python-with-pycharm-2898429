from unittest import TestCase
from grid import Grid


class TestGrid(TestCase):
    def test_update_grid(self):
        # set up a simple 3 by 3 grid
        test_grid = Grid(screen_dimensions=(10, 10), width=3, height=3)
        # creates an empty grid that is 3 by 3
        # |_|_|_|
        # |_|_|_|
        # |_|_|_|

        # |X|_|_|
        # |X|_|_|
        # |X|_|_|
        test_grid.flip(0, 0)
        test_grid.flip(0, 1)
        test_grid.flip(0, 2)

        # what do we want to see after updating the grid?
        # |_|_|_|
        # |X|X|_|
        # |_|_|_|

        test_grid.update()

        self.assertFalse(test_grid.get_cell(0, 0).active)
        self.assertTrue(test_grid.get_cell(0, 1).active)
        self.assertFalse(test_grid.get_cell(0, 2).active)
        self.assertFalse(test_grid.get_cell(1, 0).active)
        self.assertTrue(test_grid.get_cell(1, 1).active)
        self.assertFalse(test_grid.get_cell(1, 2).active)
        self.assertFalse(test_grid.get_cell(2, 0).active)
        self.assertFalse(test_grid.get_cell(2, 1).active)
        self.assertFalse(test_grid.get_cell(2, 2).active)
