import pygame

class Event:

    def __init__(self, buttons, canvas_size, mainWindow):
        self.done = False
        self.pause = False
        self.buttons = buttons
        self.canvas_size = canvas_size
        self.mainWindow = mainWindow

    def setDone(self):
        self.done = True

    def listen(self):

        while not self.done:

            # print("listen()")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if pygame.mouse.get_pos()[0] < self.canvas_size and pygame.mouse.get_pos()[1] < self.canvas_size:
                        x_mouse, y_mouse = pygame.mouse.get_pos()
                        self.mainWindow.setCellAlive(x_mouse, y_mouse)

                    for button in self.buttons:
                        if button.isOnButton(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                            button.click()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.mainWindow.btn_setRandomGeneration()

                    if event.key == pygame.K_ESCAPE:
                        self.mainWindow.btn_setEmptyGeneration()

                    if event.key == pygame.K_KP_ENTER:
                        self.mainWindow.startGeneration()

            # if not gaming_loop:
            #
            #     gamefield.counting_cells()
            #     gamefield.cell_selection()
            #
            #     gamefield.game_speed_tick()

            pygame.display.update()
