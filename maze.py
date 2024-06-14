import time
from functools import reduce

import pygame
import random


class MazeGenerator:

    def __init__(self, maze_size, type, live_speed, Painter):
        self.mazeSize = maze_size
        self.type = type
        self.liveSpeed = live_speed
        self.randomRadius = 20
        self.stop = False
        self.pause = False

        self.Painter = Painter

    def getIndexesNeighbours(self):
        return [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    # Функция определения кол-ва соседей
    def getCountAliveNeighbours(self, x, y, cells):
        neighboursIndexes = self.getIndexesNeighbours()
        func_validation = lambda elem: 0 <= elem[0] + x < self.mazeSize and 0 <= elem[1] + y < self.mazeSize
        neighboursIndexes = list(filter(func_validation, neighboursIndexes))
        func_getNeighboursCount = lambda count, neighbour_xy: count + 1 - cells[x + neighbour_xy[0]][y + neighbour_xy[1]]
        return reduce(func_getNeighboursCount, neighboursIndexes, 0)

    def getCellStatusByCondition(self, cell, count_neighbours):
        if cell == 1:
            if count_neighbours in self.type[0]:
                return 0
            return 1

        if count_neighbours not in self.type[1]:
            return 1

        return 0

    #
    #
    #

    def changeCellStatus(self, x, y):
        self.begin_cells[x][y] = 1 - self.begin_cells[x][y]
        self.Painter.updateCanvas(self.begin_cells)

    def setRandomGeneration(self):
        self.begin_cells = [[self.setRandom(i, j) for j in range(self.mazeSize)] for i in range(self.mazeSize)]
        self.Painter.updateCanvas(self.begin_cells)

    def setEmptyGeneration(self):
        self.begin_cells = [[0 for j in range(self.mazeSize)] for i in range(self.mazeSize)]
        self.Painter.updateCanvas(self.begin_cells)

    def setRandom(self, x, y):
        if self.mazeSize // 2 - self.randomRadius < x < self.mazeSize // 2 + self.randomRadius \
                and self.mazeSize // 2 - self.randomRadius < y < self.mazeSize // 2 + self.randomRadius:
            return random.choice([0, 1])

        return 1

    def setPause(self):
        self.pause = True

    def setStop(self):
        self.stop = True

    def setUnPause(self):
        self.pause = False

    def setLiveSpeed(self, live_speed):
        self.liveSpeed = live_speed

    #
    #
    #

    def generate(self):
        self.main_while(self.begin_cells, 0)

    def main_while(self, cells, depth):

        print(f"main_while() -- {depth}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop = True

        if self.pause:
            return 0

        self.Painter.updateCanvas(cells)

        time.sleep(1 / self.liveSpeed)

        self.main_while(
            [[self.getCellStatusByCondition(cells[i][j], self.getCountAliveNeighbours(i, j, cells))
              for j in range(self.mazeSize)] for i in range(self.mazeSize)],
            depth+1)



    def clean(self):
        self.setEmptyGeneration()


