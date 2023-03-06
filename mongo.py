import pymongo
import hashlib
import self as self

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

        #localizaciom
        diccionarioLocalizacion = localizacion()

        mydict = {"mail": str(mailCifrado.encMessage), "hora": self.hora,"fecha": self.fecha, "imagen": self.imagen, "localizacion": diccionarioLocalizacion.dicLocalizacion}

        x = mycol.insert_one(mydict)
        print("se ha guardado en Mongo")

