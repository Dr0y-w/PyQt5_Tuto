from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from qtdesigner_ui import Ui_Dialog #class générere par qtdesigner
from mudule_forme import * #module contenant la génération du cube

class mainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.angle = 0 #utile pour tourner la camera
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.openGLWidget = self.ui.openGLWidget



    def setupUI(self): #on initialize la vue et on cree le timer
        self.openGLWidget.initializeGL()
        self.openGLWidget.resizeGL(800, 600)
        self.openGLWidget.paintGL = self.paintGL


        timer = QTimer(self) #Le timer
        timer.timeout.connect(self.openGLWidget.update)#lance la fonction en argument
        timer.start(10) #temps entre chaque timeout en milliseconde


    def paintGL(self):#on écrit la fonction de base pour afficher la scene, appelé a chaque update lancé par le chrono
        self.angle += 1
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(1, 0, 0, 1) #couleur du font,le dernier est l'alpha/ la transparence
        glColor3f(1, 1, 1) #couleur r,g,b de la forme

        """obtention des vertices et des edges de la premiere forme """
        C1 = Cube([-0.5, -0.5, -0.5])
        vertices = C1.vertices
        edges = C1.edges
        """génération de la forme """
        glBegin(GL_LINES)
        #indique le type de forme a tracé :ici des lignes , GL_QUADS permetterais de tracer des faces avec le code adatpé
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

        """obtention des vertices et des edges de la deuxieme forme """
        C2 = Cube([-0.5, 1.5, -0.5])
        vertices = C2.vertices
        edges = C2.edges
        """génération de la forme """
        glBegin(GL_LINES)
        # indique le type de forme a tracé :ici des lignes , GL_QUADS permetterais de tracer des faces avec le code adatpé
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()
        """grid"""
        g1 = Grid(15)
        vertices = g1.vertices
        edges = g1.edges

        """génération de la forme """
        glBegin(GL_LINES)
        # indique le type de forme a tracé :ici des lignes , GL_QUADS permetterais de tracer des faces avec le code adatpé
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()


        glMatrixMode(GL_PROJECTION)#charge la matrice de projection
        glLoadIdentity()#charge une matrice identité
        gluPerspective(45.0, 4.0 / 3.0, 1, 40)#fov , ratio , distance de vue proche, distance de vue loin

        glMatrixMode(GL_MODELVIEW)#charge la matrice de camera
        glLoadIdentity()#charge une matrice identité
        gluLookAt(0, 2, -10,
                  0, 0, 0,
                  0, 1, 0)
        # coordoné de la position de l'oeil ,cooedoné du point vers le quel elle regarde, vecteur up
        glRotatef(self.angle, 0, 1, 0)#permet de tourner la camera
        #glTranslatef( 0, 0, 0,1*self.angle)#permet de déplacer la camera









app = QApplication(sys.argv)
window = mainWindow()
window.setupUI()
window.show()
sys.exit(app.exec_())