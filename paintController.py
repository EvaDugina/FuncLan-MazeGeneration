import pygame


class Painter:

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self, root, maze_size, cell_size, mainWindow):
        self.root = root
        self.mainWindow = mainWindow
        self.buttons = []
        self.mazeSize = maze_size
        self.cellSize = cell_size

        # Заполняем экран белым цветом
        self.root.fill(self.WHITE)

    def updateCanvas(self, cells):

        # Проходимся по всем клеткам
        for i in range(0, len(cells)):
            for j in range(0, len(cells[i])):
                # print(cells[i][j], i, j)
                pygame.draw.rect(self.root, (255 * cells[i][j] % 256, 0, 0),
                                 [i * self.cellSize, j * self.cellSize, self.cellSize, self.cellSize])

        # Рисуем сетку
        for i in range(0, self.mazeSize):
            pygame.draw.line(self.root, self.BLACK, (0, i * self.cellSize), (self.mazeSize * self.cellSize, i * self.cellSize))
        for j in range(0, self.mazeSize):
            pygame.draw.line(self.root, self.BLACK, (j * self.cellSize, 0), (j * self.cellSize, self.mazeSize * self.cellSize))

        pygame.display.update()