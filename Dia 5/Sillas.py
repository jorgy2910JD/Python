from itertools import combinations

n = int(input("Ingrese el número de tipos de monedas disponibles: "))
t = int(input("Ingrese la cantidad de mesas a diseñar: "))

for _ in range(t):
    monedas = []
    print(f"Ingrese el grosor de las {n} monedas:")
    for _ in range(n):
        moneda = int(input())
        monedas.append(moneda)

    print(f"Ingrese la altura de la mesa:")
    longitud = int(input())

    # Generar todas las combinaciones posibles de 4 monedas
    combinaciones = list(combinations(monedas, 4))

    # Calcular la longitud máxima y mínima de las patas de la mesa
    max_length = max(sum(combinacion) for combinacion in combinaciones if sum(combinacion) <= longitud)
    min_length = min(sum(combinacion) for combinacion in combinaciones if sum(combinacion) >= longitud)

    # Salida de los resultados
    print(max_length,min_length)
    