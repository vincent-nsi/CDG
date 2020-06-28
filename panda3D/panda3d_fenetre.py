# On utilise un fichier de paramètres de la fenêtre
from panda3d.core import loadPrcFile
loadPrcFile("config.pyc")

from direct.showbase.ShowBase import ShowBase

# le corps du programme principal
if __name__ == "__main__":    
    monJeu = ShowBase()
    monJeu.run()