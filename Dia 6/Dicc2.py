#Diccionario de productos------------
#------------------------------------

def procedimiento(productos):
    producto= str(input('Escribe los productos que desees llevar por favor: ')).lower()
    if producto in productos['productos']:
        Cant_productos = int (input('Escribe la cantidad del/ de los productos que desees llevar '))
        IndiceProducto = productos['productos'].index(producto)
        total= productos['valor'][IndiceProducto]
        total = total * Cant_productos
        print(f'El valor a pagar es de:', total, '$')
    else:
         print('El producto no está disponible en este momento')



print("Bienvenido a tu supermercado virtual! ")
print("Estos son los productos disponibles ")
productos = {'productos':('Huevos', 'cartón', 'Leche', 'pan x6', 'Milo en sobre 25gr', 'Arroz', 'lentejas','mantequilla'), 'valor':(600, 12000, 4500, 3000,1100,7500,8500,7000)}
print(productos)
print(procedimiento(productos)) 



    


   