# option = -1
# while option != 4:
#     print('''
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Salir
#     ''')

#     option = int(input("Ingrese una opcion del menu: "))

#     if option not in [1, 2, 3]:
#         print("Opcion invalida")
#     else:
#         first_value = float(input("Ingrese el primer valor: "))
#         second_value = float(input("Ingrese el segundo valor: "))
#         if option == 1:
#             print ("Resultado {}".format(first_value + second_value))
#         elif option == 2:
#             print ("Resultado {}".format(first_value - second_value))
#         elif option == 3:
#             print ("Resultado {}".format(first_value * second_value))






def binary(name, oper):
    print("Bienvenido, hoy vamos a hacer la operacion binaria: {}".format(name))
    first_value = int(input("Ingrese el primer valor: "))
    second_value = int(input("Ingrese el segundo valor: "))
    return oper(first_value, second_value)































