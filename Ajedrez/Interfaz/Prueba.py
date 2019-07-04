from Interfaz import Archivos
import pygame
from pygame.locals import *
import sys

SangriaIzq = 100
SangriaDer = 200
SangriaSup = 0
SangriaInf = 0

TamanoTablero = 640
Cuadro = TamanoTablero//8

Ancho = TamanoTablero + SangriaDer + SangriaIzq
Alto = TamanoTablero + SangriaSup + SangriaInf

#Primer color, segundo color
Piezas = [5,6]
#Tipo de Textura,Opcion de color
Fondo = [2,0]

Simetria = False

def main():
    pygame.init()
    screen = pygame.display.set_mode((Ancho, Alto))
    pygame.display.set_caption("Juego Prueba")


    #Fondo, primer color
    fondo_blanco = pygame.image.load(Archivos.OpcionesFondos[Fondo[0]][Fondo[1]][0]).convert()
    fondo_blanco = pygame.transform.scale(fondo_blanco, (Cuadro, Cuadro))

    #Fondo, segundo color
    fondo_negro = pygame.image.load(Archivos.OpcionesFondos[Fondo[0]][Fondo[1]][1]).convert()
    fondo_negro = pygame.transform.scale(fondo_negro, (Cuadro, Cuadro))


    if Simetria:

        caballoBlancoIzquierdo = pygame.image.load(Archivos.OpcionesPiezas[Piezas[0]][2]).convert_alpha()
        caballoBlancoIzquierdo = pygame.transform.scale(caballoBlancoIzquierdo, (Cuadro, Cuadro))

        alfilBlancoDerecho = pygame.image.load(Archivos.OpcionesPiezas[Piezas[0]][4]).convert_alpha()
        alfilBlancoDerecho = pygame.transform.scale(alfilBlancoDerecho, (Cuadro, Cuadro))

        caballoNegroIzquierdo = pygame.image.load(Archivos.OpcionesPiezas[Piezas[1]][2]).convert_alpha()
        caballoNegroIzquierdo = pygame.transform.scale(caballoNegroIzquierdo, (Cuadro, Cuadro))

        alfilNegroDerecho = pygame.image.load(Archivos.OpcionesPiezas[Piezas[1]][4]).convert_alpha()
        alfilNegroDerecho = pygame.transform.scale(alfilNegroDerecho, (Cuadro, Cuadro))

    else:

        caballoBlancoIzquierdo = pygame.image.load(Archivos.OpcionesPiezas[Piezas[0]][1]).convert_alpha()
        caballoBlancoIzquierdo = pygame.transform.scale(caballoBlancoIzquierdo, (Cuadro, Cuadro))

        alfilBlancoDerecho = pygame.image.load(Archivos.OpcionesPiezas[Piezas[0]][3]).convert_alpha()
        alfilBlancoDerecho = pygame.transform.scale(alfilBlancoDerecho, (Cuadro, Cuadro))

        caballoNegroIzquierdo = pygame.image.load(Archivos.OpcionesPiezas[Piezas[1]][1]).convert_alpha()
        caballoNegroIzquierdo = pygame.transform.scale(caballoNegroIzquierdo, (Cuadro, Cuadro))

        alfilNegroDerecho = pygame.image.load(Archivos.OpcionesPiezas[Piezas[1]][3]).convert_alpha()
        alfilNegroDerecho = pygame.transform.scale(alfilNegroDerecho, (Cuadro, Cuadro))

    #alpha == aplicar transparencia
    peonBlanco = pygame.image.load(Archivos.OpcionesPiezas[Piezas[0]][0]).convert_alpha()
    peonBlanco = pygame.transform.scale(peonBlanco, (Cuadro, Cuadro))

    caballoBlanco = pygame.image.load(Archivos.OpcionesPiezas[Piezas[0]][1]).convert_alpha()
    caballoBlanco = pygame.transform.scale(caballoBlanco, (Cuadro, Cuadro))

    alfilBlanco = pygame.image.load(Archivos.OpcionesPiezas[Piezas[0]][3]).convert_alpha()
    alfilBlanco = pygame.transform.scale(alfilBlanco, (Cuadro, Cuadro))

    torreBlanca = pygame.image.load(Archivos.OpcionesPiezas[Piezas[0]][5]).convert_alpha()
    torreBlanca = pygame.transform.scale(torreBlanca, (Cuadro, Cuadro))

    damaBlanca = pygame.image.load(Archivos.OpcionesPiezas[Piezas[0]][6]).convert_alpha()
    damaBlanca = pygame.transform.scale(damaBlanca, (Cuadro, Cuadro))

    reyBlanco = pygame.image.load(Archivos.OpcionesPiezas[Piezas[0]][7]).convert_alpha()
    reyBlanco = pygame.transform.scale(reyBlanco, (Cuadro, Cuadro))


    peonNegro = pygame.image.load(Archivos.OpcionesPiezas[Piezas[1]][0]).convert_alpha()
    peonNegro = pygame.transform.scale(peonNegro, (Cuadro, Cuadro))

    caballoNegro = pygame.image.load(Archivos.OpcionesPiezas[Piezas[1]][1]).convert_alpha()
    caballoNegro = pygame.transform.scale(caballoNegro, (Cuadro, Cuadro))

    alfilNegro = pygame.image.load(Archivos.OpcionesPiezas[Piezas[1]][3]).convert_alpha()
    alfilNegro = pygame.transform.scale(alfilNegro, (Cuadro, Cuadro))

    torreNegra = pygame.image.load(Archivos.OpcionesPiezas[Piezas[1]][5]).convert_alpha()
    torreNegra = pygame.transform.scale(torreNegra, (Cuadro, Cuadro))

    damaNegra = pygame.image.load(Archivos.OpcionesPiezas[Piezas[1]][6]).convert_alpha()
    damaNegra = pygame.transform.scale(damaNegra, (Cuadro, Cuadro))

    reyNegro = pygame.image.load(Archivos.OpcionesPiezas[Piezas[1]][7]).convert_alpha()
    reyNegro = pygame.transform.scale(reyNegro, (Cuadro, Cuadro))

    screen.blit(fondo_blanco, (SangriaIzq + 0 * Cuadro, SangriaSup + 0 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 0 * Cuadro, SangriaSup + 2 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 0 * Cuadro, SangriaSup + 4 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 0 * Cuadro, SangriaSup + 6 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 1 * Cuadro, SangriaSup + 1 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 1 * Cuadro, SangriaSup + 3 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 1 * Cuadro, SangriaSup + 5 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 1 * Cuadro, SangriaSup + 7 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 2 * Cuadro, SangriaSup + 0 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 2 * Cuadro, SangriaSup + 2 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 2 * Cuadro, SangriaSup + 4 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 2 * Cuadro, SangriaSup + 6 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 3 * Cuadro, SangriaSup + 1 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 3 * Cuadro, SangriaSup + 3 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 3 * Cuadro, SangriaSup + 5 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 3 * Cuadro, SangriaSup + 7 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 4 * Cuadro, SangriaSup + 0 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 4 * Cuadro, SangriaSup + 2 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 4 * Cuadro, SangriaSup + 4 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 4 * Cuadro, SangriaSup + 6 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 5 * Cuadro, SangriaSup + 1 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 5 * Cuadro, SangriaSup + 3 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 5 * Cuadro, SangriaSup + 5 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 5 * Cuadro, SangriaSup + 7 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 6 * Cuadro, SangriaSup + 0 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 6 * Cuadro, SangriaSup + 2 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 6 * Cuadro, SangriaSup + 4 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 6 * Cuadro, SangriaSup + 6 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 7 * Cuadro, SangriaSup + 1 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 7 * Cuadro, SangriaSup + 3 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 7 * Cuadro, SangriaSup + 5 * Cuadro))
    screen.blit(fondo_blanco, (SangriaIzq + 7 * Cuadro, SangriaSup + 7 * Cuadro))

    screen.blit(fondo_negro, (SangriaIzq + 0 * Cuadro, SangriaSup + 1 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 0 * Cuadro, SangriaSup + 3 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 0 * Cuadro, SangriaSup + 5 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 0 * Cuadro, SangriaSup + 7 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 1 * Cuadro, SangriaSup + 0 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 1 * Cuadro, SangriaSup + 2 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 1 * Cuadro, SangriaSup + 4 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 1 * Cuadro, SangriaSup + 6 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 2 * Cuadro, SangriaSup + 1 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 2 * Cuadro, SangriaSup + 3 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 2 * Cuadro, SangriaSup + 5 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 2 * Cuadro, SangriaSup + 7 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 3 * Cuadro, SangriaSup + 0 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 3 * Cuadro, SangriaSup + 2 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 3 * Cuadro, SangriaSup + 4 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 3 * Cuadro, SangriaSup + 6 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 4 * Cuadro, SangriaSup + 1 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 4 * Cuadro, SangriaSup + 3 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 4 * Cuadro, SangriaSup + 5 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 4 * Cuadro, SangriaSup + 7 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 5 * Cuadro, SangriaSup + 0 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 5 * Cuadro, SangriaSup + 2 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 5 * Cuadro, SangriaSup + 4 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 5 * Cuadro, SangriaSup + 6 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 6 * Cuadro, SangriaSup + 1 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 6 * Cuadro, SangriaSup + 3 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 6 * Cuadro, SangriaSup + 5 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 6 * Cuadro, SangriaSup + 7 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 7 * Cuadro, SangriaSup + 0 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 7 * Cuadro, SangriaSup + 2 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 7 * Cuadro, SangriaSup + 4 * Cuadro))
    screen.blit(fondo_negro, (SangriaIzq + 7 * Cuadro, SangriaSup + 6 * Cuadro))


    screen.blit(peonBlanco, (SangriaIzq + 0 * Cuadro, SangriaSup+ 6 * Cuadro))
    screen.blit(peonBlanco, (SangriaIzq + 1 * Cuadro, SangriaSup + 6 * Cuadro))
    screen.blit(peonBlanco, (SangriaIzq + 2 * Cuadro, SangriaSup + 6 * Cuadro))
    screen.blit(peonBlanco, (SangriaIzq + 3 * Cuadro, SangriaSup + 6 * Cuadro))
    screen.blit(peonBlanco, (SangriaIzq + 4 * Cuadro, SangriaSup + 6 * Cuadro))
    screen.blit(peonBlanco, (SangriaIzq + 5 * Cuadro, SangriaSup + 6 * Cuadro))
    screen.blit(peonBlanco, (SangriaIzq + 6 * Cuadro, SangriaSup + 6 * Cuadro))
    screen.blit(peonBlanco, (SangriaIzq + 7 * Cuadro, SangriaSup + 6 * Cuadro))

    screen.blit(torreBlanca, (SangriaIzq + 0 * Cuadro, SangriaSup+ 7 * Cuadro))
    screen.blit(torreBlanca, (SangriaIzq + 7 * Cuadro, SangriaSup+ 7 * Cuadro))

    screen.blit(caballoBlancoIzquierdo, (SangriaIzq + 1 * Cuadro, SangriaSup + 7 * Cuadro))
    screen.blit(caballoBlanco, (SangriaIzq + 6 * Cuadro, SangriaSup+ 7 * Cuadro))

    screen.blit(alfilBlanco, (SangriaIzq + 2 * Cuadro, SangriaSup+ 7 * Cuadro))
    screen.blit(alfilBlancoDerecho, (SangriaIzq + 5 * Cuadro, SangriaSup+ 7 * Cuadro))

    screen.blit(damaBlanca, (SangriaIzq + 3 * Cuadro, SangriaSup+ 7 * Cuadro))
    screen.blit(reyBlanco, (SangriaIzq + 4 * Cuadro, SangriaSup+ 7 * Cuadro))


    screen.blit(peonNegro, (SangriaIzq + 0 * Cuadro, SangriaSup + 1 * Cuadro))
    screen.blit(peonNegro, (SangriaIzq + 1 * Cuadro, SangriaSup + 1 * Cuadro))
    screen.blit(peonNegro, (SangriaIzq + 2 * Cuadro, SangriaSup + 1 * Cuadro))
    screen.blit(peonNegro, (SangriaIzq + 3 * Cuadro, SangriaSup + 1 * Cuadro))
    screen.blit(peonNegro, (SangriaIzq + 4 * Cuadro, SangriaSup + 1 * Cuadro))
    screen.blit(peonNegro, (SangriaIzq + 5 * Cuadro, SangriaSup + 1 * Cuadro))
    screen.blit(peonNegro, (SangriaIzq + 6 * Cuadro, SangriaSup + 1 * Cuadro))
    screen.blit(peonNegro, (SangriaIzq + 7 * Cuadro, SangriaSup + 1 * Cuadro))

    screen.blit(torreNegra, (SangriaIzq + 0 * Cuadro, SangriaSup+ 0 * Cuadro))
    screen.blit(torreNegra, (SangriaIzq + 7 * Cuadro, SangriaSup+ 0 * Cuadro))

    screen.blit(caballoNegroIzquierdo, (SangriaIzq + 1 * Cuadro, SangriaSup+ 0 * Cuadro))
    screen.blit(caballoNegro, (SangriaIzq + 6 * Cuadro, SangriaSup+ 0 * Cuadro))

    screen.blit(alfilNegro, (SangriaIzq + 2 * Cuadro, SangriaSup+ 0 * Cuadro))
    screen.blit(alfilNegroDerecho, (SangriaIzq + 5 * Cuadro, SangriaSup+ 0 * Cuadro))

    screen.blit(damaNegra, (SangriaIzq + 3 * Cuadro, SangriaSup+ 0 * Cuadro))
    screen.blit(reyNegro, (SangriaIzq + 4 * Cuadro, SangriaSup+ 0 * Cuadro))

    pygame.display.flip()

    while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()

