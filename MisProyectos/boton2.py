import board
import time
from ideaboard import IdeaBoard
from time import sleep

ib = IdeaBoard()

boton = ib.DigitalIn(board.IO27, pull=ib.UP) # True o False
pot = ib.AnalogIn(board.IO33) # 0-65535 2^16

AZUL = (0,0,255) # R,V,A (rojo, verde, azul)
VERDE = (0,255,0)
ROJO = (255,0,0)
AMARILLO= (255,255,0)
NEGRO = (0,0,0)

while True:
    if not boton.value:  # Si el botón está presionado (valor bajo)
        ib.pixel = ROJO  # Cambia el color del bombillo a rojo
    else:
        ib.pixel = NEGRO  # Si no se presiona el botón, el bombillo es negro
