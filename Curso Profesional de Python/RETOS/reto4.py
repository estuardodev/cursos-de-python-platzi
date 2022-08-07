def remove_duplicate(lista):
    return list(set(lista))
    

def run():
    lista = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,36,3,3,3,4,4,5,4,4]
    print(remove_duplicate(lista))

if __name__ == '__main__':
    run()