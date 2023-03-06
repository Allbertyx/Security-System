import smtplib, ssl
from time import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
from mongo import mongo

import os
import sys
import time


def envia_email():

    #emisor y receptor correo
    enviador = 'albertomansilla@ceroca.cat'
    asunto = "Te están robando"
    receptor = 'arnautoro@ceroca.cat'

    msg = MIMEMultipart()
    msg['From'] = enviador
    msg['Subject'] = asunto
    msg['To'] = receptor

    #hace la foto
    fecha = time.strftime("%d/%m/%y")
    guardarFecha = fecha.replace("/", "-")
    hora = time.strftime("%H:%M:%S")
    linkruta = "/home/aasecurity/Desktop/camer/imagen_" + guardarFecha + "_" + hora + ".png"

    os.system("fswebcam -i 0 -d /dev/video0 -r 640x480 -q --title @raspberry    " + linkruta)

    #mensaje
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(linkruta, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="captura3.jpg"')
    msg.attach(part)

    #llamada a la clase con la conexion a la bbdd

    mongo("arnautoro@ceroca.cat",time.strftime("%H:%M:%S"),time.strftime("%d/%m/%y"),linkruta)

    try:
        #concexion con el servidor smtp de google
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        #login en el correo
        s.login(user=enviador, password='47245851X')
        s.sendmail(enviador, receptor, "Envia este texto")  # Envia texto. Consulta Spam.
        s.sendmail(enviador, receptor, msg.as_string())  # Envia imagen.
        s.quit()
    except smtplib.SMTPException as error:
        print("Error")


envia_email()
print("mail enviado")
