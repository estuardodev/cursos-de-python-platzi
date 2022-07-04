def read():
    numbers = []
    with open(r"C:\Users\Estuardo\Documents\Cursos\cursos-de-python-platzi\Curso Intermedio de Python\Curso\archivos\numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Estuardo", "Daniel", "Luis"]
    with open (r"C:\Users\Estuardo\Documents\Cursos\cursos-de-python-platzi\Curso Intermedio de Python\Curso\archivos\names.txt", "w", encoding="utf-8") as f:
        for name  in names:
            f.write(name)
            f.write("\n")

def run():
    
    read()
    write()
    

if __name__ == '__main__':
    run()