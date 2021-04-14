def palindrome(string): # Utilizando raise
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacia")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

try:
    print(palindrome(**))
except TypeError:
    print("Solo se pueden ingresas strings")

""" utilizando la palabra finally """
# se utiliza para cerrar un archivo dentro de python
# Cerrar una conexion a una base de datos
# Liberar recursos externos
# Generalmente no se usa pero hay tener el conocimiento
try: 
    f = open("archivo.txt") # Hacer cualquier cosa con nuestro archivo
finally:
    f.close()
