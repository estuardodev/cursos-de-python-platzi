from time import sleep

def fibo_gen(n):
    n1: int = 0
    n2: int = 1
    counter: int = 0
    vuelta = 0

    while True:
        if vuelta != n:
            vuelta += 1    
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                aux = n1 + n2
                n1, n2 = n2, aux
                counter += 1
                yield aux
        else:
            break

if __name__ == '__main__':
    entrada = int(input("Ingrese el número de números a imprimir: "))
    fibonacci = fibo_gen(entrada)
    for element in fibonacci:
        print(element)
        sleep(1)