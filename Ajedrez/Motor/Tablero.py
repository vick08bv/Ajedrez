import sys
sys.path.append("..")

from Interfaz import Opciones
from Interfaz import Archivos

import pygame

class Casilla:

    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.numero = 8 * (fila - 1) + columna
        self.pieza = None

        pygame.sprite.Sprite.__init__(self)

        self.imagen = pygame.image.load(
        Archivos.OpcionesFondos[
        Opciones.ColorFondo[0]
        ][
        Opciones.ColorFondo[1]
        ][(self.fila % 2) == (self.columna % 2)]).convert()
        self.imagen = pygame.transform.scale(
            self.imagen, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))
        self.rect = self.imagen.get_rect()

    def set_pieza(self,pieza):
        self.pieza = pieza

    def ocupada(self):
        if self.pieza is None:
            return 0
        else:
            return self.pieza.color

    def __str__(self):
        cadena = "OABCDEFGH"
        return cadena[self.columna] + str(self.fila)



class Tablero:
    
    def __init__(self):
        self.casillas = list([list([Casilla(i,j) for j in range(1,9)]) for i in range(1,9)])

    def __str__(self):
        cadena = ""
        for fila in self.casillas:
            for casilla in fila:
                if casilla.pieza is None:
                    cadena += "None " + casilla.__str__() + "\n"
                else:
                    cadena += casilla.pieza.__str__() + "\n"
        return cadena