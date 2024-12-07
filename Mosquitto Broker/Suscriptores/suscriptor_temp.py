import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Mensaje recibido en {message.topic}: {message.payload.decode()}")

broker = "127.0.0.1"  # Dirección IP del Broker
port = 1883
topic = "sensor/temperature"

client = mqtt.Client()
client.connect(broker, port)

client.subscribe(topic)
client.on_message = on_message

print(f"Suscrito al tema {topic}")
client.loop_forever()
