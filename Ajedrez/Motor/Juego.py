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
                    self.tablero.casillas[pieza.fila][pieza.columna].pieza = pieza


    def iniciarTurno(self):

            self.set_turno()
            if self.turno == 0:
                self.set_piezas()
            self.jugadores[self.turno % 2].buscarJugadas(
                self.tablero, self.registro,self.jugadores[(self.turno + 1) % 2].piezas)
            self.jugadores[self.turno % 2].depurarJugadas(
                self.tablero, self.registro, self.jugadores[(self.turno + 1) % 2].piezas)


    def desarrollarTurno(self,jugada):

        tipoJugada = self.jugadores[self.turno % 2].anotarRegistro(
            jugada, self.tablero, self.registro)

        self.jugadores[self.turno % 2].mover(
            jugada, self.tablero, tipoJugada, self.registro)


    def terminarTurno(self):

        self.jugadores[self.turno % 2].promocionarse(self.tablero, self.registro)

        return self.jugadores[self.turno % 2].buscarJaque(
            self.tablero, self.registro, self.jugadores[(self.turno + 1) % 2].piezas)