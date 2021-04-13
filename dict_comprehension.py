import math

def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i ** 3

    # print(my_dict)
    
    # para cada numero del 1 al 100 voy a guardar ese numero como llave
    # y ese numero elevado al cubo como valor, si ese numero 
    # no es divisible entre 3 
    my_dict = {i: i ** 3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict)

    # para cada numero natural del 1 al 1000 voy a guardar ese numero 
    # como llave y ese numero con su raiz cuadrada como valor
    root_dict = {i: math.sqrt(i) for i in range(1, 1001)}
    print(root_dict)
      

if __name__ == '__main__':
    run()