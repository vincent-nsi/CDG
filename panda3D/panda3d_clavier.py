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
        self.perso1 = self.loader.loadModel("mes_objets3D/panda")
        self.perso1.setScale(0.02,0.02,0.02)
        self.perso1.setPos(-8,42,0)
        self.perso1.reparentTo(self.render)
        
        self.accept("arrow_left",self.gauche)
        self.accept("mouse1", self.tourne)
    
    def gauche(self):
        pos = self.perso1.getX()
        pos = pos + 1
        self.perso1.setX(pos)
        
    def tourne(self):
        angle = self.perso1.getH()
        angle = angle + 20
        self.perso1.setH(angle)
                 
monJeu = Jeu()

monJeu.run()
