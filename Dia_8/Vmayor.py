import json

archivito= open('Dates.json')
miJson= json.load(archivito)


def valor_mayor(pedido):
    return pedido['total'] 

numero_pedidos= (miJson['ventas']['pedidos'])
pedidos_ordenados= sorted(numero_pedidos, key=valor_mayor, reverse=True)

print(pedidos_ordenados[0], pedidos_ordenados[1]) 