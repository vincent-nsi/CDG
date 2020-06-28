from panda3d.core import loadPrcFile
loadPrcFile("config.pyc")

from direct.showbase.ShowBase import ShowBase

class Jeu(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        # Affichage de l'objet
        self.perso1 = self.loader.loadModel("mes_objets3D/panda")
        # Attacher l'objet à la scène
        self.perso1.reparentTo(self.render)
        # Modifier la taille de l'objet
        self.perso1.setScale(0.02,0.02,0.02)
        # Déplacer l'objet
        self.perso1.setPos(-20,100,0)
        # Tourner l'objet
        self.perso1.setHpr(90,0,0)
        self.

          
monJeu = Jeu()

monJeu.run()
