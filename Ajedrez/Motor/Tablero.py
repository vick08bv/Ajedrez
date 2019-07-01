class Casilla:

    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.numero = 8 * (fila - 1) + columna
        self.pieza = None

    def __setattr__(self, atributo, valor):
        self.__dict__[atributo] = valor

    def __str__(self):
        cadena = "OABCDEFGH"
        return cadena[self.columna] + str(self.fila)



class Tablero:
    
    def __init__(self):
        self.casillas = list([list([Casilla(i,j) for j in range(1,9)]) for i in range(1,9)])
