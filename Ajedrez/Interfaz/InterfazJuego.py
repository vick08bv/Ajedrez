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
    casillaOr = juego.tablero.casillas[jugada[0][0] - 1][jugada[0][1] - 1]
    #CasillaDestino
    casillaDes = juego.tablero.casillas[jugada[1][0] - 1][jugada[1][1] - 1]

    for paso in range(0,Opciones.TamanoCuadro + 1,1):

        pygame.time.wait(5)

        for fila in juego.tablero.casillas:
            for casilla in fila:
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

    CasillaPresionada = juego.tablero.casillas[casillaPresionada[0] - 1] \
                    [casillaPresionada[1] - 1]

    screen.blit(CasillaPresionada.imagen, (
        Opciones.SangriaIzq + Opciones.TamanoCuadro * (CasillaPresionada.columna - 1),
        Opciones.SangriaSup + Opciones.TamanoCuadro * (8 - CasillaPresionada.fila)))

    if CasillaPresionada.pieza is not None:
        if CasillaPresionada.pieza.activo:
            screen.blit(CasillaPresionada.pieza.imagen, (
                Opciones.SangriaIzq + Opciones.TamanoCuadro * (CasillaPresionada.columna - 1),
                Opciones.SangriaSup + Opciones.TamanoCuadro * (8 -CasillaPresionada.fila)))

    screen.blit(juego.seleccion, (
        Opciones.SangriaIzq + Opciones.TamanoCuadro * (CasillaPresionada.columna - 1),
        Opciones.SangriaSup + Opciones.TamanoCuadro * (8 - CasillaPresionada.fila)))

    pygame.display.flip()


def dibujarJugada(movimientos,juego,screen):

    for movimiento in movimientos:

        CasillaValida = juego.tablero.casillas[movimiento[0] - 1] \
                    [movimiento[1] - 1]

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

            for pieza in juego.jugadores[juego.turno % 2].piezas:
                if [pieza.fila,pieza.columna] == casillaPresionada:

                    piezaSeleccionada = pieza

                    seleccionValida = True

                    dibujarSeleccion(casillaPresionada,juego,screen)

            if not seleccionValida:
                #NuevaSelección
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
    pygame.display.set_caption("Juego Prueba")

    juego = Juego()

    dibujarPantalla(juego, screen)

    while True:

        juego.iniciarTurno()

        if (juego.turno % 2) == ((1 - Opciones.JugadorColor) // 2):
            print("Blanco")
        else:
            print("Negro")

        jugada = recibirJugada(juego,screen)
        tipoJugada = juego.set_registro(jugada)
        juego.jugadores[juego.turno % 2].mover(jugada,juego.tablero,tipoJugada)
        dibujarMovimiento(juego, screen, jugada)

        for jugador in juego.jugadores:
            for pieza in jugador.piezas:
                if pieza is None:
                    print("Nada")
                else:
                    if pieza.activo:
                        print(pieza is juego.tablero.casillas[pieza.fila-1][pieza.columna-1])
                        print(pieza)
                    else:
                        print("No activa")


if __name__ == "__main__":
    main()