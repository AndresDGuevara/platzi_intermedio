#recibe un numero como parametro y retornar una lista con todos los numeros divisores de ese numero
def divisors(num):
    try:
        if num < 0:
            raise ValueError("Oops!  sin numeros negativos. ")
        else:
            divisors = [i for i in range(1, num + 1) if num % i == 0]
            return divisors

    except ValueError as ve:
        print(ve)
        return f"{num} no es un numero positivo"

def run():
    try:
        num = int(input("Ingresa un numero: "))
        try:
            print(divisors(num))
            print("Termino mi programa")
            if num == 0:
                raise ZeroDivisionError("Es un cero")
        except ZeroDivisionError as e:
            print(e)
            return ""     
    except ValueError:
        print("Ingresa solo numeros")
   
 
if __name__ == '__main__':
    run()

# try:
#     length = int(input("Enter a positive integer: "))
#     width = int(input("Enter a second positive integer: "))
#     print(lenght / width)
# except Exception:
#     print("division by zero is invalid! kindly change your input")