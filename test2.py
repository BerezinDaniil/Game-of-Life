import pygame
from pygame.locals import *
import random


class GameOfLife:

    def __init__(self, width, height, cell_size, speed: int = 7):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.cells = [[random.choice([0, 1]) for j in range(self.cell_height)] for i in range(self.cell_width)]
        self.speed = speed

    def draw_lines(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('white'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('white'),
                             (0, y), (self.width, y))

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('black'))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_lines()
            self.draw_grid()
            self.get_neighbours()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def draw_grid(self):
        for x in range(1, self.cell_width - 1):
            for y in range(1, self.cell_height - 1):
                if self.cells[x][y] == 0:
                    pygame.draw.rect(self.screen, pygame.Color('black'),
                                     [x * self.cell_size + 2, y * self.cell_size + 2, self.cell_size - 2,
                                      self.cell_size - 2])
                elif self.cells[x][y] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('green'),
                                     [x * self.cell_size + 2, y * self.cell_size + 2, self.cell_size - 2,
                                      self.cell_size - 2])

    def get_neighbours(self):
        cells = self.cells

        def check_cell(position, cells):
            count = 0
            for x in range(position[0] - 1, position[0] + 2, 1):
                for y in range(position[1] - 1, position[1] + 2, 1):
                    if cells[x][y] == 1:
                        count += 1
            return count

        next_field = [[0 for j in range(len(cells[0]))] for i in range(len(cells))]
        for i in range(1, self.cell_width - 1):
            for j in range(1, self.cell_height - 1):
                if cells[i][j] == 1:
                    if (check_cell([i, j], cells) == 3) or (check_cell([i, j], cells) == 4):
                        next_field[i][j] = 1
                    else:
                        next_field[i][j] = 0
                elif cells[i][j] == 0:
                    if (check_cell([i, j], cells) == 3):
                        next_field[i][j] = 1
                    else:
                        next_field[i][j] = 0
        self.cells = next_field


if __name__ == '__main__':
    game = GameOfLife(700, 700, 20)
    game.run()
