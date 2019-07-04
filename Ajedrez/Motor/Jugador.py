import copy
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


    def depurarJugadas(self,tablero):

        for pieza in self.piezas:
            if not pieza is None:
                if pieza.tipo == "Rey":
                    rey = pieza

        for pieza in self.piezas:

            if pieza.activo:

                movimientosNoValidos = []

                for movimiento in pieza.movimientosDisponibles:

                    resultadoRegistro = self.simularMovimiento(pieza,movimiento)

                    for piezaContraria in tablero.piezas:
                        if not piezaContraria is None:
                            if piezaContraria.color == -self.color:
                                if piezaContraria.activo:
                                    self.buscarJugadasPieza(piezaContraria,tablero,resultadoRegistro)

                                    for movimientoContrario in piezaContraria.movimientosDisponibles:
                                        if movimientoContrario == [rey.fila,rey.columna]:

                                            movimientosNoValidos.append(movimientoContrario)

                for movimiento in movimientosNoValidos:
                    pieza.movimientosDisponibles.remove(movimiento)


    def simularMovimiento(self,pieza,movimiento):

        return "Cadena"


    def buscarJugadas(self,tablero,registro):

        #Buscamos movimientos para cada pieza
        for pieza in self.piezas:

            if not pieza is None:

                self.buscarJugadasPieza(pieza,tablero,registro)

        #self.depurarJugadas(tablero)


    def buscarJugadasPieza(self,pieza,tablero,registro):

        pieza.movimientosDisponibles.clear()

        if pieza.activo:

            if pieza.tipo == "Rey":

                if pieza.movimientosRealizados == 0:

                    torre = tablero.casillas[int(3.5 * (-pieza.color) + 4.5 - 1)][8 - 1].pieza

                    if not torre is None:

                        if torre.movimientosRealizados == 0:
                            if (tablero.casillas[int(3.5 * (-pieza.color) + 4.5 - 1)][7 - 1].pieza is None) and \
                            (tablero.casillas[int(3.5 * (-pieza.color) + 4.5 - 1)][6 - 1].pieza is None):
                                pieza.movimientosDisponibles.append(
                                [int(3.5 * (-pieza.color) + 4.5), 7])

                    torre = tablero.casillas[int(3.5 * (-pieza.color) + 4.5 - 1)][1 - 1].pieza

                    if not torre is None:

                        if torre.movimientosRealizados == 0:
                            if (tablero.casillas[int(3.5 * (-pieza.color) + 4.5 - 1)][2 - 1].pieza is None) and \
                            (tablero.casillas[int(3.5 * (-pieza.color) + 4.5 - 1)][3 - 1].pieza is None) and \
                            (tablero.casillas[int(3.5 * (-pieza.color) + 4.5 - 1)][4 - 1].pieza is None):
                                pieza.movimientosDisponibles.append(
                                [int(3.5 * (-pieza.color) + 4.5), 3])


            if pieza.tipo == "Peón":

                if pieza.fila in [1, 8]:
                    pass

                else:
                    # Comer a la derecha
                    if pieza.columna < 8:

                        if tablero.casillas[(pieza.fila + pieza.color) - 1] \
                                [(pieza.columna + 1) - 1].ocupada() == -pieza.color:
                            if [pieza.fila + pieza.color, pieza.columna + 1] \
                                    not in pieza.movimientosDisponibles:
                                pieza.movimientosDisponibles.append(
                                    [pieza.fila + pieza.color, pieza.columna + 1])

                        #AlPaso
                        if pieza.fila == int(0.5 * pieza.color + 4.5):
                            if registro[len(registro) - 1] == "P" + \
                                tablero.casillas[(int(2.5 * pieza.color + 4.5)) - 1] \
                                [(pieza.columna + 1) - 1].__str__() + \
                                tablero.casillas[(int(0.5 * pieza.color + 4.5)) - 1] \
                                [(pieza.columna + 1) - 1].__str__():
                                    pieza.movimientosDisponibles.append(
                                    [int(1.5 * pieza.color + 4.5), pieza.columna + 1])

                    #Comer a la izquierda
                    if pieza.columna > 1:

                        if tablero.casillas[(pieza.fila + pieza.color) - 1] \
                                [(pieza.columna - 1) - 1].ocupada() == -pieza.color:
                            if [pieza.fila + pieza.color, pieza.columna - 1] \
                                    not in pieza.movimientosDisponibles:
                                pieza.movimientosDisponibles.append(
                                    [pieza.fila + pieza.color, pieza.columna - 1])

                        # AlPaso
                        if pieza.fila == int(0.5 * pieza.color + 4.5):
                            if registro[len(registro) - 1] == "P" + \
                                tablero.casillas[(int(2.5 * pieza.color + 4.5)) - 1] \
                                [(pieza.columna - 1) - 1].__str__() + \
                                tablero.casillas[(int(0.5 * pieza.color + 4.5)) - 1] \
                                [(pieza.columna - 1) - 1].__str__():
                                    pieza.movimientosDisponibles.append(
                                    [int(1.5 * pieza.color + 4.5), pieza.columna - 1])


            for direccion in pieza.movimiento:

                for movimiento in direccion:

                    if ((pieza.fila + movimiento[0]) in range(1, 9)) \
                            and ((pieza.columna + movimiento[1]) in range(1, 9)):

                        casillaDestino = tablero.casillas[pieza.fila + movimiento[0] - 1] \
                            [pieza.columna + movimiento[1] - 1]

                        if pieza.tipo == "Peón":

                            if pieza.fila in [1, 8]:
                                continue
                            else:
                                if casillaDestino.ocupada() == 0:
                                    if movimiento == [2 * pieza.color, 0] and pieza.movimientosRealizados > 0:
                                        continue
                                    else:
                                        pieza.movimientosDisponibles.append(
                                            [pieza.fila + movimiento[0], pieza.columna + movimiento[1]])
                                else:
                                    break

                        elif pieza.tipo in ["Alfil", "Torre", "Dama"]:

                            if casillaDestino.ocupada() == pieza.color:
                                break
                            elif casillaDestino.ocupada() == -pieza.color:
                                pieza.movimientosDisponibles.append(
                                    [pieza.fila + movimiento[0], pieza.columna + movimiento[1]])
                                break
                            else:
                                pieza.movimientosDisponibles.append(
                                    [pieza.fila + movimiento[0], pieza.columna + movimiento[1]])

                        else:

                            if not casillaDestino.ocupada() == pieza.color:
                                pieza.movimientosDisponibles.append(
                                    [pieza.fila + movimiento[0], pieza.columna + movimiento[1]])


    def mover(self,jugada,tablero,tipoJugada):

        print(tipoJugada)

        #Formato: Lista con dos listas, entrada y destino;
        #con una fila y una columna

        # Pieza a mover
        pieza = tablero.casillas[jugada[0][0] - 1][jugada[0][1] - 1].pieza
        # Se vacía la casilla de origen
        tablero.casillas[jugada[0][0] - 1][jugada[0][1] - 1].pieza = None
        # Cambio de coordenadas en la pieza
        pieza.mover(jugada[1][0], jugada[1][1])

        if tipoJugada == "Comer":
            #Comer
            pieza.comer(tablero.casillas[jugada[1][0] - 1][jugada[1][1] - 1].pieza)

        elif tipoJugada == "Mover":
            pass

        elif tipoJugada == "AlPaso":
            # Comer al paso
            pieza.comer(tablero.casillas[jugada[1][0] - pieza.color - 1][jugada[1][1] - 1].pieza)
            tablero.casillas[jugada[1][0] - pieza.color - 1][jugada[1][1] - 1].pieza = None

        elif tipoJugada == "EnrroqueCorto":
            #Copia de la torre
            torre = Torre(int(3.5 * (-pieza.color) + 4.5), 8 - 1,self.color)
            #Se mueve la torre
            torre.mover(int(3.5 * (-pieza.color) + 4.5),6)
            #Se borra la torre de la casilla de origen
            self.piezas.remove(tablero.casillas[int(3.5 * (-pieza.color) + 4.5 - 1)][8 - 1].pieza)
            tablero.casillas[int(3.5 * (-pieza.color) + 4.5 - 1)][8 - 1].pieza = None
            #Se coloca en su nueva casilla
            tablero.casillas[int(3.5 * (-pieza.color) + 4.5 - 1)][6 - 1].pieza = torre
            self.piezas.append(torre)

        elif tipoJugada == "EnrroqueLargo":
            # Copia de la torre
            torre = Torre(int(3.5 * (-pieza.color) + 4.5),1 - 1,self.color)
            # Se mueve la torre
            torre.mover(int(3.5 * (-pieza.color) + 4.5), 4)
            # Se borra la torre de la casilla de origen
            self.piezas.remove(tablero.casillas[int(3.5 * (-pieza.color) + 4.5 - 1)][1 - 1].pieza)
            tablero.casillas[int(3.5 * (-pieza.color) + 4.5 - 1)][1 - 1].pieza = None
            # Se coloca en su nueva casilla
            tablero.casillas[int(3.5 * (-pieza.color) + 4.5 - 1)][4 - 1].pieza = torre
            self.piezas.append(torre)

        # Actualización de la casilla
        tablero.casillas[jugada[1][0] - 1][jugada[1][1] - 1].pieza = pieza