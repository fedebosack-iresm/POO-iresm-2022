def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print (numero)
        cuenta_regresiva(numero)
    else:
        print ("Boooooooom!")
    
    
    print ("Fin de la función", numero)
    
cuenta_regresiva(5)