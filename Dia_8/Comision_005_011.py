import json
with open("Dates.json", "r") as f:
    miJson = json.load(f)

ListaC= []

for comercial in miJson['ventas']['comerciales']:
    if 0.05 <= comercial['comision'] <= 0.11:

        CompleteName= comercial['nombre'] + " " + comercial['apellido1'] + " " + comercial['apellido2']
        ListaC.append(CompleteName)


print("Estos son los comerciales que tienes una comision entre 0.05 y 0.11: ")
for nombre in ListaC:
    print(nombre) 