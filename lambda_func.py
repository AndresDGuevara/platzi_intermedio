from functools import reduce

def main():
    
    """ Filter """
    my_list = [1,2,3,4,5,7,9,11,13,16,17,18,19,20,21]
    odd = list(filter(lambda x: x % 2 != 0, my_list))
    print("Odd numbers are: ", odd)

    # # Comprehension
    # my_list = [1,2,3,4,5,7,9,11,13,16,17,18,19,20,21]
    # odd = [i for i in my_list if i % 2 != 0]
    # print(odd)
   
    """ Map """
    my_list2 = [1,2,3,4,5,6,7,8,9,10]
    squares = list(map(lambda x: x ** 2, my_list2))
    print("Square numbers are: ", squares)

    # # Comprehension
    # my_list2 = [1,2,3,4,5,6,7,8,9,10]
    # squares = [i ** 2 for i in my_list2]
    # print(squares)

   
    """ Reduce """
    my_list3 = [2,2,2,2,2]
    all_multiplied = reduce(lambda a, b: a * b, my_list3)
    print("All numbers multiplied are: ", all_multiplied)

    # # Ciclo for
    # my_list3 = [2,2,2,2,2]
    # all_multiplied = 1

    # for i in my_list3:
    #     all_multiplied *= i
    # print(all_multiplied)

if __name__ == '__main__':
    main()