from panda3d.core import loadPrcFile
loadPrcFile("config.pyc")

from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
       
class Perso():
    def __init__(self, modele, x, y, z, direction):
          # Les variables de l'objet
        self.perso = modele
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction
        # Modifier la taille de l'objet
        self.perso.setScale(0.02,0.02,0.02)
        # Déplacer l'objet
        self.perso.setPos(self.x,self.y,self.z)
        # Tourner l'objet
        self.perso.setH(self.direction)

if __name__ == "__main__":
    monJeu = ShowBase()
    # On charge le modèle 3D
    modeleJoueur = Actor("mes_objets3D/panda")
    # On l'attache à la scène
    modeleJoueur.reparentTo(monJeu.render)
    # On règle les paramètres du joueur
    joueur = Perso(modeleJoueur, -20,100,0, 90)
    # On lance le jeu
    monJeu.run()

