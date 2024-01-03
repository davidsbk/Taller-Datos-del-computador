import mysql.connector

# Configurar la conexión a la base de datos
conexion_bd = mysql.connector.connect(
    host="tu_host",
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

# Crear un cursor para ejecutar consultas SQL
cursor = conexion_bd.cursor()

# Ejemplo de consulta SELECT
consulta_sql = "SELECT * FROM tu_tabla"
cursor.execute(consulta_sql)

# Obtener resultados de la consulta
resultados = cursor.fetchall()

# Imprimir resultados
for resultado in resultados:
    print(resultado)

# Cerrar el cursor y la conexión
cursor.close()
conexion_bd.close()
