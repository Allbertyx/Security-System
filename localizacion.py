import geocoder

class localizacion():

    #saca la ubicacion mediante la ip del dispositivo
    g = geocoder.ip("me")

    #guardar los valores de la localizacion en un diccionario
    dicLocalizacion = {"latitud": g.lat, "longitud": g.lng, "ciudad": g.city, "pais": g.country}

    print("se ha obtenido la localizacion")


