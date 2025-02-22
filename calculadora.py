def menu():
    return int(input("Bienvenido a la calculadora:\n"
       "Operaciones\n"
       "1. Sumar\n"
       "2. Restar\n"
       "3. Multiplicar\n"
       "4. Dividir\n"
       "5. Salir\n"
       "¿Qué desea realizar?: "))

add_lambda = lambda a, b: a + b
subs_lambda = lambda a, b: a - b
mult_lambda = lambda a, b: a * b
div_lambda = lambda a, b: a / b

def calculadora():
    while True:
        opc = menu()
        if opc == 5:
            break
        if opc in [1,2,3,4]:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            if opc == 1:
                print(f"la suma es: {add_lambda(a, b)}  \n")
            elif opc == 2:
                print(f"la resta es: {subs_lambda(a, b)}  \n")
            elif opc == 3:
                print(f"la multiplicación es: {mult_lambda(a, b)} \n")
            elif opc == 4:
                print(f"la división es: {div_lambda(a, b)} \n")
        else: 
            print("¡Opción no válida! \n \n")

calculadora()