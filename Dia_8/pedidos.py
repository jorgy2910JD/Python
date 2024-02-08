import json

archivito= open('Dates.json')
miJson= json.load(archivito)

def fechas_p(pedido):
     return pedido['fecha']
numero_pedidos= (miJson['ventas'] ['pedidos'])
pedidos_ordenados= sorted(numero_pedidos, key=fechas_p, reverse=True)
print(pedidos_ordenados) 
