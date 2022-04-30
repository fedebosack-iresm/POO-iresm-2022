"""###Ejercicio 2.10
1. Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y 
    un número entero positivo dado. (SIN RECURSION)

2. Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y
    un número entero positivo dado. (CON RECURSION)
"""
def suma_numeros(numero):
    suma = 0
    for i in range(numero+1):
        suma+=i
    return suma

print(f"Suma de numeros de 0 a 5: {suma_numeros(5)}")

def suma_numeros_recursivo(numero):
    if numero == 0:
        return 0
    else:
        return numero + suma_numeros_recursivo(numero-1)
    
print(f"Suma de numeros recursivos de 0 a 5: {suma_numeros_recursivo(5)}")