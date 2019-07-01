import pygame
import sys

sys.path.append("..")

from Interfaz import Archivos
from Interfaz import Opciones

#Pieza Pieza Pieza Pieza Pieza Pieza Pieza Pieza


class Pieza:


    def __init__(self, fila, columna,color):

        self.fila = fila
        self.columna = columna
        # Blanco = 1; Negro = -1
        self.color = color
        self.activo = True
        self.movimientos = 0
        self.movimientosDisponibles = []

        pygame.sprite.Sprite.__init__(self)


    def mover(self, nuevaFila, nuevaColumna):

        self.fila = nuevaFila
        self.columna = nuevaColumna
        self.movimientos += 1


    def comer(self, nuevaFila, nuevaColumna, Pieza):

        Pieza.activo = False
        self.mover(nuevaFila, nuevaColumna)


    def buscarMovimientos(self,listaMovimientos):

        self.movimientosDisponibles.clear()

        for direccion in listaMovimientos:
            self.movimientosDisponibles.append([self.fila + direccion[0], self.columna + direccion[1]])

        self.depurarMovimientos()


    def depurarMovimientos(self):

        #Eliminar movimientos que se salgan del tablero
        movimientosValidos = []

        for movimiento in self.movimientosDisponibles:

            if movimiento[0] in range(1,9) and movimiento[1] in range(1,9):
                if not movimiento == [self.fila, self.columna]:
                    movimientosValidos.append(movimiento)

        self.movimientosDisponibles = movimientosValidos



#Peón Peón Peón Peón Peón Peón Peón Peón


class Peon(Pieza):


    def __init__(self, fila, columna, color):
        super().__init__(fila, columna, color)

        self.imagen = pygame.image.load(
        Archivos.OpcionesPiezas[
        Opciones.ColorPiezas[
        ((-1)*(self.color-1))//2
        ]][0]).convert_alpha()
        self.imagen = pygame.transform.scale(
        self.imagen, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))
        self.rect = self.imagen.get_rect()


    def buscarMovimientos(self):
        super().buscarMovimientos([[self.color,0]])

        #DoblePaso
        if self.movimientos == 0:
            self.movimientosDisponibles.append([self.fila + 2* self.color, self.columna])



#Caballo Caballo Caballo Caballo Caballo Caballo Caballo Caballo


class Caballo(Pieza):


    def __init__(self, fila, columna, color):
        super().__init__(fila, columna, color)

        self.imagen = pygame.image.load(
        Archivos.OpcionesPiezas[
        Opciones.ColorPiezas[
        ((-1) * (self.color - 1)) // 2
        ]][1]).convert_alpha()
        self.imagen = pygame.transform.scale(
            self.imagen, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))
        self.rect = self.imagen.get_rect()


def buscarMovimientos(self):
        super().buscarMovimientos([[2,-1],[2,1],[-2,-1],[-2,1],[1,-2],[1,2],[-1,-2],[-1,2]])



#Alfil Alfil Alfil Alfil Alfil Alfil Alfil Alfil


class Alfil(Pieza):


    def __init__(self, fila, columna, color):
        super().__init__(fila, columna, color)

        self.imagen = pygame.image.load(
        Archivos.OpcionesPiezas[
        Opciones.ColorPiezas[
        ((-1) * (self.color - 1)) // 2
        ]][3]).convert_alpha()
        self.imagen = pygame.transform.scale(
            self.imagen, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))
        self.rect = self.imagen.get_rect()

    def buscarMovimientos(self):
        super().buscarMovimientos([[paso,paso] for paso in range(-7,8)] +
                                  [[paso,-paso] for paso in range(-7,8)])



#Torre Torre Torre Torre Torre Torre Torre Torre


class Torre(Pieza):


    def __init__(self, fila, columna, color):
        super().__init__(fila, columna, color)

        self.imagen = pygame.image.load(
        Archivos.OpcionesPiezas[
        Opciones.ColorPiezas[
        ((-1) * (self.color - 1)) // 2
        ]][5]).convert_alpha()
        self.imagen = pygame.transform.scale(
            self.imagen, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))
        self.rect = self.imagen.get_rect()

    def buscarMovimientos(self):
        super().buscarMovimientos([[paso, 0] for paso in range(-7, 8)] +
                                  [[0, paso] for paso in range(-7, 8)])



#Dama Dama Dama Dama Dama Dama Dama Dama


class Dama(Pieza):


    def __init__(self, fila, columna, color):
        super().__init__(fila, columna, color)

        self.imagen = pygame.image.load(
        Archivos.OpcionesPiezas[
        Opciones.ColorPiezas[
        ((-1) * (self.color - 1)) // 2
        ]][6]).convert_alpha()
        self.imagen = pygame.transform.scale(
            self.imagen, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))
        self.rect = self.imagen.get_rect()

    def buscarMovimientos(self):
        super().buscarMovimientos([[paso, paso] for paso in range(-7, 8)] +
                                  [[paso, -paso] for paso in range(-7, 8)] +
                                  [[paso, 0] for paso in range(-7, 8)] +
                                  [[0, paso] for paso in range(-7, 8)])



#Rey  Rey  Rey  Rey  Rey  Rey  Rey  Rey


class Rey(Pieza):


    def __init__(self, fila, columna, color):
        super().__init__(fila, columna, color)

        self.imagen = pygame.image.load(
        Archivos.OpcionesPiezas[
        Opciones.ColorPiezas[
        ((-1) * (self.color - 1)) // 2
        ]][7]).convert_alpha()
        self.imagen = pygame.transform.scale(
            self.imagen, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))
        self.rect = self.imagen.get_rect()

    def buscarMovimientos(self):
        super().buscarMovimientos([[1,0],[-1,0],[0,-1],[0,1],[1,-1],[1,1],[-1,-1],[-1,1]])