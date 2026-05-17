import pygame
import sys
from ui.interface import BaseUI

class PygameUI(BaseUI):
    def __init__(self, grid, cell_size=10):
        pygame.init()
        self.grid = grid
        self.cell_size = cell_size
        self.width = grid.cols * cell_size
        self.height = grid.rows * cell_size
        # Darker theme colors
        self.COLOR_BG = (10, 10, 15)
        self.COLOR_GRID = (25, 25, 35)
        self.COLOR_UI_BG = (30, 30, 45)
        self.COLOR_TEXT = (220, 220, 230)
        
        self.screen = pygame.display.set_mode((self.width, self.height + 60))
        pygame.display.set_caption("Conway's Game of Life - Aging Cells")
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = True
        self.font = pygame.font.SysFont("Segoe UI", 18, bold=True)
        self.small_font = pygame.font.SysFont("Segoe UI", 14)

    def get_color_by_age(self, age):
        # Improved gradient: Bright Neon Green -> Cyan -> Deep Electric Blue
        if age == 1:
            return (100, 255, 100) # Newborn: Bright Neon Green
        
        max_color_age = 20 # Slower transition
        ratio = min((age - 1) / (max_color_age - 1), 1.0)
        
        if ratio < 0.5:
            # Green to Cyan
            r = 0
            g = int(255 * (1 - ratio*2) + 100 * (ratio*2))
            b = int(100 * (1 - ratio*2) + 255 * (ratio*2))
        else:
            # Cyan to Deep Blue
            r = 0
            g = int(100 * (1 - (ratio-0.5)*2) + 20 * ((ratio-0.5)*2))
            b = int(255 * (1 - (ratio-0.5)*2) + 180 * ((ratio-0.5)*2))
        
        return (r, g, b)

    def draw_grid_lines(self):
        if self.cell_size < 5: return # Don't draw lines if cells are too small
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, self.COLOR_GRID, (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, self.COLOR_GRID, (0, y), (self.width, y))

    def update(self):
        self.screen.fill(self.COLOR_BG)
        
        self.draw_grid_lines()
        
        # Draw cells
        for r in range(self.grid.rows):
            for c in range(self.grid.cols):
                age = self.grid.get_age(r, c)
                if age > 0:
                    color = self.get_color_by_age(age)
                    pygame.draw.rect(
                        self.screen, 
                        color, 
                        (c * self.cell_size + 1, r * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
                    )
        
        # Draw UI Panel
        pygame.draw.rect(self.screen, self.COLOR_UI_BG, (0, self.height, self.width, 60))
        pygame.draw.line(self.screen, (100, 100, 120), (0, self.height), (self.width, self.height), 2)

        # Status and Generation
        status_text = "PAUSED" if self.paused else "RUNNING"
        status_color = (255, 100, 100) if self.paused else (100, 255, 100)
        
        gen_surface = self.font.render(f"Generation: {self.grid.generation}", True, self.COLOR_TEXT)
        status_surface = self.font.render(f"Status: {status_text}", True, status_color)
        
        self.screen.blit(gen_surface, (20, self.height + 10))
        self.screen.blit(status_surface, (20, self.height + 30))
        
        # Controls Hint
        controls_text = "SPACE: Play/Pause | R: Reset | CLICK: Toggle | DRAG: Draw"
        controls_surface = self.small_font.render(controls_text, True, (150, 150, 170))
        self.screen.blit(controls_surface, (self.width - controls_surface.get_width() - 20, self.height + 22))
        
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
                    self.grid.cells = [[0 for _ in range(self.grid.cols)] for _ in range(self.grid.rows)]
                    self.grid.generation = 0
                    self.paused = True

        # Handle mouse drawing (Continuous)
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]: # Left click
            x, y = pygame.mouse.get_pos()
            if y < self.height:
                col = x // self.cell_size
                row = y // self.cell_size
                if 0 <= row < self.grid.rows and 0 <= col < self.grid.cols:
                    self.grid.set_cell(row, col, True)
        elif mouse_pressed[2]: # Right click to erase
            x, y = pygame.mouse.get_pos()
            if y < self.height:
                col = x // self.cell_size
                row = y // self.cell_size
                if 0 <= row < self.grid.rows and 0 <= col < self.grid.cols:
                    self.grid.set_cell(row, col, False)

    def run(self):
        while self.running:
            self.handle_input()
            
            if not self.paused:
                self.grid.evolve()
            
            self.update()
            self.clock.tick(30) # Increased speed for larger population
