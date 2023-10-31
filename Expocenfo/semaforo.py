import board
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
    if pot.value>40000:
        ib.pixel = ROJO
        ib.motor_1.throttle = 1.0
    elif pot.value < 40000 and pot.value>20000:
        ib.pixel = AMARILLO
        ib.motor_1.throttle = 0
    else:
        ib.pixel=VERDE
        ib.motor_1.throttle = -1.0