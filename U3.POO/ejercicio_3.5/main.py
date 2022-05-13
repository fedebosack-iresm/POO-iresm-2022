'''
###**Ejercicio 3.5**
Crear una clase Persona unicamente con metodos estaticos.

Los metodos a crear son:

- calcular_edad, parametro (año_nacimiento)
- calcular_peso_promedio, parametro (estatura,genero) [Ayuda](https://www.zonadiet.com/tablas/pesoideal.cgi)
- calcular_IMC,  parametro (peso,estatura) [Ayuda](https://www.mundodeportivo.com/uncomo/deporte/articulo/como-calcular-el-indice-de-masa-corporal-7050.html)

Crear un menu para probar todos los requerimientos
'''
from libreria import Persona as pe

try:
  peso = int(input("ingrese el peso: "))
  estatura = int(input("ingrese su estatura: "))
except:
  print("Error")

print(f"El IMC = {pe.calcular_IMC(peso,estatura)}")