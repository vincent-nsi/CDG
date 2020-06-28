from panda3d.core import loadPrcFile
loadPrcFile("config.pyc")

from direct.showbase.ShowBase import ShowBase

class Perso():
    def __init__(self, modele, x, y, z, direction):
          # Les variables de l objet
        self.perso = modele
        self.x = x
        # Modifier la taille de l'objet
        self.perso.setScale(0.02,0.02,0.02)
        # Déplacer l'objet
        self.perso.setPos(x,y,z)
        # Tourner l'objet
        self.perso.setH(direction)

    def avance(self):
        # On lit la coordonnée x du personnage
        #pos = self.x
        # On lui ajoute 1
        #pos = pos + 1
        # On renvoie la nouvelle coordonnée
        self.x = self.x + 1
        self.perso.setX(self.x)


# le corps du programme principal
if __name__ == "__main__":    
    monJeu = ShowBase()
    ######## MISE EN PLACE DU DECOR
    monJeu.cam.setPos(40,-80,80)
    # Orientation de la caméra
    monJeu.cam.setHpr(20,-30,0)
    # Dessin du decor
    decor = monJeu.loader.loadModel("mes_objets3D/environment")
    # On attache le décor à la cène
    decor.reparentTo(monJeu.render)
    ######## AJOUT DU PERSONNAGE
    # On charge le modèle 3D
    modeleJoueur = monJeu.loader.loadModel("mes_objets3D/panda")
    # On l'attache à la scène
    modeleJoueur.reparentTo(monJeu.render)
    # On règle les paramètres du joueur
    joueur = Perso(modeleJoueur, 0, 42, 0, 45)
    ######## GESTION DES EVENEMENTS
    monJeu.accept("arrow_left",joueur.avance)


    monJeu.run()
