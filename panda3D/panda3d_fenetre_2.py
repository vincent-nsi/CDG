from panda3d.core import loadPrcFile
loadPrcFile("config.pyc")

from direct.showbase.ShowBase import ShowBase
      
monJeu = ShowBase()
monJeu.run()