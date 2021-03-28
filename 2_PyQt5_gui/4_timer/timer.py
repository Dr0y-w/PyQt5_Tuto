import sys
from PyQt5.QtWidgets import QDialog, QApplication
import PyQt5.QtCore as QtCore
from timer_ui import Ui_Dialog


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

        self.timer = QtCore.QTimer(self) # creation de l'objet
        self.timer.timeout.connect(self.fonction1)   # définition de ce qu'il se passe à chaque timeout
                                                    # prend en argument le nom d'une fonction, (sans parenthèse)
        self.timer.start(1000) # définit l'intervalle entre chaque timeout en milliseconde

    def fonction1(self):
        print("fonction1") # on affiche dans la console un message
    def fonction2(self):
        print("fonction2")

    def stop(self):
        self.timer.stop() # on arrête le timer
        print("stop")

    def restart(self): # on relance le timer
        self.timer.timeout.connect(self.fonction2) # on ajoute une autre fonction à chaque timeout
        self.timer.start(2000) # on peut redéfinir le temps d'intervalle


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
