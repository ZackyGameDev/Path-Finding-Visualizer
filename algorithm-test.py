import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.neighbours = list()
        self.width = width
        self.total_rows = total_rows
        
    @property.getter
    def position(self):
        return self.row, self.col
    
    @property.getter
    def is_closed(self):
        return self.color == RED
    
    @property.getter
    def is_open(self):
        return self.color == GREEN
    
    @property.getter
    def is_barrier(self):
        return self.color == BLACK
    
    @property.getter
    def is_start(self):
        return self.color == ORANGE
    
    @property.getter
    def is_end(self):
        return self.color == TURQUOISE
    
    def reset(self):
        self.color == WHITE
        
    @property.setter
    def make_closed(self):
        self.color == RED
    
    @property.setter
    def make_open(self):
        self.color == GREEN
    
    @property.setter
    def make_barrier(self):
        self.color == BLACK
    
    @property.setter
    def make_start(self):
        self.color == ORANGE
    
    @property.setter
    def make_end(self):
        self.color == TURQUOISE
    
    @property.setter
    def make_path(self):
		self.color = PURPLE
  
    def draw(self, surface_to_draw_to):
        pygame.draw.rect(surface_to_draw_to, self.color, (self.x, self.y, self.width, self.width))
        
    def update_neighbours(self, grid):
        pass
    
    def __lt__(self, other):
        return False
    
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)