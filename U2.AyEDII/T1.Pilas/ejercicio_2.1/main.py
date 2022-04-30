"""
INVESTIGAR
importancia de las pilas en la informatica
que son pilas dinamicas y estaticas
investigar cuando puede ocurrir un desbordamiento de pilas

"""

"""
Ejercicio 2.1
Utilizando la clase Pila y sus metodos

Dada una pila de letras determinar cuántas vocales contiene.
"""

import Gestor as ge
gestor=ge.Gestor()
while True:
    opcion=input("""\nSeleccione una opcion:
    1- Ingresar una letra a la PILA
    2- Ver Cima de la PILA
    3- Recorrer los datos de la PILA
    4- Contar cantidad de VOCALES en la PILA
    5- Eliminar un elemento de la PILA
    
    0- Salir
    
    -------> """)

    if opcion=="1":
        gestor.ingresar()
    elif opcion=="2":
        gestor.ver_cima()
    elif opcion=="3":
        gestor.ver()
    elif opcion=="4":
        gestor.contar_vocales()
    elif opcion=="5":
        gestor.eliminar_elemento()
    elif opcion=="0":
        break
    else:
        print("Opcion Incorrecta.")

