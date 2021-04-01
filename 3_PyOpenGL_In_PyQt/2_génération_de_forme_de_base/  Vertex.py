class Vertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vertex = [x, y, z]

    def __add__(self, other):  # on définit +
        if type(other) == Vertex: # dans le cas ou c'est d'autre coordoné
            coeff = [None, None, None]
            for i in range(len(self.vertex)):
                coeff[i] = self.vertex[i] + other.vertex[i]
            return Vertex(*coeff)
        if type(other) == str:  # dans le cas d'un string
            if other == "x":
                self.vertex[0] += 1

            elif other == "y":
                self.vertex[1] += 1
            elif other == "z":
                self.vertex[2] += 1
            else : # dans le cas d'un multiple de la dimension choisit exemple : "x3" = 3 * x
                if other[0] == "x":
                    self.vertex[0] += int(other[1:])
                if other[0] == "y":
                    self.vertex[1] += int(other[1:])
                if other[0] == "z":
                    self.vertex[2] += int(other[1:])

            return Vertex(*self.vertex)

    def __sub__(self, other):# de même pour -
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
            else :
                if other[0] == "x":
                    self.vertex[0] -= int(other[1:])
                if other[0] == "y":
                    self.vertex[1] -= int(other[1:])
                if other[0] == "z":
                    self.vertex[2] -= int(other[1:])
            return Vertex(*self.vertex)


    def __str__(self): # on définit ce qu'il se passe lorsqu'on print l'objet vertex
        return f"{self.vertex}"

    def __getitem__(self, item):  #on definit ce que renvoit Vertex[integer]
        if type(item) == int:
            return self.vertex[item]

    def __mul__(self, other):#on définit *
        if type(other) == int:
            for i in range(len(self.vertex)):
                self.vertex[i] *= other
