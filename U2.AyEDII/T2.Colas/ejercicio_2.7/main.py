
"""
###Ejercicio 2.7
Utilizando la clase Cola y sus metodos
*   Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.
"""
def son_primos(numero):
    divisores=0
    for i in range(1, numero+1):
        if numero % i == 0:
            divisores+=1
    if divisores==2:
        return True #El N° SI es PRIMO
    else:
        return False #El N° NO es PRIMO
    
import ClaseCola_2 as co

cola_1 = co.Cola()

cola_1.encolar(1)
cola_1.encolar(2)
cola_1.encolar(3)
cola_1.encolar(4)
cola_1.encolar(5)
cola_1.encolar(6)
cola_1.encolar(7)
cola_1.encolar(8)
cola_1.ver_cola()

for i in range(cola_1.get_tamanio()):
    numero = cola_1.desencolar()
    if son_primos(numero):
        cola_1.encolar(numero)

cola_1.ver_cola()

