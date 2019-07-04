from Motor.Tablero import *
from Motor.Jugador import *

class Juego:


    def __init__(self):

        self.jugadores = [Jugador(1),Jugador(-1)]
        self.tablero = Tablero()
        self.turno = -1
        self.set_piezas()
        self.registro = []

        Seleccion = pygame.image.load(Archivos.Seleccion).convert_alpha()
        self.seleccion = pygame.transform.scale(Seleccion, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))

        JugadasValidas = pygame.image.load(Archivos.JugadasValidas).convert_alpha()
        self.jugadasValidas = pygame.transform.scale(JugadasValidas, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))

        Jaque = pygame.image.load(Archivos.Jaque).convert_alpha()
        self.jaque = pygame.transform.scale(Jaque, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))

        self.fondoPantalla = pygame.Surface((Opciones.SangriaIzq + Opciones.SangriaDer + Opciones.TamanoTablero,
                                        Opciones.SangriaSup + Opciones.SangriaInf + Opciones.TamanoTablero))

        self.fondoPantalla.fill(Opciones.FondoPantalla)

    def set_turno(self):
        self.turno += 1

    def set_piezas(self):

        for fila in self.tablero.casillas:
            for casilla in fila:
                casilla.pieza = None

        for jugador in self.jugadores:
            for pieza in jugador.piezas:
                if pieza.activo:
                    self.tablero.casillas[pieza.fila - 1][pieza.columna - 1].pieza = pieza


    def set_registro(self,jugada):
        #Formato de la jugada:
        #Lista con dos listas
        #Coordenadas de la casilla de origen
        #Coordenadas de la casilla de destino

        tipoJugada = "Ninguna"

        casillaOrigen = self.tablero.casillas[jugada[0][0] - 1][jugada[0][1] - 1]
        casillaDestino = self.tablero.casillas[jugada[1][0] - 1][jugada[1][1] - 1]

        if casillaOrigen.pieza.tipo == "Rey":

            if jugada[1] == [int(3.5 * (-casillaOrigen.pieza.color) + 4.5), 7]:
                self.registro.append("O-O")
                return "EnrroqueCorto"

            if jugada[1] == [int(3.5 * (-casillaOrigen.pieza.color) + 4.5), 3]:
                self.registro.append("O-O-O")
                return "EnrroqueLargo"



        if casillaOrigen.pieza.tipo == "Peón":

            if casillaOrigen.fila == int(0.5 * casillaOrigen.pieza.color + 4.5):

                if casillaOrigen.columna < 8:

                    if jugada[1] == [int(1.5 * casillaOrigen.pieza.color + 4.5),
                        casillaOrigen.pieza.columna + 1]:

                        jugadaRealizada = casillaOrigen.pieza.tipo[0] + casillaOrigen.__str__() + "x" + \
                                          casillaDestino.__str__()

                        self.registro.append(jugadaRealizada)
                        return "AlPaso"

                if casillaOrigen.columna > 1:

                    if jugada[1] == [int(1.5 * casillaOrigen.pieza.color + 4.5),
                        casillaOrigen.pieza.columna -1]:

                        jugadaRealizada = casillaOrigen.pieza.tipo[0] + casillaOrigen.__str__() + "x" + \
                                      casillaDestino.__str__()

                        self.registro.append(jugadaRealizada)
                        return "AlPaso"

        if casillaDestino.pieza is None:

            jugadaRealizada = casillaOrigen.pieza.tipo[0] + casillaOrigen.__str__() + \
                            casillaDestino.__str__()

            tipoJugada = "Mover"

        else:

            jugadaRealizada = casillaOrigen.pieza.tipo[0] + casillaOrigen.__str__() + "x" + \
                              casillaDestino.pieza.tipo[0] + casillaDestino.__str__()

            tipoJugada = "Comer"

        self.registro.append(jugadaRealizada)

        return tipoJugada


    def iniciarTurno(self):

            self.set_turno()
            self.jugadores[self.turno % 2].buscarJugadas(self.tablero, self.registro)