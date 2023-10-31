import socketpool
import ssl
import wifi
import adafruit_requests as requests
import time

socket = socketpool.SocketPool(wifi.radio)
https = requests.Session(socket, ssl.create_default_context())

print("Connecting...")
wifi.radio.connect("ARRIS-E532", "BP277U392446")
print("Connected to Wifi!")

URL = "http://api.open-notify.org/iss-now.json"

data = https.get(URL).json()

timestamp = data ['timestamp']- (6 * 3600) # se le resta 6 horas para tener la hora tica

human_time = time.localtime (timestamp) 

# print (human_time[0])
# print ("2023-10-30 00:00:00")
while  True:
    data= https.get(URL).json()
    timestamp = data ['timestamp']- (6 * 3600) # se le resta 6 horas para tener la hora tica
    human_time = time.localtime (timestamp)

    print (f"{human_time[0]}-{human_time [1]}-{human_time[2]} {human_time[3]}:{human_time[4]}:{human_time[5]}")
    time.sleep(3)
#esta linea superior es para imprimir los numeros de un timestamp a una forma humana pero es del international space station
