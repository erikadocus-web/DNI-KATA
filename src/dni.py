from .tablaAsignacion import tablaAsignacion

class dni:
    def __init__(self, cadena=""):
        self.dni = cadena
        self.numeroSano = False
        self.letraSana = False
        self.tabla = tablaAsignacion()

    def getDni(self):
        return self.dni 
    
    def getNumeroSano(self):
        return self.numeroSano
    
    def getLetraSana(self):
        return self.letraSana