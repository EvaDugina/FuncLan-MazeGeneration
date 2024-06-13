import pygame

class Button:

    def __init__(
        self,
        x,
        y,
        width,
        height,
        buttonText="Button",
        onclickFunction=None,
        onePress=False,
        argv=0,
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.argv = argv

        self.fillColors = {
            "normal": "#ffffff",
            "hover": "#666666",
            "pressed": "#333333",
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        font = pygame.font.SysFont("Arial", 20)
        self.buttonSurf = font.render(buttonText, True, (0, 0, 0))

        self.alreadyPressed = False

    def isOnButton(self, x, y):
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            return True
        return False

    def click(self):
        if self.argv is not None:
            self.onclickFunction(self.argv)
        else:
            self.onclickFunction()