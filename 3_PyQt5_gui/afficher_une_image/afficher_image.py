import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ui_afficher_image import Ui_Dialog

#nouvelle importation
from PyQt5.QtGui import QPixmap
"""
Cette methode d'affichage nécessite un label et un bouton auquel on affecte la fonction afficher()
ici l'image prend la taille du label et n'est pas resize
"""

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

        self.image = QPixmap("image.png")  #nom de votre image  (png jpeg) au format QPixmap

    def afficher(self):
        self.ui.label.clear()                #clear le label
        self.ui.label.setPixmap(self.image)  #afficher dans le label l'image


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
