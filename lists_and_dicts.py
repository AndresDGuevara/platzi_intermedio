def run():
    # my_list = [1, "Hello", True, 4.5]
    # my_dict = {"firstname": "Andres", "lastname": "Guevara"}

    # Lista de diccionarios
    super_list = [
        {"firstname": "Cristian", "lastname": "Guevara"},
        {"firstname": "Stella", "lastname": "Aguirre"},
        {"firstname": "Carlos", "lastname": "Santana"},
        {"firstname": "Max", "lastname": "Cavalera"},
        {"firstname": "Dave", "lastname": "Grol"},
    ]

    # Diccionario de listas
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43],
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    # for value in super_list: # print the list as it is
    #     print(value)

    for i in super_list:
        print(i["firstname"], ",", i["lastname"])


if __name__ == '__main__':
    run()