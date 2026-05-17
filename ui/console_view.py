import os
import time
from ui.interface import BaseUI

class ConsoleUI(BaseUI):
    def __init__(self, grid, delay=0.2):
        self.grid = grid
        self.delay = delay
        self.running = True

    def update(self):
        # Clear terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        output = []
        for r in range(self.grid.rows):
            line = []
            for c in range(self.grid.cols):
                if self.grid.is_alive(r, c):
                    # Use 'X' for living cells, '.' for dead
                    line.append('X')
                else:
                    line.append('.')
            output.append(' '.join(line))
        
        print('\n'.join(output))
        print(f"\nGeneración activa. Presione Ctrl+C para salir.")

    def run(self):
        try:
            while self.running:
                self.update()
                self.grid.evolve()
                time.sleep(self.delay)
        except KeyboardInterrupt:
            print("\nSimulación finalizada.")
            self.running = False
