import paho.mqtt.client as mqtt
from datetime import datetime
import time
import psutil

# Configuración del cliente MQTT
broker_address = "broker.hivemq.com"
port = 1883
topic = "uce/arquitectura/grupo2024"

# Callback para el evento de conexión
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conexión exitosa al broker MQTT")
    else:
        print(f"Fallo en la conexión. Código de retorno: {rc}")

# Inicializar el cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect

# Conectar al broker MQTT
client.connect(broker_address, port, 60)
frecuencia = psutil.cpu_freq()

      # Imprimir la frecuencia actual en MHz
freq="Frecuencia actual del procesador: {frecuencia.current} MHz" 
# Iniciar el bucle de red del cliente MQTT en un hilo separado
client.loop_start()

try:
    
    while True:
        frecuencia = psutil.cpu_freq()

      # Imprimir la frecuencia actual en MHz
        freq="Frecuencia actual del procesador: {frecuencia.current} MHz" 
        client.publish(topic, freq)
        # Obtener la fecha y hora actual
        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Publicar la fecha y hora en el tema MQTT
        client.publish(topic, fecha_hora_actual)

        # Esperar antes de enviar el siguiente mensaje
        time.sleep(1)
     
except KeyboardInterrupt:
    # Desconectar el cliente MQTT al recibir una interrupción de teclado
    client.disconnect()
    client.loop_stop()
    print("Cliente MQTT desconectado.")
