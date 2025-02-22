try:
    divisor = int(input("Ingresa un número divisor: "))
    result = 100 / divisor
    print(result)
except:
    print("Error: rl dividor no puede ser cero.")

try:
    divisor = int(input("Ingresa un número divisor: "))
    result = 100 / divisor
    print(result)
except ZeroDivisionError:
    print("Error: el dividor no puede ser cero.")

try:
    divisor = int(input("Ingresa un número divisor: "))
    result = 100 / divisor
    print(result)
except ZeroDivisionError as e:
    print("Error, el dividor no puede ser cero.")
    print("Ha ocurrido un error: ", e)
except ValueError as e:
    print("Error, debe introducir un número válido.")
    print("Ha ocurrido un error: ", e)



