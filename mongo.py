import pymongo
import hashlib
import self as self
import bson.binary
import io

from PIL import Image
from cifrar import cifrar
from localizacion import localizacion


class mongo():

    def __init__(self, mail, hora, fecha, imagen):
        self.mail = mail
        self.hora = hora
        self.imagen = imagen
        self.fecha = fecha

        myclient = pymongo.MongoClient("mongodb+srv://Alberto:aasecurity@aasecurity-db.61m5uv9.mongodb.net/?retryWrites=true&w=majority")

        mydb = myclient["AASECURITY-DB"]
        mycol = mydb["Registro_camera" + self.fecha + "_" + self.hora]

        #mailIncriptado = hashlib.new("sha256", str(self.mail))
        mailCifrado = cifrar(self.mail)

        #pasar a binario la imagen
        with open(self.imagen, "rb") as image_file:
            self.encoded_image = bson.binary.Binary(image_file.read())

        image = Image.open(io.BytesIO(self.encoded_image))
        png_image = io.BytesIO()
        image.save(png_image, format="PNG")
        png_image_bytes = png_image.getvalue()

        #localizaciom
        diccionarioLocalizacion = localizacion()

        mydict = {"mail": str(mailCifrado.encMessage), "hora": self.hora,"fecha": self.fecha, "imagen": png_image_bytes, "localizacion": diccionarioLocalizacion.dicLocalizacion}

        x = mycol.insert_one(mydict)
        print("se ha guardado en Mongo")

