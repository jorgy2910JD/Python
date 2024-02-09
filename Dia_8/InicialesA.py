import json
with open("Dates.json", "r") as f:
    miJson = json.load(f) 
#creamos lista
InicialA=[]
#Ciclo 'for' para recorres la lista de clientes y filtrar los nombres con inicial A
for cliente in miJson['ventas']['clientes']:
    inicial2= cliente['nombre']
    if inicial2.startswith("A"):
        InicialA.append(inicial2)

        #orden alfabetico
        InicialA.sort()

        #Impresion de los nombres en forma de lista
        print("Los nombres que comienzan por A son: ")
        for inicial2 in InicialA:
            print(inicial2)

