# RETO 12
## Ejercicio 1
Para este punto hice un programa que toma los valores de un diccionario y los muestra en orden ascendente. Usé .values() para sacar todos los valores y luego los ordené con sorted(). Es importante que todos los valores fueran del mismo tipo (como todos números o todos textos), porque si no, no se puede ordenar bien.
```python
dic = {
    "a": 42,
    "b": 15,
    "c": 33,
    "d": 8,
    "e": 56,
    "f": 21,
    "g": 4,
    "h": 78,
    "i": 12,
    "j": 29,
    "k": 65,
    "l": 3,
    "m": 37,
    "n": 19,
    "o": 50,
    "p": 6,
    "q": 44,
    "r": 9,
    "s": 71,
    "u": 18,
    "v": 31,
    "w": 23,
    "x": 39,
    "y": 1,
    "z": 60
}

elementos=list(dic.values())
elementos.sort()
print(elementos)
```


## Ejercicio 2
Aquí hice una función que recibe dos diccionarios y los junta en uno nuevo. Si los dos tienen la misma clave, el valor que queda es el del primer diccionario (como lo pedía el ejercicio). Lo resolví copiando el primer diccionario y luego agregando las claves del segundo solo si no estaban ya.
```python
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

```

## Ejercicio 3
En este punto trabajé con un JSON que contiene información de varias personas. En el programa le pido al usuario que escriba un deporte, y muestro los nombres completos de quienes lo practican. Luego también le pido una edad mínima y máxima, y muestro las personas que estén dentro de ese rango. 
```python
import json
jsooon='''
{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "Diaz Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["Futbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}
'''
yeison=json.loads(jsooon)

deporteusu=input('Ingrese el nombre del deporte: ')
for j in yeison:
    persona=yeison[j]
    for i in persona["deportes"]:
        if i.lower()==deporteusu:
            nombre_completo=persona["nombres"]+' '+persona["apellidos"]
            print(nombre_completo)

edad_max=int(input('Ingrese edad máxima: '))
edad_min=int(input('Ingrese edad mínima: '))

for j in yeison:
    persona=yeison[j]
    edad=persona["edad"]
    if edad_min <= edad <= edad_max:
        nombre_completo2=persona["nombres"]+' '+persona["apellidos"]
        print(nombre_completo2)
```

## Ejercicio 4
Para este último punto me conecté a tres APIs públicas usando el módulo requests. Cada API me devolvió datos en formato JSON, que imprimí y luego recorrí para mostrar cada par clave: valor. Usé una API de chistes de Chuck Norris, una de actividades aleatorias y una que da información de personas al azar.
```python
import requests

# 1. API de chistes
url1 = "https://api.chucknorris.io/jokes/random"
resp1 = requests.get(url1)
datos1 = resp1.json()
print("\n--- API 1: Chiste ---")
print(datos1)
for clave, valor in datos1.items():
    print(f"{clave}: {valor}")

# 2. API de actividad aleatoria
url2 = "https://www.boredapi.com/api/activity"
resp2 = requests.get(url2)
datos2 = resp2.json()
print("\n--- API 2: Actividad ---")
print(datos2)
for clave, valor in datos2.items():
    print(f"{clave}: {valor}")

# 3. API de persona aleatoria
url3 = "https://randomuser.me/api/"
resp3 = requests.get(url3)
datos3 = resp3.json()
print("\n--- API 3: Persona aleatoria ---")
print(datos3)
# solo claves del primer resultado
for clave, valor in datos3["results"][0].items():
    print(f"{clave}: {valor}")
```

Muchas gracias.
