def conversor(tipo_pesos, valor_dolar):
    quetzales = input("¿Cuantos Pesos "+tipo_pesos+" tienes?: ")
    quetzales = float(quetzales)

    dolares = quetzales / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dolares" )


menu = """
Bienvenido al conversor de monedas <3

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Quetzales

Elige una opción: 
"""
opcion = int(input(menu))

if opcion == 1:
    conversor("colombiano", 3943.02)
elif opcion == 2:
    conversor("argentinos", 105.19)
elif opcion == 3:
    conversor("quetzales", 7.87)
else:
    print("Ingresa una opción correcta.")
