#Coordenadas
#Python pygame:
#(largo, altura)

#Ajedrez
#(fila,columna)

#Cambio de coordenadas
#largo = columna - 1
#altura = 8 - fila

SangriaIzq = 100
SangriaDer = 200
SangriaSup = 0
SangriaInf = 0

TamanoTablero = 640
TamanoCuadro = TamanoTablero//8

AnchoPantalla = TamanoTablero + SangriaDer + SangriaIzq
AltoPantalla = TamanoTablero + SangriaSup + SangriaInf

#Primer color, segundo color
ColorPiezas = [5,6]
#Tipo de Textura,Opcion de color
ColorFondo = [7,0]

SimetriaPiezas = False

