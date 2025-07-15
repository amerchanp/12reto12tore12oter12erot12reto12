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