import psutil

def mostrar_frecuencia_cpu():
    # Obtener información sobre la frecuencia del CPU
    frecuencias = psutil.cpu_freq()

    print("----------------------------------------------------")
    print("Frecuencia actual del CPU:")
    print(f"Frecuencia actual: {frecuencias.current} MHz")
    print(f"Frecuencia mínima: {frecuencias.min} MHz")
    print(f"Frecuencia máxima: {frecuencias.max} MHz")

if __name__ == "__main__":
    mostrar_frecuencia_cpu()


def mostrar_rendimiento_memoria():
    # Obtener información sobre el uso de la memoria
    memoria = psutil.virtual_memory()

    print("----------------------------------------------------")
    print("Información sobre el rendimiento de la memoria:")
    print(f"Memoria total: {memoria.total / (1024 ** 3):.2f} GB")
    print(f"Memoria disponible: {memoria.available / (1024 ** 3):.2f} GB")
    print(f"Memoria utilizada: {memoria.used / (1024 ** 3):.2f} GB")
    print(f"Porcentaje de uso de la memoria: {memoria.percent}%")

if __name__ == "__main__":
    mostrar_rendimiento_memoria()

def mostrar_rendimiento_almacenamiento():
    # Obtener información sobre el uso del almacenamiento interno
    almacenamiento = psutil.disk_usage('/')

    print("----------------------------------------------------")
    print("Información sobre el rendimiento del almacenamiento interno:")
    print(f"Almacenamiento total: {almacenamiento.total / (1024 ** 3):.2f} GB")
    print(f"Almacenamiento utilizado: {almacenamiento.used / (1024 ** 3):.2f} GB")
    print(f"Almacenamiento libre: {almacenamiento.free / (1024 ** 3):.2f} GB")
    print(f"Porcentaje de uso del almacenamiento: {almacenamiento.percent}%")

if __name__ == "__main__":
    mostrar_rendimiento_almacenamiento()


def mostrar_uso_de_red():
    # Obtener información sobre el uso de la red
    redes = psutil.net_io_counters(pernic=True)

    print("Información sobre el uso de la red:")
    for interfaz, datos in redes.items():
        
        print("----------------------------------------------------")
        print(f"Interfaz: {interfaz}")
        print(f"Bytes enviados: {datos.bytes_sent}")
        print(f"Bytes recibidos: {datos.bytes_recv}")
        print(f"Packets enviados: {datos.packets_sent}")
        print(f"Packets recibidos: {datos.packets_recv}")
        print("-----------------------------")

if __name__ == "__main__":
    mostrar_uso_de_red()
