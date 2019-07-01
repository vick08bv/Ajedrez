#Para importar de otras carpetas
#import sys
#sys.path.append("..")

from Motor.Piezas import *


class Jugador:


    def __init__(self,color):

        self.color = color

        filasIniciales = [[7,8],[0,0],[2,1]]

        self.piezas = []

        for columna in range(1,9):
            self.piezas.append(Peon(filasIniciales[color + 1][0],columna, self.color))

        self.piezas.append(Torre(filasIniciales[color + 1][1], 1, self.color))
        self.piezas.append(Caballo(filasIniciales[color + 1][1], 2, self.color))
        self.piezas.append(Alfil(filasIniciales[color + 1][1], 3, self.color))
        self.piezas.append(Dama(filasIniciales[color + 1][1], 4, self.color))
        self.piezas.append(Rey(filasIniciales[color + 1][1], 5, self.color))
        self.piezas.append(Alfil(filasIniciales[color + 1][1], 6, self.color))
        self.piezas.append(Caballo(filasIniciales[color + 1][1], 7, self.color))
        self.piezas.append(Torre(filasIniciales[color + 1][1], 8, self.color))


    def buscarJugadas(self):

        for pieza in self.piezas:
            pieza.buscarMovimientos()
