
##---------------------------------------
##---EJercicio 1---
##---------------------------------------

#----------Funcion Sin/Sin---------------
def saludo():
    print("hola")
#Impresion de consola 
Fun1 = saludo()
print ( " hola mundo ")

#----------Funcion Con/Con---------------
def Operacion(a,b):
    c = a + b
    return c
n = int(input("Digite un número"))
t = int(input("Digite otro número"))
print(Operacion(n,t))

#---------Función Con/Sin----------------
def suma(a,b):
    c = a + b 
    print(c)
a = 5
b = 10
Fun2 = suma(a,b)

#---------Función Sin/Con----------------
def multiplicacion():
    print ("multiplicaión de dos numeros")
    Num1= float(input("ingrese el primer número por favor"))
    Num2= float(input("ingrese el segundo número por favor"))
    return Num1*Num2
result= multiplicacion()
print(result)

#-------------arrays----------------------

Limite = int(input("Escriba cuantos nombres deseea almacenar por favor "))
ListaNombres = [Limite]
for i in range (Limite):
    Almacenador = str(input(f"ingrese el nombre {i+1}: ")) #str es para identificar elemento como caracter(texto)
    ListaNombres.append(Almacenador)
print(ListaNombres)
 
#-----Datos primitivos-------------------
#1. String
Texto =  " CAMPUS " 
print ( Texto)
print (type(Texto) )
#2. Int
numeroentero = 1 
print (numeroentero)

#3.Double
numerodecimallargo =3.1416239823982
print (numerodecimallargo)
#4. Float
numerodecimal= 3.5
print(numerodecimal)
#5 Boolean 
booleano= True
print(booleano)
#------Entrada por parte del usuario------
User = input( "ingresa tu nombre: ")
print ("tu nombre es:" , User)
#----------Entrada por parte del usuario con definicion de datos primitivos--------
Edad =input ("Ingresa tu edad: ")
numeroFinal = int (Edad)
print ("Tu edad es: " , numeroFinal)

#------Ciclos------
#ciclo for 
for i in range (5,10): # for contador in range (desde, hasta, pasos)
    print (i)
#ciclo while
    booleanito = True 
    while booleanito == True: #while condición_a_cumplir :
        print ("sigo vivo")
        booleanito= False
        #-------condicionales--------
    texto1 = "Campus"
    if texto1 == "Campus":
        print ("Soy campus")
    else:
        print ("No soy campus")
##Desarrollado por JORGE LUIS MOZO CASTRO - 1099738869