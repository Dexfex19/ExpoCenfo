# README - Proyecto ComfortPet Sensor / Quantum Coders 

![image](https://github.com/Dexfex19/ExpoCenfo/assets/65746618/40810536-2e2f-40bd-9e56-55e31dca45ac)


## Descripción del Proyecto

El "ComfortPet Sensor" es un prototipo de un dispositivo accesorio innovador diseñado para garantizar el bienestar de las mascotas durante su estancia en el hotel Pet Inc. Este dispositivo utiliza un microcontrolador IdeaBoard (ESP32) en combinación con un sensor DHT11 para monitorear la temperatura y la humedad relativa en el entorno de las mascotas. El dispositivo se comunica con la API de la aplicación del hotel, enviando mediciones periódicas en formato JSON.

La información emitida por el dispositivo se asocia a una reserva y se almacenan en una base de datos, lo que permite al administrador del hotel visualizar y generar informes para evaluar el bienestar de sus mascotas huéspedes. Además, los clientes pueden confirmar el estado en el que se encuentra su mascota durante su estancia en el hotel.

El "ComfortPet Sensor" no solo monitoriza las condiciones ambientales, sino que también garantiza el bienestar de la mascota ajustando la temperatura ambiente de la habitación. Esto se logra mediante la comunicación del dispositivo con otro IdeaBoard (ESP32), que controla un ventilador o abanico en la habitación del hotel. De esta manera, el dispositivo contribuye activamente a mantener un entorno cómodo y seguro para las mascotas.

## Características Principales

- Monitoreo en tiempo real de la temperatura y la humedad relativa en la habitación de la mascota.
- Comunicación con la API del hotel para el registro y almacenamiento de datos.
- La información que proporciona el  dispositivo permite generación de informes y visualización de datos para el dueño del hotel.
- Comunicación con dispositivos de control de temperatura en la habitación de la mascota.

## Estructuras de datos

```json
[
    {
        'momento': 'AAAA-MM-DD hh:mm:ss',
        'temperatura': '25 grados',
        'humedadRelativa': 'Humedad relativa baja',
        'dispositivo': '02'
    }
]
```

![Clase Iot Data](https://github.com/Dexfex19/ExpoCenfo/assets/65746618/07aa05b0-21f3-4bd6-8c04-77de32c0bc18)


## Diagrama conceptual de la solución

![Dispositivo](https://github.com/Dexfex19/ExpoCenfo/assets/65746618/9e0d2ee6-4a36-454c-beb9-bd608ee858ba)

## Diagrama flujo de transmisión de datos

![Transmision de datos](https://github.com/Dexfex19/ExpoCenfo/assets/65746618/997ffa9e-3e2a-460b-9dad-af1fa2f53f80)


## Licencia

Este proyecto está licenciado bajo los términos de la Licencia MIT. 

---

Esperamos que el "ComfortPet Sensor" sea una herramienta valiosa para garantizar el bienestar de las mascotas en hoteles para perros y que contribuya a la tranquilidad de los dueños y cuidadores. Si tiene alguna pregunta o necesita asistencia, no dude en ponerse en contacto con nuestro equipo de soporte.

