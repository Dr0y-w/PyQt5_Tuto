from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# importation du module PyOpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# importation du module contenant la class générée par Qtdesigner
from sphere_ui import Ui_Dialog
from gen import *


class mainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.angle = 0  # utilisé pour tourner la camera
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.openGLWidget = self.ui.openGLWidget  # raccourci
        self.radius = 6
        self.precision = 25
        self.ui.horizontalSlider.setMinimum(0)
        self.ui.horizontalSlider.setMinimum(10)
        self.ui.horizontalSlider_2.setMinimum(0)
        self.ui.horizontalSlider_2.setMinimum(20)
        self.ui.horizontalSlider_3.setMinimum(0)
        self.ui.horizontalSlider_3.setMinimum(20)
        self.ui.horizontalSlider_3.setValue(20)
        self.distance = 50
        self.x, self.y, self.z = sphere(self.radius, self.precision, [0, 0, 0])
        print(len(self.x))

    def radius(self):
        self.radius = self.ui.horizontalSlider.value()
        self.x, self.y, self.z = sphere(self.radius, self.precision, [0, 0, 0])
    def precision(self):
        self.precision = self.ui.horizontalSlider_2.value()
        self.x, self.y, self.z = sphere(self.radius, self.precision, [0, 0, 0])
    def distance(self):
        self.distance = self.ui.horizontalSlider_3.value()
    def setupUI(self):  # initialisation de la vue et création du timer
        self.openGLWidget.initializeGL() # appelé au premier affichage uniquement
        self.openGLWidget.resizeGL(800, 600)
        self.openGLWidget.paintGL = self.paintGL # raccourci

        timer = QTimer(self)  # Le timer
        timer.timeout.connect(self.openGLWidget.update)  # appelle la fonction en argument (sans parenthèse )
        #ici update appelle la fonction resizeGL et paintGL
        timer.start(10)  # lance le timer pour un temps de 100 ms entre chaque timeout

    def paintGL(self):  # réécriture de la fonction de base pour afficher la scène
                        # appelé a chaque 'update' lancé par le timer
        self.angle += 1
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0, 0, 0, 1)  # définition de la couleur du font,le dernier nombre est l'alpha/la transparence

        glPointSize(100)  # taille initiale
        """changement de la taille des points avec la distance"""
        glPointParameterfv(GL_POINT_DISTANCE_ATTENUATION,(1, 5, 1))  # permet de diminuer la taille des points avec
                        # la distance, (surtout les 2 derniers)
        glPointParameterfv(GL_POINT_SIZE_MAX, 32.0)  # définit la taille maximum des points
        glPointParameterfv(GL_POINT_SIZE_MIN, 0.01)  # définit la taille minimum des points
        glBegin(GL_POINTS)
        glColor3fv((1, 1, 1))

        for i in range(len(self.y)):
            glVertex3f(self.x[i], self.y[i], self.z[i])

        glEnd()

        glMatrixMode(GL_PROJECTION)  # charge la matrice de projection
        """ on change ici les options de la projection sur l'écran """
        glLoadIdentity()  # charge une matrice identité
        gluPerspective(45.0, 4.0 / 3.0, 1, 1000)  # fov , ratio , distance de vue proche, distance de vue de loin

        glMatrixMode(GL_MODELVIEW)  # charge la matrice de caméra
        """ on change ici la position de la caméra """
        glLoadIdentity()  # charge une matrice identité
        gluLookAt(0, 1, -self.distance,
                  0, 0, 0,
                  0, 1, 0)
        # coordonnées de la position de la caméra  ,coordonnées du point vers lequel elle est dirigée, axe vertical de la caméra
        glRotatef(0.4*self.angle, 0, 1, 0)  # permet de tourner la caméra autour de l'axe x ,y ,z

        #glTranslatef( 0, 0, 0.1*self.angle)#permet de déplacer la camera ,
        # mais est impacté par la rotation de la camera



app = QApplication(sys.argv)
window = mainWindow()
window.setupUI() # on initialize le QOpenGLwidget
window.show()
sys.exit(app.exec_())
