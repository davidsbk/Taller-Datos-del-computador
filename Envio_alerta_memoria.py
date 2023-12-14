import psutil
import smtplib
from email.mime.text import MIMEText

# Configuración de la cuenta de Gmail
usuario_gmail = 'correonotificacionac@gmail.com'
contrasena_gmail = 'rrmy qdxj lucb xjuh'

# Dirección de correo electrónico para recibir las notificaciones
destinatario = 'correonotificacionac@gmail.com'

# Función para enviar correo electrónico
def enviar_correo(subject, body):
    mensaje = MIMEText(body)
    mensaje['Subject'] = subject
    mensaje['From'] = usuario_gmail
    mensaje['To'] = destinatario

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(usuario_gmail, contrasena_gmail)
        server.sendmail(usuario_gmail, destinatario, mensaje.as_string())

# Monitoreo del rendimiento del sistema
def monitorear_memoria():
    try:
        uso_memoria = psutil.virtual_memory().percent

        if uso_memoria > 40:
            subject = 'Alerta de Uso de Memoria del CPU'
            body = f'El uso de la memoria del CPU ha superado el 40%. Actualmente es {uso_memoria}%.'
            
            enviar_correo(subject, body)
    except Exception as e:
        print(f"Error al monitorear la memoria: {str(e)}")

# Llamada a la función de monitoreo
monitorear_memoria()