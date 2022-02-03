def run():
    #for contador in range (100):
    #    if contador % 2 != 0:
    #        continue
    #    print(contador)

    #for i in range(100):
    #    print(i)
    #    if i == 50:
    #        break

    #texto = input("Escribe un texto: ")
    #for letra in texto:
    #    if letra == "o":
    #        break
    #    print(letra)

    # RETO
    numero = int(input("Ingresa un numero: "))
    while numero:
        if numero == 6:
            print("GANASTE")
            break
        if numero != 6:
            print("Lo siento")
            break
            

if __name__ == "__main__":
    run()