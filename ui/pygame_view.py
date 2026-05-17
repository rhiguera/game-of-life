import pygame
import sys
from ui.interface import BaseUI

class PygameUI(BaseUI):
    def __init__(self, grid, cell_size=15):
        pygame.init()
        self.grid = grid
        self.cell_size = cell_size
        self.width = grid.cols * cell_size
        self.height = grid.rows * cell_size
        self.screen = pygame.display.set_mode((self.width, self.height + 50)) # Extra space for UI info
        pygame.display.set_caption("Conway's Game of Life - Aging Cells")
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = True
        self.font = pygame.font.SysFont("Arial", 18)

    def get_color_by_age(self, age):
        # Color gradient: Bright Green (1) -> Deep Blue (10+)
        # New: (0, 255, 100)
        # Old: (0, 50, 200)
        if age == 1:
            return (0, 255, 100)
        
        # Max age for color transition
        max_color_age = 10
        ratio = min((age - 1) / (max_color_age - 1), 1.0)
        
        # Linear interpolation
        r = 0
        g = int(255 * (1 - ratio) + 50 * ratio)
        b = int(100 * (1 - ratio) + 200 * ratio)
        
        return (r, g, b)

    def update(self):
        self.screen.fill((20, 20, 20)) # Dark background
        
        # Draw cells
        for r in range(self.grid.rows):
            for c in range(self.grid.cols):
                if self.grid.is_alive(r, c):
                    age = self.grid.get_age(r, c)
                    color = self.get_color_by_age(age)
                    pygame.draw.rect(
                        self.screen, 
                        color, 
                        (c * self.cell_size, r * self.cell_size, self.cell_size - 1, self.cell_size - 1)
                    )
        
        # Draw UI Info
        status = "PAUSED" if self.paused else "RUNNING"
        info_text = self.font.render(
            f"Status: {status} | Space: Pause/Play | R: Reset | Click: Toggle Cell", 
            True, 
            (200, 200, 200)
        )
        self.screen.blit(info_text, (10, self.height + 15))
        
        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                if event.key == pygame.K_r:
                    # Reset grid
                    self.grid.cells = [[0 for _ in range(self.grid.cols)] for _ in range(self.grid.rows)]
                    self.paused = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if y < self.height:
                    col = x // self.cell_size
                    row = y // self.cell_size
                    currently_alive = self.grid.is_alive(row, col)
                    self.grid.set_cell(row, col, not currently_alive)

    def run(self):
        while self.running:
            self.handle_input()
            
            if not self.paused:
                self.grid.evolve()
            
            self.update()
            self.clock.tick(10) # 10 FPS
