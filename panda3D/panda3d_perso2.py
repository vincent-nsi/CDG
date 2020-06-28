from panda3d.core import loadPrcFile
loadPrcFile("config.pyc")

from direct.showbase.ShowBase import ShowBase

class Jeu(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
class Perso():
    def __init__(self):
          # Affichage de l'objet
        self.perso = monJeu.loader.loadModel("mes_objets3D/panda")
        # Attacher l'objet à la scène
        self.perso.reparentTo(monJeu.render)
        # Modifier la taille de l'objet
        self.perso.setScale(0.02,0.02,0.02)
        # Déplacer l'objet
        self.perso.setPos(-20,100,0)
        # Tourner l'objet
        self.perso.setHpr(90,0,0) 

monJeu = Jeu()
panda = Perso()

monJeu.run()
