from panda3d.core import loadPrcFile
loadPrcFile("config.pyc")

from direct.showbase.ShowBase import ShowBase
        
# le corps du programme principal
if __name__ == "__main__":    
    monJeu = ShowBase()
    monJeu.cam.setPos(40,-80,80)
    # Orientation de la caméra
    monJeu.cam.setHpr(20,-30,0)
    # Dessin du decor
    decor = monJeu.loader.loadModel("mes_objets3D/environment")
    # On attache le décor à la cène
    decor.reparentTo(monJeu.render)
    monJeu.run()
