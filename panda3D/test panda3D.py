from panda3d.core import loadPrcFile
loadPrcFile("config.pyc")

from direct.showbase.ShowBase import ShowBase

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
'''
        self.environ = loader.loadModel("mes_objets3D/panda-model")
        self.environ.reparentTo(render)
        self.environ.setScale(0.02,0.02,0.02)
        self.environ.setPos(0,50,0)
'''       
game = Game()
game.run()