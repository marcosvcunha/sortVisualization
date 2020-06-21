import sys
sys.path.append('../')
from sort import bubbleSort, mergeSort, quickSort
from createList import randomList
from canvas import Canvas
from menu import Menu
from button import Button
# import threading
from thread import thread_with_trace
import pygame
import time

grey = (125, 125, 125)
white = (255, 255, 255)
black = (0, 0, 0)
purple= (0x5b, 0x34, 0x9e)

class Screen():
    
    def __init__(self):
        pygame.init()
        self.sortingThread = None
        self.win = pygame.display.set_mode((840, 540))
        self.list = randomList(100, 500)
        self.canvas = Canvas(20, 20, 500, 500, pygame, self.win, white, purple,self.list)
        self.menu = Menu(540, 0, 540, 300, pygame, self.win, grey)
        self.gameOver = False
        self.speed = 5
        self.sleepTime = [0.01]
        self.sortingAlg = 'Bubble Sort'
        self.buttons = [
            Button(pygame, self.win, x=690, y=540 - 40, height=60, width=150, text='Shuffle', onPressed=self.shuffleList),
            Button(pygame, self.win, x=690, y=540 - 120, height=60, width=150, text='Start', onPressed=self.startStopFunc),
            Button(pygame, self.win, x=690, y= 540 - 480, height=30, width=75, text='Speed', color=grey),
            Button(pygame, self.win, x=690, y= 540 - 430, height=30, width=40, text=str(self.speed), color=grey),
            Button(pygame, self.win, x=630, y= 540 - 430, height=30, width=40, text='-', color=white, onPressed=self.decreaseSpeed),
            Button(pygame, self.win, x=750, y= 540 - 430, height=30, width=40, text='+', color=white, onPressed=self.increaseSpeed),
            Button(pygame, self.win, x=690, y= 540 - 380, height=30, width=75, text='Algorithm', color=grey),
            Button(pygame, self.win, x=690, y= 540 - 330, height=30, width=40, text=self.sortingAlg, color=grey),
            Button(pygame, self.win, x=600, y= 540 - 330, height=30, width=40, text='<', color=white, onPressed=self.nextAlg),
            Button(pygame, self.win, x=780, y= 540 - 330, height=30, width=40, text='>', color=white, onPressed=self.nextAlg),
            
        ]
        # self.shuffleButton = Button(pygame, self.win, x=690, y=540 - 120, height=60, width=150, text='Shuffle', onPressed=self.shuffleList)
        # self.startStopButton = Button(pygame, self.win, x=690, y=540 - 200, height=60, width=150, text='Start', onPressed=self.startStopFunc)
        self.sorting = False

    def run(self):
        try:
            while(not self.gameOver):
                ## Handle Time
                time.sleep(1/30)
                self.handleEvents()
                self.draw()
        except Exception as e:
            print('Erro: ' + str(e))
        if(self.sortingThread != None):
            self.sortingThread.kill()        

    def draw(self):
        self.win.fill((255,255,255))
        self.canvas.draw()
        self.menu.draw()
        for button in self.buttons:
            button.draw()
        pygame.display.update()
        pass

    def handleEvents(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                self.gameOver = True
            if(event.type == pygame.MOUSEBUTTONDOWN):
                for button in self.buttons:
                    button.click(event.dict['pos'][0], event.dict['pos'][1])

    def startStopFunc(self):
        if(self.sorting):
            self.buttons[1].setText('Start')
            self.sortingThread.kill()
            self.sorting = False
        else:
            self.buttons[1].setText('Stop')
            self.sortingThread = thread_with_trace(target=self.sortList, args=(self.list,))
            self.sorting = True
            self.sortingThread.start()

    def shuffleList(self):
        if(not self.sorting):
            shuffledList = randomList(len(self.list), 500)
            for i in range(len(self.list)):
                self.list[i] = shuffledList[i]

    def sortList(self, myList):
        if(self.sortingAlg == 'Bubble Sort'):
            bubbleSort(myList, delay=self.sleepTime)
        elif(self.sortingAlg == 'Merge Sort'):
            mergeSort(myList, delay=self.sleepTime)
        elif(self.sortingAlg == 'Quick Sort'):
            quickSort(myList, delay=self.sleepTime)
        self.buttons[1].setText('Start')
        self.sorting = False

    def increaseSpeed(self):
        if(self.speed < 10):
            self.speed += 1
            self.sleepTime[0] -= (1/100)*0.19
        self.buttons[3].setText(str(self.speed))

    def decreaseSpeed(self):
        if(self.speed > 1):
            self.speed -= 1
            self.sleepTime[0] += (1/100)*0.2
        self.buttons[3].setText(str(self.speed))

    def nextAlg(self):
        if(self.sortingAlg == 'Bubble Sort'):
            self.sortingAlg = 'Merge Sort'
        elif(self.sortingAlg == 'Merge Sort'):
            self.sortingAlg = 'Quick Sort'
        elif(self.sortingAlg == 'Quick Sort'):
            self.sortingAlg = 'Bubble Sort'
        self.buttons[7].setText(self.sortingAlg)
    
if __name__ == "__main__":
    screen = Screen()
    screen.run()