from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# importation du module PyOpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# importation du module contenant la class générée par Qtdesigner
from update_slider_ui import Ui_Dialog



class mainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.angle = 225  # utilisé pour tourner la camera = 90°
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.openGLWidget = self.ui.openGLWidget  # raccourci
        self.y = 0
        self.ui.verticalSlider.setValue(0)
        self.ui.verticalSlider.setMinimum(-10)
        self.ui.verticalSlider.setMaximum(10)

    def update_slider(self):
        self.y = self.ui.verticalSlider.value()



    def setupUI(self):  # initialisation de la vue et création du timer
        self.openGLWidget.initializeGL() # appelé au premier affichage uniquement
        self.openGLWidget.resizeGL(800, 600)
        self.openGLWidget.paintGL = self.paintGL # raccourci

        timer = QTimer(self)  # Le timer
        timer.timeout.connect(self.openGLWidget.update)  # appelle la fonction en argument (sans parenthèse )
        #ici update appelle la fonction resizeGL et paintGL
        timer.start(10)  # lance le timer pour un temps de 10 ms entre chaque timeout

    def paintGL(self):  # réécriture de la fonction de base pour afficher la scène
                        # appelé a chaque 'update' lancé par le timer

        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0, 0, 0, 1)  # définition de la couleur du font,le dernier nombre est l'alpha/la transparence


        glBegin(GL_LINES) # début de l'affichage des lignes
        # indique le type de formes à tracer (GL_LINES = des lignes). GL_QUADS permettrait de tracer des faces avec le code adapté

        # un vertex est une liste ou un tuple de 3 int ou float (x,y,z)
        """affichage du segment rouge correspondant à la premiere coordonnée 'x' des vertices"""
        glColor3f(1, 0, 0) # couleur en rgb du segment, ici rouge
        glVertex3fv((0,0,0)) # première extrémité de l'axe x
        # glVertex3fv prend en argument un vertex
        glVertex3fv((1, 0, 0)) # seconde extrémité de l'axe x

        """on affiche le segment vert correspondant à la deuxième coordonnée  'y' des vertices"""
        glColor3f(0, 1, 0) # couleur r,g,b de la forme - vert
        glVertex3fv((0, 0, 0))
        glVertex3fv((0, 1, 0))

        """on affiche le segment bleu correspondant à la dernière  coordonnée 'z' des vertices"""
        glColor3f(0, 0, 1) # couleur r,g,b de la forme - bleu
        glVertex3fv((0, 0, 0))
        glVertex3fv((0, 0, 1))

        """affichage d'une ligne de 3 points dont un qui s'update"""
        glColor3f(1, 1, 1)
        glVertex3fv((0, 0, 0))
        glVertex3fv((0, 0, 1))
        glVertex3fv((0, 0, 1))
        glVertex3fv((0, 0.1*self.y, 2))
        glVertex3fv((0, 0.1*self.y, 2))
        glVertex3fv((0, 0, 3))
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
        gluLookAt(1, 1, -4,
                  1, 0, 0,
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
