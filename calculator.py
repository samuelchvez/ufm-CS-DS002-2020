print('''
1. Sumar
2. Restar
3. Multiplicar
''')

option = int(input("Ingrese una opcion del menu: "))

if option not in [1, 2, 3]:
    print("Opcion invalida")
else:
    first_value = float(input("Ingrese el primer valor: "))
    second_value = float(input("Ingrese el segundo valor: "))
    if option == 1:
        print ("Resultado {}".format(first_value + second_value))
    elif option == 2:
        print ("Resultado {}".format(first_value - second_value))
    elif option == 3:
        print ("Resultado {}".format(first_value * second_value))
