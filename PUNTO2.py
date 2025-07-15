diccionario1 = {
    "manzana": "fruta",
    "perro": "animal",
    "cielo": "azul",
    "fuego": "calor",
    "lluvia": "agua",
    "roca": "dura",
    "flor": "olor",
    "tren": "veloz",
    "mar": "salado",
    "nube": "algodón",
    "pájaro": "vuelo",
    "sol": "luz",
    "tierra": "suelo",
    "viento": "aire",
    "montaña": "alta",
    "río": "corriente",
    "noche": "oscura",
    "arena": "playa",
    "hoja": "verde",
    "lago": "tranquilo"
}

diccionario2 = {
    "pelota": "juego",
    "perro": "animal",
    "lago": "tranquilo",
    "ventana": "vidrio",
    "puerta": "entrada",
    "camino": "andar",
    "fuego": "calor",
    "estrella": "brilla",
    "ratón": "pequeño",
    "mesa": "madera",
    "libro": "leer",
    "computador": "tecnología",
    "silla": "sentarse",
    "planta": "vida",
    "auto": "rápido",
    "avión": "cielo",
    "mariposa": "colores",
    "sol": "luz",
    "carro": "motor",
    "puente": "cruzar"
}

def mezclar(dic1,dic2):
    diccomun=dict(dic1)
    for i in dic2:
        if i not in diccomun:
            diccomun[i]=dic2[i]
    return diccomun

#ejemplo d ejecución

ejem=mezclar(diccionario1, diccionario2)
print(ejem)
