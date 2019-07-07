import sys
sys.path.append("..")
from Motor.Juego import *
from Interfaz import Opciones
from Interfaz import Archivos
import pygame
from pygame.locals import *


def borrarEventos():
    pygame.event.set_blocked(pygame.ACTIVEEVENT)
    pygame.event.set_blocked(pygame.KEYDOWN)
    pygame.event.set_blocked(pygame.KEYUP)
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
    #pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_blocked(pygame.JOYAXISMOTION)
    pygame.event.set_blocked(pygame.JOYBALLMOTION)
    pygame.event.set_blocked(pygame.JOYHATMOTION)
    pygame.event.set_blocked(pygame.JOYBUTTONUP)
    pygame.event.set_blocked(pygame.JOYBUTTONDOWN)
    pygame.event.set_blocked(pygame.VIDEORESIZE)
    pygame.event.set_blocked(pygame.VIDEOEXPOSE)
    pygame.event.set_blocked(pygame.USEREVENT)


def dibujarPantalla(juego, screen):

    screen.blit(juego.fondoPantalla, (0, 0))

    for fila in juego.tablero.casillas:
        for casilla in fila:
            if not (casilla.fila == 0 or casilla.columna == 0):
                screen.blit(casilla.imagen, (
                    Opciones.SangriaIzq + Opciones.TamanoCuadro * (casilla.columna - 1),
                    Opciones.SangriaSup + Opciones.TamanoCuadro * (8 - casilla.fila)))
                #Dibujado de la pieza que ocupa la casilla
                if casilla.pieza is not None:
                    if casilla.pieza.activo:
                        screen.blit(casilla.pieza.imagen, (
                        Opciones.SangriaIzq + Opciones.TamanoCuadro * (casilla.columna - 1),
                        Opciones.SangriaSup + Opciones.TamanoCuadro * (8 - casilla.fila)))

    pygame.display.flip()


def dibujarMovimiento(juego, screen, jugada):

    #Casilla Origen
    casillaOr = juego.tablero.casillas[jugada[0][0]][jugada[0][1]]
    #CasillaDestino
    casillaDes = juego.tablero.casillas[jugada[1][0]][jugada[1][1]]

    for paso in range(0,Opciones.TamanoCuadro + 1,1):

        pygame.time.wait(5)

        for fila in juego.tablero.casillas:
            for casilla in fila:
                if not (casilla.fila == 0 or casilla.columna == 0):
                    screen.blit(casilla.imagen, (
                        Opciones.SangriaIzq + Opciones.TamanoCuadro * (casilla.columna - 1),
                        Opciones.SangriaSup + Opciones.TamanoCuadro * (8 - casilla.fila)))
                    # Dibujado de la piezas fijas que ocupan las casillas
                    if casilla.pieza is not None:
                        if casilla.pieza.activo:
                            if not casilla.pieza == casillaDes.pieza:
                                screen.blit(casilla.pieza.imagen, (
                                    Opciones.SangriaIzq + Opciones.TamanoCuadro * (casilla.columna - 1),
                                    Opciones.SangriaSup + Opciones.TamanoCuadro * (8 - casilla.fila)))

        screen.blit(casillaDes.pieza.imagen, (
        Opciones.SangriaIzq + Opciones.TamanoCuadro * (casillaOr.columna - 1) + paso * (casillaDes.columna - casillaOr.columna),
        Opciones.SangriaSup + Opciones.TamanoCuadro * (8 - casillaOr.fila) + paso * (casillaOr.fila - casillaDes.fila)))

        pygame.display.flip()

    pygame.display.flip()


def dibujarSeleccion(casillaPresionada,juego,screen):

    CasillaPresionada = juego.tablero.casillas[casillaPresionada[0]] \
                    [casillaPresionada[1]]

    screen.blit(CasillaPresionada.imagen, (
        Opciones.SangriaIzq + Opciones.TamanoCuadro * (CasillaPresionada.columna - 1),
        Opciones.SangriaSup + Opciones.TamanoCuadro * (8 - CasillaPresionada.fila)))

    if CasillaPresionada.pieza is not None:
        if CasillaPresionada.pieza.activo:
            screen.blit(CasillaPresionada.pieza.imagen, (
                Opciones.SangriaIzq + Opciones.TamanoCuadro * (CasillaPresionada.columna - 1),
                Opciones.SangriaSup + Opciones.TamanoCuadro * (8 - CasillaPresionada.fila)))

    screen.blit(juego.seleccion, (
        Opciones.SangriaIzq + Opciones.TamanoCuadro * (CasillaPresionada.columna - 1),
        Opciones.SangriaSup + Opciones.TamanoCuadro * (8 - CasillaPresionada.fila)))

    pygame.display.flip()


def dibujarJugada(movimientos, juego, screen):

    for movimiento in movimientos:

        CasillaValida = juego.tablero.casillas[movimiento[0]] \
                    [movimiento[1]]

        screen.blit(CasillaValida.imagen, (
            Opciones.SangriaIzq + Opciones.TamanoCuadro * (CasillaValida.columna - 1),
            Opciones.SangriaSup + Opciones.TamanoCuadro * (8 - CasillaValida.fila)))

        if CasillaValida.pieza is not None:
            if CasillaValida.pieza.activo:
                screen.blit(CasillaValida.pieza.imagen, (
                    Opciones.SangriaIzq + Opciones.TamanoCuadro * (CasillaValida.columna - 1),
                    Opciones.SangriaSup + Opciones.TamanoCuadro * (8 - CasillaValida.fila)))

        screen.blit(juego.jugadasValidas, (
            Opciones.SangriaIzq + Opciones.TamanoCuadro * (CasillaValida.columna - 1),
            Opciones.SangriaSup + Opciones.TamanoCuadro * (8 - CasillaValida.fila)))

    pygame.display.flip()


def recibirJugada(juego,screen):

    jugadaValida = False

    while not jugadaValida:

        piezaSeleccionada = None

        seleccionValida = False

        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            posicion = event.pos

            #Casillas de acuerdo al ajedrez
            casillaPresionada = [
            (8 - (posicion[1] - Opciones.SangriaSup) // Opciones.TamanoCuadro),
            ((posicion[0] - Opciones.SangriaIzq) // Opciones.TamanoCuadro) + 1
            ]

            if casillaPresionada[0] in range(1,9) and casillaPresionada[0] in range(1,9):

                if juego.tablero.casillas[casillaPresionada[0]][casillaPresionada[1]].pieza is None:
                    continue
                if not juego.tablero.casillas[casillaPresionada[0]][casillaPresionada[1]].pieza.activo:
                    continue
                if not juego.tablero.casillas[casillaPresionada[0]][casillaPresionada[1]].pieza.color == \
                    juego.jugadores[juego.turno % 2].color:
                    continue

                piezaSeleccionada = juego.tablero.casillas[casillaPresionada[0]][casillaPresionada[1]].pieza

                dibujarSeleccion(casillaPresionada,juego,screen)

            else:
                continue

        #Dibujado de las opciones por jugar
        dibujarJugada(piezaSeleccionada.movimientosDisponibles,juego,screen)

        #Espera la casilla de destino
        anotherEvent = pygame.event.wait()

        if anotherEvent.type == pygame.QUIT:
            sys.exit()
        elif anotherEvent.type == pygame.MOUSEBUTTONDOWN:
            nuevaPosicion = anotherEvent.pos

            # Casillas de acuerdo al ajedrez
            nuevaCasillaPresionada = [
            (8 - (nuevaPosicion[1] - Opciones.SangriaSup) // Opciones.TamanoCuadro),
            ((nuevaPosicion[0] - Opciones.SangriaIzq) // Opciones.TamanoCuadro) + 1
            ]

            if nuevaCasillaPresionada in piezaSeleccionada.movimientosDisponibles:

                jugadaValida = True

            #Redibujado
            dibujarPantalla(juego,screen)

    return [casillaPresionada, nuevaCasillaPresionada]


def main():

    pygame.init()

    borrarEventos()

    screen = pygame.display.set_mode((Opciones.AnchoPantalla, Opciones.AltoPantalla))
    pygame.display.set_caption("Automatic Chess")

    juego = Juego()

    dibujarPantalla(juego, screen)

    terminar = False

    while True:

        juego.iniciarTurno()

        if juego.jugadores[juego.turno % 2].movimientosDisponibles == 0:
            break

        jugada = recibirJugada(juego,screen)

        juego.desarrollarTurno(jugada)

        dibujarMovimiento(juego, screen, jugada)

        terminar = juego.terminarTurno()

        dibujarPantalla(juego, screen)


    if terminar:
        if (juego.turno % 2) == ((1 - Opciones.JugadorColor) // 2):
            print("Jugador Negro ganó")
        else:
            print("Jugador Blanco ganó")
    else:
        print("Empate")
        

if __name__ == "__main__":
    main()