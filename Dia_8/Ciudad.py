import json
with open("Dates.json", "r") as f:
    miJson = json.load(f) 

#Crear listica
SevillaFC= []
#Ciclo 'for' para recorres la lista de clientes y filtrar los que son de Sevilla
for cliente in miJson['ventas']['clientes']:
    if cliente['ciudad']== 'Sevilla':
        #Se crea un Dicc con el Id, el nombre, y el primer apellido del cliente
        Dicc_Dates= {'id': cliente['id'], 'nombre': cliente['nombre'], 'apellido1': cliente['apellido1']}
        SevillaFC.append(Dicc_Dates)


SevillaFC.sort(key=lambda x: (x["apellido1"], x["nombre"]))

print("Los clientes de la ciudad de Sevilla son: ")

for Dicc_Dates in SevillaFC:
    print(Dicc_Dates['id'], Dicc_Dates['nombre'], Dicc_Dates['apellido1']) 