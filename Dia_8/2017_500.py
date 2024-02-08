import json

archivito= open('Dates.json')
miJson= json.load(archivito)

cont=0
Lista2017 = []
for j in miJson["ventas"]["pedidos"]:
    if "2017" in miJson["ventas"]["pedidos"][cont]["fecha"]:
        if miJson["ventas"]["pedidos"][cont]["total"] > 500:
            Lista2017.append(j)
        cont += 1
    else:
        cont += 1

for i in Lista2017:
    print(i) 