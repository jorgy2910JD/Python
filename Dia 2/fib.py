#------------------Ejercicio S.Fibonacci------------------------------
def fib(n):
    a = 0
    b = 1
    
    for i in range(n):
        c = b+a
        a = b
        b = c
        
        return a 