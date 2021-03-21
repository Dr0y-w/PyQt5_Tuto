from copy import deepcopy


class Vertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vertex = [x, y, z]

    def __add__(self, other):
        if type(other) == Vertex:
            coeff = [None, None, None]
            for i in range(len(self.vertex)):
                coeff[i] = self.vertex[i] + other.vertex[i]
            return Vertex(*coeff)
        if type(other) == str:
            if other == "x":
                self.vertex[0] += 1

            elif other == "y":
                self.vertex[1] += 1
            elif other == "z":
                self.vertex[2] += 1

            return Vertex(*self.vertex)

    def __sub__(self,other):
        if type(other) == Vertex:
            coeff = [None, None, None]
            for i in range(len(self.vertex)):
                coeff[i] = self.vertex[i] - other.vertex[i]
            return Vertex(*coeff)
        if type(other) == str:
            if other == "x":
                self.vertex[0] -= 1

            elif other == "y":
                self.vertex[1] -= 1
            elif other == "z":
                self.vertex[2] -= 1

            return Vertex(*self.vertex)


    def __str__(self):
        return f"{self.vertex}"

    def __getitem__(self, item):
        if type(item) == int:
            return self.vertex[item]

    def __mul__(self, other):
        if type(other) == int:
            for i in range(len(self.vertex)):
                self.vertex[i] *= other
        elif type(other) == Vertex:
            for i in range(len(self.vertex)):
                pass


class Cube:
    def __init__(self, origine=[0, 0, 0]):
        self.origine = Vertex(*origine)
        self.vertices = self.gen()[0]
        self.edges = self.gen()[1]

    def gen(self, longueur=1):
        vertices = [
             self.origine.vertex,
             (deepcopy(self.origine) + "x").vertex,
             (deepcopy(self.origine) + "y").vertex,
             (deepcopy(self.origine) + "z").vertex,
             (deepcopy(self.origine) + "x" + "y").vertex,
             (deepcopy(self.origine) + "x" + "y" + "z").vertex,
             (deepcopy(self.origine) + "x" + "z").vertex,
             (deepcopy(self.origine) + "z" + "y").vertex
            ]
        edges = ((0, 1), (0, 2), (0, 3), (1, 4), (1, 6), (2, 7),
                 (4, 5), (5, 6), (3, 6), (5, 7), (2, 4), (3, 7))
        return vertices, edges

class Grid:
    def __init__(self, rayon,origine=[0, 0, 0]):
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
        #gen des vertex
        for i in range(2*self.rayon+1):
            or1 + "z"
            for j in range(2*self.rayon+1):
                or1 + "x"
                vertices.append(deepcopy(or1.vertex))
            or1.vertex[0] = -1*self.rayon -1
        #gen des edeges,ceux du dessus

        for i in range((2*self.rayon+1)*(2*self.rayon+1)-(2*self.rayon+1)):
            edges.append((i,i+2*self.rayon+1))
        #gen des edges, ceux de coté

        for i in range((2 * self.rayon + 1) * (2 * self.rayon + 1)):
            if (i+1)%(2*self.rayon+1)==0:
                pass
            else :
                edges.append((i,i+1))

        return vertices, edges
