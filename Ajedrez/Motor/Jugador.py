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

        self.movimientosDisponibles = 100

        self.rey = self.piezas[12]

    def __str__(self):
        if self.color == 1:
            return "Jugador Blanco"
        else:
            return "Jugador Negro"


    def buscarJugadas(self,tablero,registro,piezasContrarias):

        #Buscamos movimientos para cada pieza
        for pieza in self.piezas:

            if not pieza is None:

                self.buscarJugadasPieza(pieza,tablero,registro)


    def buscarJugadasPieza(self, pieza, tablero, registro):

        pieza.movimientosDisponibles.clear()

        if pieza.activo:

            if pieza.tipo == "Rey":

                if pieza.movimientosRealizados == 0:

                    torre = tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][8].pieza

                    if not (torre is None):

                        if torre.movimientosRealizados == 0:
                            if (tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][7].pieza is None) and \
                            (tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][6].pieza is None):
                                #Enrroque Corto
                                pieza.movimientosDisponibles.append(
                                [int(3.5 * (-pieza.color) + 4.5), 7])

                    torre = tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][1].pieza

                    if not (torre is None):

                        if torre.movimientosRealizados == 0:
                            if (tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][2].pieza is None) and \
                            (tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][3].pieza is None) and \
                            (tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][4].pieza is None):
                                # Enrroque Largo
                                pieza.movimientosDisponibles.append(
                                [int(3.5 * (-pieza.color) + 4.5), 3])


            if pieza.tipo == "Peón":

                if pieza.fila in [1, 8]:
                    pass

                else:
                    # Comer a la derecha
                    if pieza.columna < 8:

                        if tablero.casillas[(pieza.fila + pieza.color)] \
                                [(pieza.columna + 1)].ocupada() == -pieza.color:
                            if [pieza.fila + pieza.color, pieza.columna + 1] \
                                    not in pieza.movimientosDisponibles:
                                pieza.movimientosDisponibles.append(
                                    [pieza.fila + pieza.color, pieza.columna + 1])

                        #AlPaso
                        if pieza.fila == int(0.5 * pieza.color + 4.5):
                            if registro[len(registro) - 1] == "P" + \
                                tablero.casillas[(int(2.5 * pieza.color + 4.5))] \
                                [(pieza.columna + 1)].__str__() + \
                                tablero.casillas[(int(0.5 * pieza.color + 4.5))] \
                                [(pieza.columna + 1)].__str__():
                                    pieza.movimientosDisponibles.append(
                                    [int(1.5 * pieza.color + 4.5), pieza.columna + 1])

                    #Comer a la izquierda
                    if pieza.columna > 1:

                        if tablero.casillas[(pieza.fila + pieza.color)] \
                                [(pieza.columna - 1)].ocupada() == -pieza.color:
                            if [pieza.fila + pieza.color, pieza.columna] \
                                    not in pieza.movimientosDisponibles:
                                pieza.movimientosDisponibles.append(
                                    [pieza.fila + pieza.color, pieza.columna - 1])

                        # AlPaso
                        if pieza.fila == int(0.5 * pieza.color + 4.5):
                            if registro[len(registro) - 1] == "P" + \
                                tablero.casillas[(int(2.5 * pieza.color + 4.5))] \
                                [(pieza.columna - 1)].__str__() + \
                                tablero.casillas[(int(0.5 * pieza.color + 4.5))] \
                                [(pieza.columna - 1)].__str__():
                                    pieza.movimientosDisponibles.append(
                                    [int(1.5 * pieza.color + 4.5), pieza.columna - 1])


            for direccion in pieza.movimiento:

                for movimiento in direccion:

                    if ((pieza.fila + movimiento[0]) in range(1, 9)) \
                            and ((pieza.columna + movimiento[1]) in range(1, 9)):

                        casillaDestino = tablero.casillas[pieza.fila + movimiento[0]] \
                            [pieza.columna + movimiento[1]]

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


    def depurarJugadas(self, tablero, registro, piezasContrarias):

        for piezaContraria in piezasContrarias:
            if not piezaContraria is None:
                if piezaContraria.activo:
                    self.buscarJugadasPieza(
                        piezaContraria, tablero, registro)

                    for movimientoContrario in piezaContraria.movimientosDisponibles:
                        if movimientoContrario in [[int(3.5 * (-self.color) + 4.5), 5],
                                                   [int(3.5 * (-self.color) + 4.5), 4]]:
                            if [int(3.5 * (-self.color) + 4.5), 3] in self.rey.movimientosDisponibles:
                                self.rey.movimientosDisponibles.remove(
                                [int(3.5 * (-self.color) + 4.5), 3])
                        if movimientoContrario in [[int(3.5 * (-self.color) + 4.5), 5],
                                                   [int(3.5 * (-self.color) + 4.5), 6]]:
                            if [int(3.5 * (-self.color) + 4.5), 7] in self.rey.movimientosDisponibles:
                                self.rey.movimientosDisponibles.remove(
                                [int(3.5 * (-self.color) + 4.5), 7])

        for pieza in self.piezas:

            if pieza.activo:

                movimientosNoValidos = []

                for movimiento in pieza.movimientosDisponibles:

                    ############################################
                    jugada, tipoJugada = self.simularMovimiento(
                        pieza,movimiento,tablero,registro)

                    for piezaContraria in piezasContrarias:
                        if not piezaContraria is None:
                            if piezaContraria.activo:
                                self.buscarJugadasPieza(
                                    piezaContraria,tablero,registro)

                                for movimientoContrario in piezaContraria.movimientosDisponibles:
                                    if movimientoContrario == [self.rey.fila,self.rey.columna]:

                                        movimientosNoValidos.append(movimiento)

                    self.deshacerMovimiento(jugada, tipoJugada,
                        tablero, registro, piezasContrarias)

                for movimiento in movimientosNoValidos:
                    if movimiento in pieza.movimientosDisponibles:
                        pieza.movimientosDisponibles.remove(movimiento)

        #Actualizar el contador de movimientos totales disponibles
        self.movimientosDisponibles = 0
        for pieza in self.piezas:
            if pieza.activo:
                for movimiento in pieza.movimientosDisponibles:
                    self.movimientosDisponibles += 1


    def anotarRegistro(self, jugada, tablero, registro):
        #Formato de la jugada:
        #Lista con dos listas
        #Coordenadas de la casilla de origen
        #Coordenadas de la casilla de destino

        tipoJugada = "Ninguna"

        casillaOrigen = tablero.casillas[jugada[0][0]][jugada[0][1]]
        casillaDestino = tablero.casillas[jugada[1][0]][jugada[1][1]]

        if casillaOrigen.pieza.tipo  == "Rey":

            if casillaOrigen.pieza.movimientosRealizados == 0:

                if jugada[1] == [int(3.5 * (-casillaOrigen.pieza.color) + 4.5), 7]:
                    registro.append("O-O")
                    return "EnrroqueCorto"

                if jugada[1] == [int(3.5 * (-casillaOrigen.pieza.color) + 4.5), 3]:
                    registro.append("O-O-O")
                    return "EnrroqueLargo"


        if casillaOrigen.pieza.tipo == "Peón":

            if casillaOrigen.fila == int(0.5 * casillaOrigen.pieza.color + 4.5):

                if casillaOrigen.columna < 8:

                    if jugada[1] == [int(1.5 * casillaOrigen.pieza.color + 4.5),
                        casillaOrigen.pieza.columna + 1]:

                        jugadaRealizada = casillaOrigen.pieza.tipo[0] + casillaOrigen.__str__() + "x" + \
                                          casillaDestino.__str__()

                        registro.append(jugadaRealizada)
                        return "AlPaso"

                if casillaOrigen.columna > 1:

                    if jugada[1] == [int(1.5 * casillaOrigen.pieza.color + 4.5),
                        casillaOrigen.pieza.columna -1]:

                        jugadaRealizada = casillaOrigen.pieza.tipo[0] + casillaOrigen.__str__() + "x" + \
                                      casillaDestino.__str__()

                        registro.append(jugadaRealizada)
                        return "AlPaso"


        if casillaDestino.pieza is None:

            jugadaRealizada = casillaOrigen.pieza.tipo[0] + casillaOrigen.__str__() + \
                            casillaDestino.__str__()

            tipoJugada = "Mover"

        else:

            jugadaRealizada = casillaOrigen.pieza.tipo[0] + casillaOrigen.__str__() + "x" + \
                              casillaDestino.pieza.tipo[0] + casillaDestino.__str__()

            tipoJugada = "Comer"

        registro.append(jugadaRealizada)

        return tipoJugada


    def simularMovimiento(self, pieza, movimiento, tablero, registro):

        jugada = [[pieza.fila,pieza.columna], movimiento]

        tipoJugada = self.anotarRegistro(jugada, tablero, registro)

        #######################################
        self.mover(jugada, tablero, tipoJugada,registro)

        return jugada, tipoJugada


    def deshacerMovimiento(self, jugada, tipoJugada, tablero, registro, piezasContrarias):

        # Pieza de la casilla de destino
        pieza = tablero.casillas[jugada[1][0]][jugada[1][1]].pieza
        # Se vacía la casilla de destino
        tablero.casillas[jugada[1][0]][jugada[1][1]].pieza = None
        # Cambio de coordenadas en la pieza a las originales
        pieza.mover(jugada[0][0], jugada[0][1])
        pieza.movimientosRealizados -= 2

        if tipoJugada == "Comer":
            # Deshacer comer
            for piezaContraria in piezasContrarias:
                if not (piezaContraria is None):
                    if not piezaContraria.activo:
                        if [ - piezaContraria.fila - 100 * len(registro),
                             - piezaContraria.columna - 100* len(registro)] == \
                            [jugada[1][0], jugada[1][1]]:
                            pieza.comer(piezaContraria,len(registro))
                            tablero.casillas[jugada[1][0]][jugada[1][1]].pieza = piezaContraria

        elif tipoJugada == "Mover":
            pass

        elif tipoJugada == "AlPaso":
            # Deshacer comer al paso
            for piezaContraria in piezasContrarias:
                if not (piezaContraria is None):
                    if not piezaContraria.activo:
                        if [- piezaContraria.fila - 100 * len(registro),
                            - piezaContraria.columna - 100 * len(registro)] == \
                            [jugada[1][0] - pieza.color, jugada[1][1]]:
                            pieza.comer(piezaContraria,len(registro))
                            tablero.casillas[jugada[1][0] - pieza.color][jugada[1][1]].pieza = piezaContraria

        elif tipoJugada == "EnrroqueCorto":
            # Torre a mover
            torre = tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][6].pieza
            # Se vacía su casilla de origen
            tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][6].pieza = None
            # Se mueve la torre
            torre.mover(int(3.5 * (-pieza.color) + 4.5), 8)
            torre.movimientosRealizados -= 1
            # Se coloca en su nueva casilla
            tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][8].pieza = torre

        elif tipoJugada == "EnrroqueLargo":
            # Torre a mover
            torre = tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][4].pieza
            # Se vacía su casilla de origen
            tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][4].pieza = None
            # Se mueve la torre
            torre.mover(int(3.5 * (-pieza.color) + 4.5), 1)
            torre.movimientosRealizados -= 1
            # Se coloca en su nueva casilla
            tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][1].pieza = torre


        # Actualización de la casilla de origen
        tablero.casillas[jugada[0][0]][jugada[0][1]].pieza = pieza
        registro.pop(len(registro) - 1)


    def mover(self, jugada, tablero, tipoJugada, registro):

        #Formato: Lista con dos listas, entrada y destino;
        #con una fila y una columna

        # Pieza a mover
        pieza = tablero.casillas[jugada[0][0]][jugada[0][1]].pieza
        # Se vacía la casilla de origen
        tablero.casillas[jugada[0][0]][jugada[0][1]].pieza = None
        # Cambio de coordenadas en la pieza
        pieza.mover(jugada[1][0], jugada[1][1])

        if tipoJugada == "Comer":
            #Comer
            pieza.comer(tablero.casillas[jugada[1][0]][jugada[1][1]].pieza,len(registro))
            tablero.casillas[jugada[1][0]][jugada[1][1]].pieza = None

        elif tipoJugada == "Mover":
            pass

        elif tipoJugada == "AlPaso":
            # Comer al paso
            pieza.comer(tablero.casillas[jugada[1][0] - pieza.color][jugada[1][1]].pieza,len(registro))
            tablero.casillas[jugada[1][0] - pieza.color][jugada[1][1]].pieza = None

        elif tipoJugada == "EnrroqueCorto":
            #Torre a mover
            torre = tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][8].pieza
            # Se vacía su casilla de origen
            tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][8].pieza = None
            #Se mueve la torre
            torre.mover(int(3.5 * (-pieza.color) + 4.5),6)
            torre.movimientosRealizados -= 1
            #Se coloca en su nueva casilla
            tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][6].pieza = torre

        elif tipoJugada == "EnrroqueLargo":
            # Torre a mover
            torre = tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][1].pieza
            # Se vacía su casilla de origen
            tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][1].pieza = None
            # Se mueve la torre
            torre.mover(int(3.5 * (-pieza.color) + 4.5), 4)
            torre.movimientosRealizados -= 1
            # Se coloca en su nueva casilla
            tablero.casillas[int(3.5 * (-pieza.color) + 4.5)][4].pieza = torre


        # Actualización de la casilla
        tablero.casillas[jugada[1][0]][jugada[1][1]].pieza = pieza


    def promocionarse(self, tablero, registro):

        for casilla in tablero.casillas[int(3.5 * self.color + 4.5 )]:
            if not (casilla.pieza is None):
                if casilla.pieza.tipo == "Peón":
                    self.piezas.remove(casilla.pieza)
                    casilla.pieza = None
                    nuevaPieza = Dama(casilla.fila, casilla.columna, self.color)
                    casilla.pieza = nuevaPieza
                    self.piezas.append(nuevaPieza)



    def buscarJaque(self,tablero,registro,piezasContrarias):

        self.buscarJugadas(tablero, registro, piezasContrarias)

        for piezaContraria in piezasContrarias:
            if not (piezaContraria is None):
                if piezaContraria.tipo == "Rey":
                    rey = piezaContraria

        for pieza in self.piezas:
            for movimiento in pieza.movimientosDisponibles:
                if movimiento == [rey.fila,rey.columna]:
                    return True

        return False
