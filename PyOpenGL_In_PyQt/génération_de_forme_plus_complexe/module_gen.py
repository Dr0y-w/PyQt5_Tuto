from copy import deepcopy
from Vertex import Vertex


class Cube:  # renvoi les vertices et les edges
    def __init__(self, longueur=1, origine=[0, 0, 0]):
        self.origine = Vertex(*origine)
        self.longueur = longueur
        self.vertices = self.gen()[0]
        self.edges = self.gen()[1]


    def gen(self):
        vertices = [
             self.origine.vertex,
             (deepcopy(self.origine) + ("x" + str(self.longueur))).vertex,
             (deepcopy(self.origine) + ("y" + str(self.longueur))).vertex,
             (deepcopy(self.origine) + ("z" + str(self.longueur))).vertex,
             (deepcopy(self.origine) + ("x" + str(self.longueur)) + ("y" + str(self.longueur))).vertex,
             (deepcopy(self.origine) + ("x" + str(self.longueur)) + ("y" + str(self.longueur)) + ("z" + str(self.longueur))).vertex,
             (deepcopy(self.origine) + ("x" + str(self.longueur)) + ("z" + str(self.longueur))).vertex,
             (deepcopy(self.origine) + ("z" + str(self.longueur)) + ("y" + str(self.longueur))).vertex
            ]
        edges = ((0, 1), (0, 2), (0, 3), (1, 4), (1, 6), (2, 7),
                 (4, 5), (5, 6), (3, 6), (5, 7), (2, 4), (3, 7))
        return vertices, edges


class Grid:
    def __init__(self, rayon, origine=[0, 0, 0]):
        self.origine = Vertex(*origine)
        self.rayon = rayon
        self.vertices = self.gen()[0]
        self.edges = self.gen()[1]

    def gen(self):
        orig = deepcopy(self.origine)
        vertices = []
        edges = []
        for i in range(self.rayon+1):
            orig - "x"
            orig - "z"
        or1 = deepcopy(orig)
        #gen des vertices
        for i in range(2*self.rayon+1):
            or1 + "z"
            for j in range(2*self.rayon+1):
                or1 + "x"
                vertices.append(deepcopy(or1.vertex))
            or1.vertex[0] = -1*self.rayon -1
        #gen des edges,ceux du dessus

        for i in range((2*self.rayon+1)*(2*self.rayon+1)-(2*self.rayon+1)):
            edges.append((i,i+2*self.rayon+1))
        #gen des edges, ceux de coté

        for i in range((2 * self.rayon + 1) * (2 * self.rayon + 1)):
            if (i+1)%(2*self.rayon+1)==0:
                pass
            else:
                edges.append((i,i+1))

        return vertices, edges


class Grille_opti:
    def __init__(self, rayon, centre=[0,0,0]):
        self.origine = Vertex(*centre)
        self.rayon = rayon
        self.vertices = self.gen()[0]
        self.edges = self.gen()[1]

    def gen(self):
        vertices = []
        edges = []
        origine = deepcopy(self.origine)
        origine = origine - ("x" + str(self.rayon)) - ("z" + str(self.rayon))
        for i in range(2*self.rayon +1 ):
            vertices.append((deepcopy(origine) + ("x" + str(i))).vertex)
            vertices.append((deepcopy(origine) + ("x" + str(i)) + ("z" + str(2*self.rayon))).vertex)
        for i in range(len(vertices)):
            if i%2 == 0:
                edges.append((i, i+1))
        n = len(vertices)
        for i in range(2*self.rayon + 1):
            vertices.append((deepcopy(origine) + ("z" + str(i))).vertex)
            vertices.append((deepcopy(origine) + ("z" + str(i)) + ("x" + str(2*self.rayon))).vertex)
        for i in range(n, len(vertices)):
            if i % 2 == 0:
                edges.append((i, i+1))

        return vertices, edges
