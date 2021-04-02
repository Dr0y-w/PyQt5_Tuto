from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# importation du module PyOpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# importation du module contenant la class générée par Qtdesigner
from untitled import Ui_Dialog
from module_gen import *


class mainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.angle = 0  # utilisé pour tourner la camera
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.openGLWidget = self.ui.openGLWidget  # raccourci

    def setupUI(self):  # initialisation de la vue et création du timer
        self.openGLWidget.initializeGL() # appelé au premier affichage uniquement
        self.openGLWidget.resizeGL(800, 600)
        self.openGLWidget.paintGL = self.paintGL # raccourci

        timer = QTimer(self)  # Le timer
        timer.timeout.connect(self.openGLWidget.update)  # appelle la fonction en argument
        #ici update appelle la fonction resizeGL et paintGL
        timer.start(10)  # lance le timer pour un temps de 10 ms entre chaque timeout

    def paintGL(self):  # réécriture de la fonction de base pour afficher la scène
                        # appelé a chaque 'update' lancé par le timer
        self.angle += 1
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0, 0, 0, 1)  # définition de la couleur du font,le dernier nombre est l'alpha/la transparence

        c1 = Grid(5)
        vertices = c1.vertices
        edges = c1.edges
        glBegin(GL_LINES) # début de l'affichage des lignes
        # indique le type de formes à tracer (GL_LINES = des lignes). GL_QUADS permettrait de tracer des faces avec le code adapté
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd() # fin de l'affichage des lignes

        """glBegin() et glEnd() ne sont pas très optimisées
         Il existe des manières plus efficace pour faire la même chose mais plus complexe
         chercher 'modern OpenGL' et  'VAO' ou 'VBO'
         """

        glMatrixMode(GL_PROJECTION)  # charge la matrice de projection
        """ on change ici les options de la projection sur l'écran """
        glLoadIdentity()  # charge une matrice identité
        gluPerspective(45.0, 4.0 / 3.0, 1, 40)  # fov , ratio , distance de vue proche, distance de vue de loin

        glMatrixMode(GL_MODELVIEW)  # charge la matrice de caméra
        """ on change ici la position de la caméra """
        glLoadIdentity()  # charge une matrice identité
        gluLookAt(0, 2, -5,
                  0, 0, 0,
                  0, 1, 0)
        # coordonnées de la position de la caméra  ,coordonnées du point vers lequel elle est dirigée, axe vertical de la caméra
        #glRotatef(1*self.angle, 1, 1, 1)  # permet de tourner la caméra autour de l'axe x,y,z

        #glTranslatef( 0, 0, 0.1*self.angle)#permet de déplacer la camera ,
        # mais est impacté par la rotation de la camera



app = QApplication(sys.argv)
window = mainWindow()
window.setupUI() # on initialize le QOpenGLwidget
window.show()
sys.exit(app.exec_())
