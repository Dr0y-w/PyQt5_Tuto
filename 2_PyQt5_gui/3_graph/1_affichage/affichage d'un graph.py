import sys
from PyQt5.QtWidgets import QDialog, QApplication

import pyqtgraph as pg # module qui permet de gérer les graphs

from affichage_graph import Ui_Dialog # classe généré par QtQesigner

#on utilise le widget Graphics View, qu'on promu en PlotWidget
#Dans qtdesigner:
#une fois le widget graphic view placé, click droit sur celui-ci
#selectionner 'promouvoir en' , et remplir :
#Nom de la classe Promu : PlotWidget
#fichier d'en-tête : pyqtgraph (remplacer celui crée automatiquement)
#cliquer sur ajouter puis promouvoir



class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

        self.ui.graphicsView.setTitle("le graph",color = (0,255,0), size = "10pt") # définit le titre
        self.ui.graphicsView.setYRange(0,5) # définit la hauteur du graph (axe y)
        self.ui.graphicsView.setXRange(1,4) # définit la longueur du graphe (axe x)

        self.ui.graphicsView.setLabel("left","un label", color = 'red') # définit le titre de l'axe y
        self.ui.graphicsView.setLabel("bottom","un autre label") # définit le titre de l'axe x
        self.ui.graphicsView.setBackground((0,0,0)) # couleur en rgb du background
        self.pen = pg.mkPen(color=(255, 0, 0), width=3) # choix du pen définissant les caractéristique du trait
        self.ui.graphicsView.plot([1,2,3,4],[1,2,5,4], pen=self.pen) # d'abord les abscisses ensuite les ordonnées


    def clear(self):
        self.ui.graphicsView.clear() # efface la figure


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
