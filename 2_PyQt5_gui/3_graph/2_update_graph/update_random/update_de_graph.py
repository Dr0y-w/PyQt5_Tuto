import sys
from PyQt5.QtWidgets import QDialog, QApplication
import PyQt5.QtCore as QtCore # pour le timer
from plot_ui import Ui_Dialog
import pyqtgraph as pg
import random as rd


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


        self.ui.graphicsView.setYRange(0,5) # définit la hauteur du graph (axe y)
        self.ui.graphicsView.setXRange(1,4) # définit la longueur du graphe (axe x)
        self.ui.graphicsView.setBackground((0, 0, 0)) # couleur en rgb du background
        self.pen = pg.mkPen(color=(255, 0, 0),width=5) # choix du trait
        self.ui.graphicsView.plot([1,2,3,4],[1,2,5,4], pen=self.pen)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)


    def cl(self): # efface juste l'affichage
        self.ui.graphicsView.clear()

    def clear(self): # efface l'affichage et stop le timer
        self.ui.graphicsView.clear()
        self.timer.stop()

    def update(self): # fonction appeler a chaque timeout, affiche un graphe de point aléatoire
        self.cl()
        self.ui.graphicsView.plot([1, 2, 3, 4], [rd.randint(0, 5) for x in range(4)], pen = self.pen)

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())

