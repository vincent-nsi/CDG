from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/models/environment")
        # Reparent the model to render.pview models/panda-model.egg.pz
        self.pandaActor = Actor("models/panda-model")

app = MyApp()
app.run()