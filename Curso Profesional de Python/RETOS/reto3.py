import random

emails:list = ["estuardo@example.com", "lopez@example.com", "facundo@example.com", "edgar@example.com", "gamer123@example.com", "franco@example.com"]
phones: list = ["+e00000000", "+e00000001", "+p00000010", "+s00000101", "+m0000101", "+g0001010"]
datos: list = [1,2,3,4,5,6,7,8,9]
asuntos: list = ["Emergencia", "Trabajo", "Familia", "Escuela", "Tareas", "Empleo"]

def respuesta():
    def chequeo_email(x: int) -> str:
        
        if x == 1:
            veces = random.choice(datos)
            asunto = random.choice(asuntos)
            email = random.choice(emails)
            return f'El correo {email} te ha enviado {veces} correos con nombre de asunto: "{asunto}"'
        elif x == 2:
            veces = random.choice(datos)
            phone = random.choice(phones)
            return f'Tienes {veces} llamadas perdidas del número {phone}'
        else:
            return 'Has introducido un valor incorrecto'
    return chequeo_email

def entrada():
    try:
        entradas = int(input("Ingresa 1 para revisar tu correo o 2 para revisar llamadas perdidas: "))
        funcion = respuesta()
        print(funcion(entradas))
    except ValueError:
        print("Solo puedes ingresar números")

def run():
    entrada()

if __name__ == '__main__':
    run()