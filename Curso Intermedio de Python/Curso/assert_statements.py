def divisor(num):
    divisors =[]
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors
   

def run():

    num = input("Ingresa un numero: ")
    assert num.isnumeric() and num > 0, "Debes ingresar un numero positivo"
    print(divisor(int(num)))
    print("Termino")
    

if __name__ == "__main__":
    run()