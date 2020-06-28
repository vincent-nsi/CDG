from panda3d.core import loadPrcFile
loadPrcFile("config.pyc")

from direct.showbase.ShowBase import ShowBase

class Jeu(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        # Positionnement de la caméra
        self.cam.setPos(40,-80,80)
        # Orientation de la caméra
        self.cam.setHpr(20,-30,0)
        # Dessin du decor
        decor = self.loader.loadModel("mes_objets3D/environment")
        decor.reparentTo(self.render)
        
        #decor.setScale(8,0,0)
        
        # Affichage d'un objet
        perso1 = self.loader.loadModel("mes_objets3D/panda")
        perso1.setScale(0.02,0.02,0.02)
        perso1.setPos(-8,42,0)
        perso1.reparentTo(self.render)
          
monJeu = Jeu()

monJeu.run()
