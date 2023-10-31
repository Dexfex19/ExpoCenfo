import socketpool
import ssl
import wifi
import adafruit_requests as requests
from time import sleep
from secrets import secrets

socket = socketpool.SocketPool(wifi.radio)
https = requests.Session(socket, ssl.create_default_context())

print("Connecting...")
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to Wifi!")

URL = "https://ideaboard-api.azurewebsites.net/api/Board/getInformacion"

# metodo get
data = https.get(URL).json()
print ( "Resultado del get", data)

# metodo post
URL_POST= "https://ideaboard-api.azurewebsites.net/api/Board/postInformacion"

data = {'id': '02',
        'temperatura': '25 grados',
        'humedadRelativa': 'Humedad relativa baja'
    }

result = https.post(URL_POST, json=data)
print ("Resultado de prueba post", result.json())