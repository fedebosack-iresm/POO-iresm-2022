import Clases as cl

pila=cl.Pila()
lista_vocales=["a","e","i","o","u","A","E","I","O","U"]
class Gestor:
    
    def ingresar(self):
        while True:
            letra=input("Ingrese una LETRA o 0 para Salir: ")
            if letra.isalpha()==True and len(letra)==1:
                pila.apilar(letra)
                print(f"\nSe agrego ->{letra}<- a la pila.")
            elif letra=="0":
                break
            else:
                print("\nSolo se admiten LETRAS y de a 1 por vez!")
                
    def eliminar_elemento(self):
        if pila.get_tamanio()==0:
            print("\nPila Vacia")
            return
        print("\n::::::PILA ACTUAL::::::\n")
        pila.ver_pila()
        lista_desapilada=[]
        antigua_pila=pila.contenido_pila()
        letra_a_eliminar=input("\nIngrese la Letra que desea elimnar de la pila: ")
        if letra_a_eliminar in antigua_pila:
            for i in reversed(antigua_pila):
                if i !=letra_a_eliminar:
                    lista_desapilada.append(pila.desapilar())
                elif i==letra_a_eliminar:
                    pila.desapilar()
                    break
            if len(lista_desapilada) >0:
                for i in reversed(lista_desapilada):
                    pila.apilar(i)
            print("\nElemento Eliminado con Exito!")
            print("\n::::::PILA ACTUALIZADA::::::\n")
            pila.ver_pila() 
        else:
            print(f"El elemento | {letra_a_eliminar} | NO se encuentra en la pila")   
                
    def contar_vocales(self):
        if pila.get_tamanio() ==0:
            print("\nPila Vacia")
            return
        cont=0
        lista_desapilada=[]
        for i in reversed(pila.contenido_pila()):
            if i in lista_vocales:
                cont+=1
                lista_desapilada.append(i)
                pila.desapilar()
            else:
                lista_desapilada.append(i)
                pila.desapilar()
        for i in reversed(lista_desapilada):
            pila.apilar(i)
        print(f"\nLa Pila contiene {cont} vocales.")
    
    def ver(self):
        if pila.get_tamanio() ==0:
            print("\nPila Vacia")
            return
        pila.ver_pila()
    
    def ver_cima(self):
        if pila.get_tamanio() ==0:
            print("\nPila Vacia")
            return
        print(f"\nLa cima de la pila es el elemento | {pila.get_cima()} |")
    
    