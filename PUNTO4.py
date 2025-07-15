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
