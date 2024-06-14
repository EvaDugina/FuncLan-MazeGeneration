import pygame

from maze import MazeGenerator
from paintController import Painter
from events import Event
from gui_elements import Button


class MainWindow:
    root = None

    cellSize = 5
    mazeType = [[3, 7], [1, 2, 3, 4]]
    screenSize = 750
    mazeSize = screenSize // cellSize
    liveSpeed = 100
    buttons = []

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Клеточный автомат')

        self.root = pygame.display.set_mode((1000, 750))

        self.event = Event(self.buttons, self.screenSize, self)

        self.applyMazeConfiguration()

        self.event.listen()



    def createButtons(self):
        buttons = []

        btn_submit = Button(775, 20, 100, 30, buttonText="РАЗМЕР КЛЕТОК = 5", onclickFunction=self.btn_setCellSize5, argv=None)
        self.root.blit(btn_submit.buttonSurf, btn_submit.buttonRect)
        self.buttons.append(btn_submit)

        btn_submit = Button(775, 60, 100, 30, buttonText="РАЗМЕР КЛЕТОК = 10", onclickFunction=self.btn_setCellSize10, argv=None)
        self.root.blit(btn_submit.buttonSurf, btn_submit.buttonRect)
        self.buttons.append(btn_submit)

        btn_submit = Button(775, 100, 100, 30, buttonText="B-3 S-12345", onclickFunction=self.btn_b3s12345, argv=None)
        self.root.blit(btn_submit.buttonSurf, btn_submit.buttonRect)
        self.buttons.append(btn_submit)

        btn_submit = Button(775, 140, 100, 30, buttonText="B-3 S-2345", onclickFunction=self.btn_b3s2345, argv=None)
        self.root.blit(btn_submit.buttonSurf, btn_submit.buttonRect)
        self.buttons.append(btn_submit)

        btn_submit = Button(775, 180, 100, 30, buttonText="B-3 S-1234", onclickFunction=self.btn_b3s2345, argv=None)
        self.root.blit(btn_submit.buttonSurf, btn_submit.buttonRect)
        self.buttons.append(btn_submit)

        btn_submit = Button(775, 220, 100, 30, buttonText="B-37 S-1234", onclickFunction=self.btn_b37s1234, argv=None)
        self.root.blit(btn_submit.buttonSurf, btn_submit.buttonRect)
        self.buttons.append(btn_submit)

        btn_submit = Button(775, 260, 100, 30, buttonText="СКОРОСТЬ ИГРЫ Х1", onclickFunction=self.setLiveSpeed, argv=1)
        self.root.blit(btn_submit.buttonSurf, btn_submit.buttonRect)
        self.buttons.append(btn_submit)

        btn_submit = Button(775, 300, 100, 30, buttonText="СКОРОСТЬ ИГРЫ Х10", onclickFunction=self.setLiveSpeed,
                            argv=10)
        self.root.blit(btn_submit.buttonSurf, btn_submit.buttonRect)
        self.buttons.append(btn_submit)

        btn_submit = Button(775, 340, 100, 30, buttonText="СКОРОСТЬ ИГРЫ Х60", onclickFunction=self.setLiveSpeed,
                            argv=60)
        self.root.blit(btn_submit.buttonSurf, btn_submit.buttonRect)
        self.buttons.append(btn_submit)

        btn_submit = Button(775, 380, 100, 30, buttonText="СКОРОСТЬ ИГРЫ Х100", onclickFunction=self.setLiveSpeed,
                            argv=100)
        self.root.blit(btn_submit.buttonSurf, btn_submit.buttonRect)
        self.buttons.append(btn_submit)

        btn_submit = Button(775, 500, 100, 30, buttonText="ЗАПУСТИТЬ ГЕНЕРАЦИЮ", onclickFunction=self.startGeneration, argv=None)
        self.root.blit(btn_submit.buttonSurf, btn_submit.buttonRect)
        self.buttons.append(btn_submit)

        self.buttons = buttons

        pygame.display.update()


    def applyMazeConfiguration(self):
        self.mazeSize = self.screenSize // self.cellSize
        painter = Painter(self.root, self.mazeSize, self.cellSize, self)
        self.MazeGenerator = MazeGenerator(self.mazeSize, self.mazeType, self.liveSpeed, painter)
        self.MazeGenerator.setLiveSpeed(self.liveSpeed)
        self.MazeGenerator.setRandomGeneration()
        self.createButtons()


    def btn_setCellSize5(self):
        print("btn_setCellSize5()")
        self.cellSize = 5
        self.applyMazeConfiguration()

    def btn_setCellSize10(self):
        print("btn_setCellSize10()")
        self.cellSize = 10
        self.applyMazeConfiguration()

    def btn_b3s12345(self):
        print("btn_b3s12345()")
        self.mazeType = [[3], [1, 2, 3, 4, 5]]
        self.applyMazeConfiguration()

    def btn_b3s2345(self):
        print("btn_b3s2345()")
        self.mazeType = [[3], [2, 3, 4, 5]]
        self.applyMazeConfiguration()

    def btn_b37s1234(self):
        print("btn_b37s1234()")
        self.mazeType = [[3, 7], [1, 2, 3, 4]]
        self.applyMazeConfiguration()

    def btn_setEmptyGeneration(self):
        print("btn_setEmptyGeneration()")
        self.MazeGenerator.setEmptyGeneration()

    def btn_setRandomGeneration(self):
        print("btn_setRandomGeneration()")
        self.MazeGenerator.setRandomGeneration()

    def btn_startGeneration(self):
        print("btn_startGeneration()")
        self.startGeneration()

    def setLiveSpeed(self, live_speed):
        print("setLiveSpeed()")
        self.liveSpeed = live_speed
        self.MazeGenerator.setLiveSpeed(live_speed)


    def setCellAlive(self, x, y):
        print("setCellAlive()")
        self.MazeGenerator.changeCellStatus(x // self.cellSize, y // self.cellSize)

    def pauseGame(self):
        self.MazeGenerator.setPause()

    def unpauseGame(self):
        self.MazeGenerator.setUnPause()

    def startGeneration(self):
        self.event.setDone()
        self.MazeGenerator.generate()


game = MainWindow()