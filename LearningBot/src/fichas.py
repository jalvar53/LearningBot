class ficha(object):
    color = ""
    jugador = "n"
    score = 0
    def __init__(self,color):
        self.color = color;
    def tostring(self):
        pass

class peon(ficha):
    def type(self):
        if self.jugador == 0:
            return 'p'
        else:
            return 'P'
    movimientos = [1]
    direccion = [8]
    come = []
    def __init__(self, pos, color):
        ficha.__init__(self,color)
        if color == "Blanco":
            self.jugador = 0
            self.come.append(-9)
            self.come.append(-7)
        else:
            self.jugador = 1
            self.come.append(9)
            self.come.append(7)
        self.score = 1
    def tostring(self):
        if (self.color == "Blanco"):
            return u'\u2659'
        else:
            return u'\u265F'

class torre(ficha):
    def type(self):
        if self.jugador == 0:
            return 't'
        else:
            return 'T'
    movimientos = [1,2,3,4,5,6,7,8]
    direccion =[8,-1,-8,1]
    come = direccion
    def __init__(self,color):
        ficha.__init__(self,color)
        if color == "Blanco":
            self.jugador = 0
        else:
            self.jugador = 1
        self.score = 5
    def tostring(self):
        if (self.color == "Blanco"):
            return u'\u2656'
        else:
            return u'\u265C'

class caballo(ficha):
    def type(self):
        if self.jugador == 0:
            return 'c'
        else:
            return 'C'
    movimientos = []
    direccion = []
    come = direccion
    def __init__(self,color):
        ficha.__init__(self,color)
        if color == "Blanco":
            self.jugador = 0
        else:
            self.jugador = 1
        self.score = 3
    def tostring(self):
        if (self.color == "Blanco"):
            return u'\u2658'
        else:
            return u'\u265E'

class alfil(ficha):
    def type(self):
        if self.jugador == 0:
            return 'a'
        else:
            return 'A'
    movimientos = [1,2,3,4,5,6,7,8]
    direccion = [7,-9,-7,9]
    come = direccion
    def __init__(self,color):
        ficha.__init__(self,color)
        if color == "Blanco":
            self.jugador = 0
        else:
            self.jugador = 1
        self.score = 3
    def tostring(self):
        if (self.color == "Blanco"):
            return u'\u2657'
        else:
            return u'\u265D'

class rey(ficha):
    def type(self):
        if self.jugador == 0:
            return 'k'
        else:
            return 'K'
    movimientos = [1]
    direccion = [8,7,-1,-9,-8,-7,1,9]
    come = direccion
    def __init__(self,color):
        ficha.__init__(self,color)
        if color == "Blanco":
            self.jugador = 0
        else:
            self.jugador = 1
    def tostring(self):
        if (self.color == "Blanco"):
            return u'\u2654'
        else:
            return u'\u265A'

class reina(ficha):
    def type(self):
        if self.jugador == 0:
            return 'r'
        else:
            return 'R'
    movimientos = [1,2,3,4,5,6,7,8]
    direccion = [8,7,-1,-9,-8,-7,1,9]
    come = direccion
    def __init__(self,color):
        ficha.__init__(self,color)
        if color == "Blanco":
            self.jugador = 0
        else:
            self.jugador = 1
        self.score = 9
    def tostring(self):
        if (self.color == "Blanco"):
            return u'\u2655'
        else:
            return u'\u265B'

class casilla(ficha):
    def type(self):
        if self.color == "Blanco":
            return 'b'
        else:
            return 'B'
    def __init__(self,color):
        ficha.__init__(self,color)
    def tostring(self):
        if(self.color == "Blanco"):
            return " "
        else:
            return u'\u2588'
