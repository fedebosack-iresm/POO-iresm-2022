class Persona:
    @staticmethod
    def calcular_IMC(peso,estatura):
        return peso/(estatura/100)**2
    
    @staticmethod
    def calcular_edad(anio_nacimiento):
        return anio_nacimiento