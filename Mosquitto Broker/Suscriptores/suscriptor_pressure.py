import paho.mqtt.client as mqtt

# Callback cuando se recibe un mensaje
def on_message(client, userdata, message):
    print(f"Mensaje recibido en {message.topic}: {message.payload.decode()}")

# Configuración del broker
broker = "127.0.0.1"  # IP del broker
port = 1883
topic = "sensor/pressure"

# Crear el cliente MQTT
client = mqtt.Client()
client.connect(broker, port)

# Suscribirse al tema
client.subscribe(topic)
client.on_message = on_message

print(f"Suscrito al tema {topic}")

# Mantener la conexión activa
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Suscriptor detenido.")
    client.disconnect()
