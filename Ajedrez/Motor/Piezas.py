import sys
sys.path.append("..")

from Interfaz import Archivos
from Interfaz import Opciones

import pygame


#Pieza Pieza Pieza Pieza Pieza Pieza Pieza Pieza


class Pieza:


    def __init__(self, fila, columna,color):

        self.tipo = "Pieza"
        self.fila = fila
        self.columna = columna

        # Blanco = 1; Negro = -1
        self.color = color
        self.activo = True

        #Lista inicial con los movimientos máximos posibles
        #para la pieza
        #Cada elemento es una dirección posible
        #Cada dirección es una lista con movimientos posibles
        #Cada movimiento es de la forma [incrementoFila,incrementoColumna]
        self.movimiento = []

        #Movimientos válidos para la posición actual
        self.movimientosDisponibles = []

        self.movimientosRealizados = 0

        pygame.sprite.Sprite.__init__(self)


    def mover(self, nuevaFila, nuevaColumna):

        self.fila = nuevaFila
        self.columna = nuevaColumna

        self.movimientosRealizados += 1


    def comer(self, pieza):

        if pieza is None:
            pass

        else:
            pieza.activo = False

            pieza.fila = -100
            pieza.columna = -100

    def set_movimientos(self,listaMovimientos):

        self.movimientosDisponibles.clear()

        if self.activo:
            for direccion in listaMovimientos:
                self.movimientosDisponibles.append([self.fila + direccion[0], self.columna + direccion[1]])


    def __str__(self):

        cadena = "OABCDEFGH"
        color = [" Blanco "," Negro "]
        return self.tipo + color[(1 - self.color) // 2] + cadena[self.columna] + str(self.fila)


#Peón Peón Peón Peón Peón Peón Peón Peón


class Peon(Pieza):


    def __init__(self, fila, columna, color):
        super().__init__(fila, columna, color)

        self.tipo = "Peón"

        self.movimiento = [
            [[self.color,0],[2 * self.color, 0]]
        ]

        self.imagen = pygame.image.load(
        Archivos.OpcionesPiezas[
        Opciones.ColorPiezas[
        (1 - self.color)//2
        ]][0]).convert_alpha()
        self.imagen = pygame.transform.scale(
        self.imagen, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))
        self.rect = self.imagen.get_rect()


    def set_movimientos(self):
        super().set_movimientos([[self.color,0]])

        #DoblePaso
        if self.movimientosRealizados == 0:
            self.movimientosDisponibles.append([self.fila + 2* self.color, self.columna])



#Caballo Caballo Caballo Caballo Caballo Caballo Caballo Caballo


class Caballo(Pieza):


    def __init__(self, fila, columna, color):
        super().__init__(fila, columna, color)

        self.tipo = "Caballo"

        self.movimiento = [
            [[2,-1]],
            [[2,1]],
            [[-2,-1]],
            [[-2,1]],
            [[1,-2]],
            [[1,2]],
            [[-1,-2]],
            [[-1,2]]
        ]

        self.imagen = pygame.image.load(
        Archivos.OpcionesPiezas[
        Opciones.ColorPiezas[
        (1 - self.color) // 2
        ]][1]).convert_alpha()
        self.imagen = pygame.transform.scale(
            self.imagen, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))
        self.rect = self.imagen.get_rect()


    def set_movimientos(self):
        super().set_movimientos([[2,-1],[2,1],[-2,-1],[-2,1],[1,-2],[1,2],[-1,-2],[-1,2]])



#Alfil Alfil Alfil Alfil Alfil Alfil Alfil Alfil


class Alfil(Pieza):


    def __init__(self, fila, columna, color):
        super().__init__(fila, columna, color)

        self.tipo = "Alfil"

        #ArribaDerecha
        self.movimiento.append([[paso,paso] for paso in range(1,8)])
        #AbajoIzquierda
        self.movimiento.append([[paso, paso] for paso in range(-1, -8,-1)])
        #ArribaIzquierda
        self.movimiento.append([[paso,-paso] for paso in range(1,8)])
        #AbajoDerecha
        self.movimiento.append([[paso, -paso] for paso in range(-1, -8,-1)])

        self.imagen = pygame.image.load(
        Archivos.OpcionesPiezas[
        Opciones.ColorPiezas[
        (1 - self.color) // 2
        ]][3]).convert_alpha()

        self.imagen = pygame.transform.scale(
            self.imagen, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))
        self.rect = self.imagen.get_rect()

    def set_movimientos(self):
        super().set_movimientos([[paso,paso] for paso in range(-7,8)] +
                                  [[paso,-paso] for paso in range(-7,8)])



#Torre Torre Torre Torre Torre Torre Torre Torre


class Torre(Pieza):


    def __init__(self, fila, columna, color):
        super().__init__(fila, columna, color)

        self.tipo = "Torre"

        #Arriba
        self.movimiento.append([[paso, 0] for paso in range(1, 8)])
        #Abajo
        self.movimiento.append([[paso, 0] for paso in range(-1, -8, -1)])
        #Derecha
        self.movimiento.append([[0, paso] for paso in range(1, 8)])
        #Izquierda
        self.movimiento.append([[0, paso] for paso in range(-1, -8, -1)])

        self.imagen = pygame.image.load(
        Archivos.OpcionesPiezas[
        Opciones.ColorPiezas[
        (1 - self.color) // 2
        ]][5]).convert_alpha()
        self.imagen = pygame.transform.scale(
            self.imagen, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))
        self.rect = self.imagen.get_rect()

    def set_movimientos(self):
        super().set_movimientos([[paso, 0] for paso in range(-7, 8)] +
                                  [[0, paso] for paso in range(-7, 8)])



#Dama Dama Dama Dama Dama Dama Dama Dama


class Dama(Pieza):


    def __init__(self, fila, columna, color):
        super().__init__(fila, columna, color)

        self.tipo = "Dama"

        # Arriba
        self.movimiento.append([[paso, 0] for paso in range(1, 8)])
        # Abajo
        self.movimiento.append([[paso, 0] for paso in range(-1, -8, -1)])
        # Derecha
        self.movimiento.append([[0, paso] for paso in range(1, 8)])
        # Izquierda
        self.movimiento.append([[0, paso] for paso in range(-1, -8, -1)])
        # ArribaDerecha
        self.movimiento.append([[paso, paso] for paso in range(1, 8)])
        # AbajoIzquierda
        self.movimiento.append([[paso, paso] for paso in range(-1, -8, -1)])
        # ArribaIzquierda
        self.movimiento.append([[paso, -paso] for paso in range(1, 8)])
        # AbajoDerecha
        self.movimiento.append([[paso, -paso] for paso in range(-1, -8, -1)])

        self.imagen = pygame.image.load(
        Archivos.OpcionesPiezas[
        Opciones.ColorPiezas[
        (1 - self.color) // 2
        ]][6]).convert_alpha()
        self.imagen = pygame.transform.scale(
            self.imagen, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))
        self.rect = self.imagen.get_rect()

    def set_movimientos(self):
        super().set_movimientos([[paso, paso] for paso in range(-7, 8)] +
                                  [[paso, -paso] for paso in range(-7, 8)] +
                                  [[paso, 0] for paso in range(-7, 8)] +
                                  [[0, paso] for paso in range(-7, 8)])



#Rey  Rey  Rey  Rey  Rey  Rey  Rey  Rey


class Rey(Pieza):


    def __init__(self, fila, columna, color):
        super().__init__(fila, columna, color)

        self.tipo = "Rey"

        self.movimiento = [
            [[1, 0]],
            [[-1, 0]],
            [[0, -1]],
            [[0, 1]],
            [[1, -1]],
            [[1, 1]],
            [[-1, -1]],
            [[-1, 1]]
        ]

        self.imagen = pygame.image.load(
        Archivos.OpcionesPiezas[
        Opciones.ColorPiezas[
        (1 - self.color) // 2
        ]][7]).convert_alpha()
        self.imagen = pygame.transform.scale(
            self.imagen, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))
        self.rect = self.imagen.get_rect()

    def set_movimientos(self):
        super().set_movimientos([[1,0],[-1,0],[0,-1],[0,1],[1,-1],[1,1],[-1,-1],[-1,1]])