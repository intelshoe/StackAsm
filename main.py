from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Set windows size
        properties = WindowProperties()
        properties.setSize(900, 800)
        self.win.requestProperties(properties)

        # disable mouse-based camera-control
        self.disableMouse()

game = Game()
game.run()