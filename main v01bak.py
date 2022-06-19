from logging import raiseExceptions
import time

from convertARStoUSD import ARStoUSD, convertARStoUSD
from convertUSDtoARS import USDtoARS, convertUSDtoARS

# hay veces que el servidor no responde

# iniciar variables
ARStoUSD
USDtoARS

print(
    """Bienvenido a DolarYa !

Aguarde mientras se carga la aplicación..."""
)

# waiting time
time.sleep(2)

print(
    f"""
El valor del dolar hoy es
==> {ARStoUSD}.

Seleccione que operación desea:

1. Convertir ARS a USD
2. Convertir USD a ARS
"""
)


def swapARStoUSD():
    print("\n")
    monto = abs(float(input("Ingrese el monto por favor: \n")))
    cotizacion = convertARStoUSD(monto)
    print(f"""==> USD$ {cotizacion:,.2f}""")


def swapUSDtoARS():
    print("\n")
    monto = abs(float(input("Ingrese el monto por favor: \n")))
    cotizacion = convertUSDtoARS(monto)
    print(f"""==> ARS$ {cotizacion:,.2f}""")


# elige opcion 1 o 2, si es otra salta error

while True:
    try:
        opcion = int(input())
        print("Su opcion fue ", opcion,"\n")
        break 
    except Exception as e:
        print("Ingrese un monto valido.")
        continue


# funcion de salida

def exitRestart():
    while True:
        opcion = input("Desea seguir el programa ?(y,n)\n").lower()
        if opcion == "y":
            print("Ok, dale gas !")
            return True
        elif opcion == "n":
            return False
        else:
            print("Opcion incorrecta")
        continue
    return 


# ejecutar

def masterSwapper(opcion):
    while True:
        try:

            # swap ARS to USD
            if opcion == 1:
                swapARStoUSD()
                time.sleep(1)
                if exitRestart() == True:
                    continue
                else:
                    break

            # swap ARS to USD
            if opcion == 2:
                swapUSDtoARS()
                time.sleep(1)
                exitRestart()
                if exitRestart() == True:
                    continue
                else:
                    break

            else:  # si hay mala eleccion resetea
                print(
                f"""
Elija 1 o 2:

1. Convertir ARS a USD
2. Convertir USD a ARS
"""
            )
                opcion = int(input())
                continue
        except:
            exitRestart()

masterSwapper(opcion)

# mensaje de salida
print("\nMuchas gracias por usar este programa !\n")
