menu = """
Bienvenido al conversor de monedas <3

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Quetzales

Elige una opción: 
"""
opcion = int(input(menu))

if opcion == 1:
    quetzales = input("¿Cuantos Pesos Colombianos tienes?: ")
    quetzales = float(quetzales)
    valor_dolar = 3943.02
    dolares = quetzales / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dolares" )
elif opcion == 2:
    quetzales = input("¿Cuantos Pesos Argentinos tienes?: ")
    quetzales = float(quetzales)
    valor_dolar = 105.19
    dolares = quetzales / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dolares" )
elif opcion == 3:
    quetzales = input("¿Cuantos quetzales tienes?: ")
    quetzales = float(quetzales)
    valor_dolar = 7.77
    dolares = quetzales / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dolares" )
else:
    print("Ingresa una opción correcta.")
