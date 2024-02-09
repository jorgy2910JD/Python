import json
with open("Dates.json", "r") as f:
    miJson = json.load(f) 

IniNames= []
#Ciclo 'for' para recorres la lista de clientes y filtrar los nombres con inicial A y final N
for cliente in miJson['ventas']['clientes']:
    inicial= cliente['nombre']
    if inicial.startswith("A") and inicial.endswith("n") or inicial.startswith("P"):

        IniNames.append(inicial)

        #ordenar nombres en orden alfabetico
        IniNames.sort()


     #se imprimen los nombres en forma de lista
        print("Los nombres que comienzan por A y terminan por n, tambien que inician con P son: ")  
        for inicial in IniNames:
            print(inicial) 