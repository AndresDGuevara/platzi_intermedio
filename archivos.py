def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f: # encoding para evitar errores con caracteres extraños
        for line in f:
            numbers.append(int(line))
        print(numbers)


def write():
    names = ["Violeta", "Mario", "Karla", "Carlos", "Sophia", "Andrés"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name) # write para escribir cada uno de los nombres
            f.write("\n")

def run():
    write()


if __name__ == '__main__':
    run()