class Menu:
    def __init__(self, x, y, h, w, pygame, win, color):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.pygame = pygame
        self.win = win
        self.color = color
    
    def draw(self):
        self.pygame.draw.rect(self.win, self.color, (self.x, self.y, self.w, self.h))