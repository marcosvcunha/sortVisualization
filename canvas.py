import pygame

class Canvas:
    def __init__(self, x, y, h, w, pygame, win, color, barsColor, myList):
        """[summary]

        Args:
            x (int): [description]
            y (int): [description]
            h (int): [description]
            w (int): [description]
            pygame (pygame): [description]
            win (pygame.win): [description]
            color ((r, g, b)): [description]
            myList (list<int>): [description]
        """
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.pygame = pygame
        self.win = win
        self.color = color
        self.barsColor = barsColor
        self.list = myList
        self.listSize = len(self.list)
    
    def draw(self):
        self.pygame.draw.rect(self.win, self.color, (self.x, self.y, self.w, self.h))
        ## Draw List
        for i in range(self.listSize):
            self.pygame.draw.rect(self.win, self.barsColor, (i * 5 + self.x, self.h - self.list[i] + self.y, 5, self.list[i]))
            