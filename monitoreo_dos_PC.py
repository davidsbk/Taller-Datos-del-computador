import psutil
import socket
import platform

def obtener_informacion_cpu():
    return psutil.cpu_freq()

def obtener_informacion_memoria():
    return psutil.virtual_memory()

def obtener_informacion_almacenamiento():
    return psutil.disk_usage('/')

def obtener_edicion_sistema_remota(ip, puerto=22, tiempo_espera=1):
    try:
        # Crear un socket para la conexión
        s = socket.create_connection((ip, puerto), timeout=tiempo_espera)

        # Obtener la información del sistema operativo utilizando platform
        sistema_operativo = platform.system()
        version_sistema = platform.version()

        # Cerrar el socket
        s.close()

        return f"Sistema Operativo: {sistema_operativo}\nVersión del Sistema: {version_sistema}"
    except Exception as e:
        return f"Error al obtener información del sistema remoto: {str(e)}"
# Cambiar 'ip_de_la_otra_pc' por la dirección IP de la otra computadora
ip_otra_pc = '10.3.20.246'

# Obtener información del CPU
info_cpu = obtener_informacion_cpu()
print(f"Frecuencia del CPU: {info_cpu.current} MHz")

# Obtener información de la memoria
info_memoria = obtener_informacion_memoria()
print(f"Uso de memoria: {info_memoria.percent}%")

# Obtener información del almacenamiento
info_almacenamiento = obtener_informacion_almacenamiento()
print(f"Uso de almacenamiento interno: {info_almacenamiento.percent}%")


# Obtener información remota del sistema
informacion_sistema_remoto = obtener_edicion_sistema_remota(ip_otra_pc)

# Mostrar la información remota del sistema
print(informacion_sistema_remoto)
