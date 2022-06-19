if opcion == 1:
    print("\n")
    print("Ingrese el monto por favor:")
    monto = float(input())
    cotizacion = convertUSDtoARS(monto)
    print(f"""$ {cotizacion:,.4f}""")
elif opcion == 2:
    print("\n")
    print("Ingrese el monto por favor:")
    monto = float(input())
    cotizacion = convertARStoUSD(monto)
    print(f"""$ {cotizacion:,.2f}""")
else:
    print("Seleccion incorrecta, elija 1 o 2.")

   finally:
        print("Seleccion incorrecta, elija 1 o 2:")
        opcion = int(input())
        # break
        # pass
