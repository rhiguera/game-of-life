import copy

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.generation = 0
        # Grid stores age: 0 if dead, >0 if alive (represents consecutive generations)
        self.cells = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_cell(self, row, col, alive=True):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.cells[row][col] = 1 if alive else 0

    def is_alive(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.cells[row][col] > 0
        return False

    def get_age(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.cells[row][col]
        return 0

    def count_neighbors(self, row, col):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    if self.cells[r][c] > 0:
                        count += 1
        return count

    def evolve(self):
        new_cells = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                neighbors = self.count_neighbors(r, c)
                currently_alive = self.cells[r][c] > 0

                if currently_alive:
                    # Survival rules: 2 or 3 neighbors
                    if neighbors in [2, 3]:
                        new_cells[r][c] = self.cells[r][c] + 1
                    else:
                        new_cells[r][c] = 0
                else:
                    # Birth rule: exactly 3 neighbors
                    if neighbors == 3:
                        new_cells[r][c] = 1
        
        self.cells = new_cells
        self.generation += 1
