from Motor.Piezas import *
from Motor.Tablero import *
from Motor.Jugador import *

class Juego:


    def __init__(self):

        self.jugadores = [Jugador(1),Jugador(-1)]
        self.tablero = Tablero()
        self.turno = -1

    def rotarTurno(self):
        self.turno += 1

    def jugar(self):

        while self.turno < 200:
            self.rotarTurno()
            self.jugadores[self.turno % 2].buscarJugadas()



