def divisor(num):
    divisors =[]

    try:
        if num < 0:
            raise ValueError("Ingresaste un numero negativo")
        else:
            for i in range(1, num + 1):
                if num % i == 0:
                    divisors.append(i)
            return divisors
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisor(num))
        print("Termino")
    except ValueError:
        print("Error, ingresaste un caracter incorrecto")

if __name__ == "__main__":
    run()