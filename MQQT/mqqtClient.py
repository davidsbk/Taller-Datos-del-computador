import paho.mqtt.client as mqtt

# Definir los callbacks para eventos MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conexión exitosa al broker MQTT")
        # Suscribirse a un tema al conectarse
        client.subscribe("uce/arquitectura/grupo1")

def on_message(client, userdata, msg):
    print(f"Mensaje recibido en el tema {msg.topic}: {msg.payload.decode()}")

# Configurar el cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Configurar la conexión al broker MQTT
broker_address = "broker.hivemq.com"
port = 1883
client.connect(broker_address, port, 60)

# Iniciar el bucle de red del cliente MQTT
client.loop_start()

# Publicar un mensaje en un tema
topic = "uce/arquitectura/grupo1"
message = "Hola, mundo!"
client.publish(topic, message)

# Mantener el programa en ejecución
try:
    while True:
        pass
except KeyboardInterrupt:
    # Desconectar el cliente MQTT al recibir una interrupción de teclado
    client.disconnect()
    client.loop_stop()
    print("Cliente MQTT desconectado.")
