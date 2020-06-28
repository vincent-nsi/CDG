from panda3d.core import loadPrcFile
loadPrcFile("config.pyc")

from direct.showbase.ShowBase import ShowBase
       
class Perso():
    def __init__(self, modele, x, y, z, direction):
          # Affichage de l'objet
        self.perso = modele
        # Modifier la taille de l'objet
        self.perso.setScale(0.02,0.02,0.02)
        # Déplacer l'objet
        self.perso.setPos(x,y,z)
        # Tourner l'objet
        self.perso.setH(direction)

if __name__ == "__main__":
    monJeu = ShowBase()
    # On charge le modèle 3D
    modeleJoueur = monJeu.loader.loadModel("mes_objets3D/panda")
    # On l'attache à la scène
    modeleJoueur.reparentTo(monJeu.render)
    # On règle les paramètres du joueur
    joueur = Perso(modeleJoueur, -20,100,0, 90)
    # On lance le jeu
    monJeu.run()

