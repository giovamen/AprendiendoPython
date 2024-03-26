#concatena dos cadenas de texto

string1 = "Hello"
string2 = "World"
result = string1 + " " + string2
print(result)

#En este ejemplo, tenemos dos cadenas y las concatenamos usando el operador. También agregamos un espacio entre las dos cadenas usando otro operador.string1string2++También puede utilizar el método para concatenar cadenas. He aquí un ejemplo:.format()



string1 = "Hello"
string2 = "World"
result = "{} {}".format(string1, string2)
print(result)

def add_numbers(num1, num2):
    """
    Esta función suma dos números y devuelve la suma
    :p aram num1: primer número
    :p aram num2: segundo número
    :return: suma
    """
    return num1 + num2

print(add_numbers(2, 3))