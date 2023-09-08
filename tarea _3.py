import time
inicio = time.time()

number1=int(input("ingresa un numero "))
number2=int(input("ingresa el segundo numeron "))

eleccion=0
while eleccion!=6:

    print("""
          
          Seleccione la opcion deseada:
          
          1) Suma
          2) Resta 
          3) Multiplicacion 
          4) Division 
          5) cambio de valores 
          6) Salir 
          """)
    eleccion=int(input())

    if eleccion == 1:
        print("El resultado es: ",number1, "+",number2, "=",number1+number2)
        res = 0
        for i in range(0,1000):
            res = res + i
        

        fin = time.time()
        tiempo_ejecutado = fin - inicio
        print("el tiempo que tarda en ejecutarse es de :")
        print(tiempo_ejecutado)
       

    if eleccion == 2:
        print("El resultado es: ",number1, "-",number2, "=",number1-number2)
        res =0
        for i in range(0,1000):
            res = res+i
        
        fin =time.time()
        tiempo_ejecutado = fin - inicio
        print("el tiempo que tarda en ejecutarse es de :")
        print(tiempo_ejecutado)
       
    
    if eleccion == 3:
        print("El resultado es: ",number1, "x",number2, "=",number1*number2)
        print("El resultado es: ",number1, "-",number2, "=",number1-number2)
        res =0
        for i in range(0,1000):
            res = res+i
       
        fin =time.time()
        tiempo_ejecutado = fin - inicio
        print("el tiempo que tarda en ejecutarse es de :")
        print(tiempo_ejecutado)
       
        
    
    if eleccion == 4:
        print("El resultado es: ",number1, "/",number2, "=",number1/number2)
        res = 0
        for i in range(0,1000):
            res = res+i
       
        fin =time.time()
        tiempo_ejecutado = fin - inicio
        print("el tiempo que tarda en ejecutarse es de :")
        print(tiempo_ejecutado)
       

    if eleccion == 5:
     number1=int(input("ingresa un numero "))
     number2=int(input("ingresa el segundo numero"))

    if eleccion == 6:
        print("gracias por usar el programa :) ")
        