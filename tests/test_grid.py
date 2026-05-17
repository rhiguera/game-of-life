import unittest
from core.grid import Grid

class TestGrid(unittest.TestCase):
    def test_initialization(self):
        grid = Grid(10, 10)
        self.assertEqual(grid.rows, 10)
        self.assertEqual(grid.cols, 10)
        self.assertFalse(grid.is_alive(0, 0))

    def test_set_cell(self):
        grid = Grid(5, 5)
        grid.set_cell(2, 2, True)
        self.assertTrue(grid.is_alive(2, 2))
        self.assertEqual(grid.get_age(2, 2), 1)

    def test_count_neighbors(self):
        grid = Grid(5, 5)
        grid.set_cell(1, 1)
        grid.set_cell(1, 2)
        grid.set_cell(1, 3)
        self.assertEqual(grid.count_neighbors(2, 2), 3)
        self.assertEqual(grid.count_neighbors(1, 2), 2)

    def test_block_pattern(self):
        # Static pattern: Block
        grid = Grid(4, 4)
        grid.set_cell(1, 1)
        grid.set_cell(1, 2)
        grid.set_cell(2, 1)
        grid.set_cell(2, 2)
        
        grid.evolve()
        self.assertTrue(grid.is_alive(1, 1))
        self.assertTrue(grid.is_alive(1, 2))
        self.assertTrue(grid.is_alive(2, 1))
        self.assertTrue(grid.is_alive(2, 2))
        self.assertEqual(grid.get_age(1, 1), 2)

    def test_blinker_pattern(self):
        # Oscillator pattern: Blinker
        grid = Grid(5, 5)
        grid.set_cell(2, 1)
        grid.set_cell(2, 2)
        grid.set_cell(2, 3)
        
        grid.evolve()
        self.assertTrue(grid.is_alive(1, 2))
        self.assertTrue(grid.is_alive(2, 2))
        self.assertTrue(grid.is_alive(3, 2))
        self.assertFalse(grid.is_alive(2, 1))
        self.assertFalse(grid.is_alive(2, 3))

if __name__ == '__main__':
    unittest.main()
