#------------------Ejercicio S.Fibonacci------------------------------
def fib(n):
    a = 0
    b = 1 

    n= int(input("Por favor escribe el limite que deseas para la secuencia"))

    for i in range (n):
        c = b + a
        a = b
        b = c   
 
    return a 
