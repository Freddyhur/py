import os

def Temperaturas():
    print ("--- Opción de Temperaturas ---")
    veces=int(input("Cuantas temperaturas ingresa ?: "))
    sum=0
    for x in range(veces):
        tempe=float(input("Ingrese temperatura: "))
        suma=suma+tempe
    print("El promedio es: " , round((suma/veces),2))


def Personas():
     print ("--- Opción de Datos de Personas ---")


seguir=True
while seguir:
    os.system('cls')
    print ("1. Temperaturas")
    print ("2. Datos de Personas")
    print ("3. Salir ")
    op=int(input("ingrese opcion= "))
    if(op==1):
        Temperaturas()
    if(op==2)
        Personas()
    if(op==3)
        print("Programa fin")
        break