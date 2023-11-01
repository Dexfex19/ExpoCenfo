import socketpool
import ssl
import wifi
import adafruit_requests as requests
import time
from secrets import secrets
import board
from ideaboard import IdeaBoard

socket = socketpool.SocketPool(wifi.radio)
https = requests.Session(socket, ssl.create_default_context())

ib = IdeaBoard()

boton = ib.DigitalIn(board.IO27, pull=ib.UP) # True o False
pot = ib.AnalogIn(board.IO33) # 0-65535 2^16

AZUL = (0,0,255) # R,V,A (rojo, verde, azul)
VERDE = (0,255,0)
ROJO = (255,0,0)
AMARILLO= (255,255,0)
NEGRO = (0,0,0)


print("Connecting...")
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to Wifi!")


URL = "https://ideaboard-api.azurewebsites.net/api/Board/getInformacion"
URL_POST= "https://ideaboard-api.azurewebsites.net/api/Board/postInformacion"
# metodo get
data = https.get(URL).json()
print ( "Resultado del get", data)
    
# metodo post
while True:
    if pot.value>40000:
        ib.pixel = ROJO
        data = {'id': '02',
        'temperatura': '35 grados',
        'humedadRelativa': 'Humedad relativa alta'}
    elif pot.value < 40000 and pot.value>20000:
        ib.pixel = AMARILLO
        data = {'id': '02',
        'temperatura': '30 grados',
        'humedadRelativa': 'Humedad relativa media'}
    else:
        ib.pixel=VERDE
        data = {'id': '02',
        'temperatura': '25 grados',
        'humedadRelativa': 'Humedad relativa baja'}
    result = https.post(URL_POST, json=data)
    print ("Resultado de prueba post", result.json())
    time.sleep(3)
