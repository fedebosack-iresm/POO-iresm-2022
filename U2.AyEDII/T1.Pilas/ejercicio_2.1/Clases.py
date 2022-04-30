
class Pila:
    def __init__(self): #CREA UNA PILA DINAMICA AL NO SOLICITAR UN LIMITE DE TAMAÑO
        self.items=[]
    
    def apilar(self, x): #APILA UN ELEMENTO EN LA PILA
        self.items.append(x)
        
    def desapilar(self): #DESAPILA EL ULTIMO ELEMENTO ALMACENADO EN LA PILA
        try:
            return self.items.pop()
        except: #si la pilla llegase a estar vacia, envia un msj de informacion
            print("\nPila vacía")
        
    def contenido_pila(self): #RETORNA EL CONTENIDO DE LA PILA EN UNA VARIABLE
        contenido_pila=self.items
        return contenido_pila
    
    def ver_pila(self): #ITERA SOBRE LA PILA y RETORNA CADA VALOR
        cont=0
        for i in reversed(self.items):
            cont+=1
            print(f"|  {i}  |")

    def get_tamanio(self): #RETORNA EL TAMAÑO DE LA PILA
        return len(self.items)
    
    def get_cima(self): #RETORNA EL ULTIMO ELEMENTO ALMACENADO EN LA PILA
        return self.items[-1]
    