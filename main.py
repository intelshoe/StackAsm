from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
import time

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Set windows size
        properties = WindowProperties()
        properties.setSize(900, 880)
        self.win.requestProperties(properties)

        # disable mouse-based camera-control
        ## self.disableMouse()

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Attach to root of scene to show environment
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.11, 0.11, 0.11)
        self.scene.setPos(8, 34, -4)



game = Game()
game.run()