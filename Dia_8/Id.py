import json

archivito= open('Dates.json')
miJson= json.load(archivito)

ListaPedidos= []
for i in miJson['ventas']['pedidos']:
    ListaPedidos.append(i['id_cliente'])
Sin_repetir= set(ListaPedidos)

print(Sin_repetir) 
