import argparse
import random
from core.grid import Grid
from ui.console_view import ConsoleUI
from ui.pygame_view import PygameUI

def main():
    parser = argparse.ArgumentParser(description="Conway's Game of Life with Aging Cells")
    parser.add_argument(
        "--mode", 
        choices=["gui", "console"], 
        default="gui",
        help="Display mode: gui (default) or console"
    )
    parser.add_argument("--rows", type=int, default=80, help="Number of rows")
    parser.add_argument("--cols", type=int, default=120, help="Number of columns")
    parser.add_argument("--cell-size", type=int, default=10, help="Cell size in pixels (for GUI)")
    
    args = parser.parse_args()

    grid = Grid(args.rows, args.cols)
    
    # Random initial population for a more "vibrant" start
    for r in range(args.rows):
        for c in range(args.cols):
            if random.random() < 0.15: # 15% chance of being alive
                grid.set_cell(r, c, True)

    # Also include the glider
    if args.rows > 10 and args.cols > 10:
        grid.set_cell(5, 5)
        grid.set_cell(6, 6)
        grid.set_cell(7, 4)
        grid.set_cell(7, 5)
        grid.set_cell(7, 6)

    if args.mode == "gui":
        ui = PygameUI(grid, cell_size=args.cell_size)
    else:
        ui = ConsoleUI(grid)

    ui.run()

if __name__ == "__main__":
    main()
