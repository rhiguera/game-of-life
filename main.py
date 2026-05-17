import argparse
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
    parser.add_argument("--rows", type=int, default=40, help="Number of rows")
    parser.add_argument("--cols", type=int, default=60, help="Number of columns")
    parser.add_argument("--cell-size", type=int, default=15, help="Cell size in pixels (for GUI)")
    
    args = parser.parse_args()

    grid = Grid(args.rows, args.cols)
    
    # Initialize with a basic glider pattern
    if args.rows > 5 and args.cols > 5:
        grid.set_cell(1, 2)
        grid.set_cell(2, 3)
        grid.set_cell(3, 1)
        grid.set_cell(3, 2)
        grid.set_cell(3, 3)

    if args.mode == "gui":
        ui = PygameUI(grid, cell_size=args.cell_size)
    else:
        ui = ConsoleUI(grid)

    ui.run()

if __name__ == "__main__":
    main()
