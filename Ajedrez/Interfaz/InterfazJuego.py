import sys
sys.path.append("..")
from Motor.Juego import *
from Interfaz import Opciones
from Interfaz import Archivos
import pygame
from pygame.locals import *


def main():


    pygame.init()

    screen = pygame.display.set_mode((Opciones.AnchoPantalla, Opciones.AltoPantalla))
    pygame.display.set_caption("Juego Prueba")

    juego = Juego()

    # Fondo, primer color
    fondo_blanco = pygame.image.load(Archivos.OpcionesFondos[Opciones.ColorFondo[0]][Opciones.ColorFondo[1]][0]).convert()
    fondo_blanco = pygame.transform.scale(fondo_blanco, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))

    # Fondo, segundo color
    fondo_negro = pygame.image.load(Archivos.OpcionesFondos[Opciones.ColorFondo[0]][Opciones.ColorFondo[1]][1]).convert()
    fondo_negro = pygame.transform.scale(fondo_negro, (Opciones.TamanoCuadro, Opciones.TamanoCuadro))


    for fila in range(1,9):
        for columna in range(1,9):
                if (fila % 2) == (columna % 2):
                    screen.blit(fondo_negro, (
                    Opciones.SangriaIzq + Opciones.TamanoCuadro * (columna - 1),
                    Opciones.SangriaSup + Opciones.TamanoCuadro * (8 - fila)))
                else:
                    screen.blit(fondo_blanco, (
                    Opciones.SangriaIzq + Opciones.TamanoCuadro * (columna - 1),
                    Opciones.SangriaSup + Opciones.TamanoCuadro * (8 - fila)))

    for jugador in juego.jugadores:
        for pieza in jugador.piezas:
            screen.blit(pieza.imagen, (
                Opciones.SangriaIzq + Opciones.TamanoCuadro * (pieza.columna - 1),
                Opciones.SangriaSup + Opciones.TamanoCuadro * (8- pieza.fila)))

    pygame.display.flip()

    while True:

        juego.rotarTurno()

        if (juego.turno % 2) == 0:
            #Entra en acción el jugador
            # Posibles entradas del teclado y mouse
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    posicion = event.pos

                    #Casillas de acuerdo al ajedrez
                    casillaPresionada = [
                    (8 - (posicion[1] - Opciones.SangriaSup) // Opciones.TamanoCuadro),
                    ((posicion[0] - Opciones.SangriaIzq) // Opciones.TamanoCuadro) + 1
                    ]

                    # si se presiona el botón izquierdo
                    if event.button == 1:
                        print(casillaPresionada)

                    # si se presiona el botón derecho
                    elif event.button == 3:
                        print(casillaPresionada)

if __name__ == "__main__":
    main()


