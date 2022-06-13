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
    print("Ingrese el monto por favor:")
    monto = float(input())
    cotizacion = convertARStoUSD(monto)
    print(f"""==> USD$ {cotizacion:,.2f}""")


def swapUSDtoARS():
    print("\n")
    print("Ingrese el monto por favor:")
    monto = float(input())
    cotizacion = convertUSDtoARS(monto)
    print(f"""==> ARS$ {cotizacion:,.2f}""")


# elige opcion 1 o 2, si es otra salta error
opcion = int(input())

# ejecutar

"""
creo que hay q hacer una funcion q sea la de masterswapper
donde ejecuta los swaps
si falla el input de opcion
raisea el error y da la chance de elegir devuelta ?
o capaz no sea exeption sino otro tipo de error mas generico ?
"""


def masterSwapper(opcion):
    i = True
    while i == True:
        try:
            # swap ARS to USD
            if opcion == 1:
                swapARStoUSD()
                time.sleep(1)
                raise Exception()
            # swap ARS to USD
            if opcion == 2:
                swapUSDtoARS()
                time.sleep(1)
                raise Exception()
            else:  # si hay mala eleccion resetea
                raise Exception()
        except Exception:
            print(
                f"""
Elija 1 o 2:

1. Convertir ARS a USD
2. Convertir USD a ARS
"""
            )
            opcion = int(input())


masterSwapper(opcion)

# mensaje de salida
print("\nMuchas gracias por usar este programa !")
