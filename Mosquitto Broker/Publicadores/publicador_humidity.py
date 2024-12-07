import paho.mqtt.client as mqtt
import time

# Configuración del broker
broker = "127.0.0.1"  # Cambia a la IP de tu máquina con el broker si no es local
port = 1883
topic = "sensor/humidity"

# Crear el cliente MQTT
client = mqtt.Client()
client.connect(broker, port)

try:
    while True:
        message = "Humedad: 60%"
        client.publish(topic, message)
        print(f"Mensaje publicado: {message}")
        time.sleep(5)  # Publica cada 5 segundos
except KeyboardInterrupt:
    print("Publicador detenido.")
    client.disconnect()
