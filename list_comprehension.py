def run():
    # squares = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i ** 2)

    #  para cada i de los numeros del 1 al 100, voy a guardar esa
    # i al cuadrado solamente si no es divisible por 3 
    squares = [i ** 2 for i in range(1, 101) if i % 3 != 0]
    print(squares)

    # lista de todos los multiplos de 4, 6, 9 hasta 5 digitos
    
    # para cada i de los numeros del 1 al 99999, voy a guardar esa
    # i solamente si es multiplo de 4, de 6 y de 9
    multiples = [i for i in range(1, 100000) 
        if i % 4 == 0 and i % 6 == 0 and i % 9 == 0
    ]
    print(multiples)    
    
   
if __name__ == '__main__':
    run()