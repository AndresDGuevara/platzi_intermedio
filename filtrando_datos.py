DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    # Detodos los trabajadores en DATA voy a guardar el nombre de ese trabajador, 
    # solo si domina el lenguaje Python
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    
    # traer todos los workers que trabajan en platzi
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    
    # Flitrar los trabajadores mayores de edad
    # pero con esta funcion nos trae todo el diccionario completo de las personas mayores
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))

    # utilizamos map para mapear la variable anterior y que solo nos traiga los nombres de las personas mayores
    #aqui sobre-escribimos la variable adults
    adults_names = list(map(lambda worker: worker["name"], adults))
    

    # crear una nueva lista de diccionarios pero que en lugar de tener las llaves que ya conociamos, 
    # tengamos una llave mas, una llave old que va a tener True or False si la persona es mayor a 70 años o menor 

    # Entonces tengo un list que me transforma en una lista el resultado de aplicar la funcion map 
    # (transformar a cada uno de los diccionarios que ya tenemos en un diccionario nuevo que es la combinacion 
    # de nuestro diccionario original con un nuevo diccionario que simplemente tiene la 
    # llave old que va a arrojar True si hay personas mayores a 70 o False si no es asi )
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    for worker in old_people:
        print(worker)

if __name__ == '__main__':
    run()