import paho.mqtt.client as mqtt
import time

broker = "127.0.0.1"  # O la IP de la máquina A si no está en localhost
port = 1883
topic = "sensor/temperature"

client = mqtt.Client()
client.connect(broker, port)

while True:
    message = "Temperatura: 25°C"
    client.publish(topic, message)
    print(f"Mensaje publicado: {message}")
    time.sleep(5)
