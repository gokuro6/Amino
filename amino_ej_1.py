# -*- coding: utf-8 -*-
'''Hacer funciones una que sume, otra que reste, multiplique y divida dos numeros y retornen los resultados, no reciben parametros.
crear funcion datos que pidan los numeros al usuario y se almacenen en variables globales
si llamo a una funcion sin haber introducido primero los datos tiene que pedirme los datos, si ya he introducido los datos ya no me lo tiene que volver a pedir
si llamo a la funcion datos dos veces no tiene que dejarme volver a introducirlo.'''

num_1 = 0
num_2 = 0
data_fill = False

def pedir_datos():
    global data_fill
    global num_1
    global num_2
    if not data_fill:
        num_1 = input("Primer Numero: ")
        print ("---------------------------------")
        num_2 = input("Segundo Numero: ")
        print ("---------------------------------")
        print ("Numero : {} --- Numero : {}").format(num_1,num_2)
        data_fill = True
    else:
        print ("---------------------------------")
        print ("Ya han sido asignados los datos")

def suma():
    if not data_fill:
        pedir_datos()
        resultado = num_1 + num_2
    else:
        resultado = num_1 + num_2
    return resultado

def resta():
    if not data_fill:
        pedir_datos()
        resultado = num_1 - num_2
    else:
        resultado = num_1 - num_2
    return resultado

def multiplicacion():
    if not data_fill:
        pedir_datos()
        resultado = num_1 * num_2
    else:
        resultado = num_1 * num_2
    return resultado

def division():
    if not data_fill:
        pedir_datos()
        resultado = num_1 / num_2
    else:
        resultado = num_1 / num_2
    return resultado

def main():
    menu = 1
    while menu >= 1 and menu <= 5:
        print ("---------------------------------")
        print ("              Menu:")
        print ("---------------------------------")
        print ("1. Asignar valores")
        print ("2. Suma")
        print ("3. Resta")
        print ("4. Multiplicacion")
        print ("5. Division")
        print ("Otro. Salir")
        print ("---------------------------------")
        menu = input("Seleccione una opcion: ")
        if menu == 1:
            pedir_datos()
        elif menu == 2:
            print ("---------------------------------")
            print ("La Suma de los numeros es: {}").format(suma())
        elif menu == 3:
            print ("---------------------------------")
            print ("La Resta de los numeros es: {}").format(resta())
        elif menu == 4:
            print ("---------------------------------")
            print ("La Multiplicacion de los numeros es: {}").format(multiplicacion())
        elif menu == 5:
            print ("---------------------------------")
            print ("La Multiplicacion de los numeros es: {}").format(division())
        else:
           print ("---------------------------------")
           print ("Saliendo del Script...")

if __name__ == '__main__':
    main()
