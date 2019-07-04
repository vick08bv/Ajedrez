#Coordenadas
#Python pygame:
#(largo, altura)

#Ajedrez
#(fila,columna)

#Cambio de coordenadas
#largo = columna - 1
#altura = 8 - fila

SangriaIzq = 20
SangriaDer = 20
SangriaSup = 20
SangriaInf = 20

TamanoCuadro = 80
TamanoTablero = 8 * TamanoCuadro

AnchoPantalla = TamanoTablero + SangriaDer + SangriaIzq
AltoPantalla = TamanoTablero + SangriaSup + SangriaInf

JugadorColor = 1

#Primer color, segundo color
ColorPiezas = [9,2]
#Tipo de Textura,Opcion de color
ColorFondo = [7,0]

#Fondo de la pantalla
FondoPantalla = (60, 10, 10)

SimetriaPiezas = False