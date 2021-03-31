import sys
from PyQt5.QtWidgets import QDialog, QApplication
from graph_slider_ui import Ui_Dialog
import pyqtgraph as pg


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

        self.ui.graphicsView.setYRange(0, 11) # définit la hauteur du graph (axe y)
        self.ui.graphicsView.setXRange(1, 6) # définit la longueur du graphe (axe x)
        self.ui.graphicsView.setBackground((0,0,0)) # couleur en rgb du background
        self.pen = pg.mkPen(color=(255, 0, 0),width=5) # choix du trait
        self.x = [1,2,3,4,5]
        self.y = [0, 0, 0, 0, 0]
        self.ui.graphicsView.plot(self.x ,self.y, pen=self.pen)

        self.slider = [self.ui.verticalSlider, self.ui.verticalSlider_2, self.ui.verticalSlider_3, self.ui.verticalSlider_4, self.ui.verticalSlider_5]
        for slider in self.slider:
            slider.setMinimum(0)
            slider.setMaximum(10)


    def clear(self):
        self.ui.graphicsView.clear()

    def plot_(self):

        self.clear()
        self.ui.graphicsView.plot(self.x,self.y,pen = self.pen)

    def s1(self):
        self.clear()
        self.y[0] = self.slider[0].value()

        self.plot_()

    def s2(self):
        self.clear()
        self.y[1] = self.slider[1].value()
        self.plot_()
    def s3(self):
        self.clear()
        self.y[2] = self.slider[2].value()
        self.plot_()
    def s4(self):
        self.clear()
        self.y[3] = self.slider[3].value()
        self.plot_()
    def s5(self):
        self.clear()
        self.y[4] = self.slider[4].value()
        self.plot_()

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())

