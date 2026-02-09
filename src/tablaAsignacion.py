class TablaAsignacion:

    def __init__(self):
        self.tabla = ["T","R","W","A","G","M","Y","F","P","D","X","B",
                      "N","J","Z","S","Q","V","H","L","C","K","E"]
        
    def getTabla(self):
        return self.tabla
    

    def getLetra(self, posicion):
        
        if posicion < len(self.tabla): 
            return self.tabla[posicion]
        else:
            return "Posicion letra fuera de rango"
        
    def getModulo(self):
        return len(self.tabla)
    
    def isLetraPermitida(self, letra):
        return letra in self.tabla