from src.tablaAsignacion import TablaAsignacion


class Dni:
    def __init__(self, cadena=""):
        self.dni = cadena
        self.numero_sano = False
        self.letra_sana = False
        self.tabla = TablaAsignacion()

    def setDni(self, cadena):
        self.dni = cadena
        self.numero_sano = False
        self.letra_sana = False

    def getDni(self):
        return self.dni

    def getNumeroSano(self):
        return self.numero_sano

    def getLetraSana(self):
        return self.letra_sana

    def checkCIF(self):
        numero_ok = self.checkDni()
        letra_ok = self.checkLetra()
        self._setLetraSana(letra_ok)
        return numero_ok and letra_ok

    def checkDni(self):
        self._setNumeroSano(False)
        if not self._checkLength():
            return False
        if not self._checkNumber():
            return False
        self._setNumeroSano(True)
        return True

    def checkLetra(self):
        if self.getNumeroSano():
            resultado = self.getParteAlfabeticaDni() == self.obtenerLetra()
            self._setLetraSana(resultado)
            return resultado
        self._setLetraSana(False)
        return False

    def obtenerLetra(self):
        if self.getNumeroSano():
            return self.tabla.calcularLetra(self.getParteNumericaDni())
        return None

    def getParteNumericaDni(self):
        if self.getNumeroSano():
            return self.getDni()[:-1]
        return False

    def getParteAlfabeticaDni(self):
        return self.getDni()[-1]

    def _setNumeroSano(self, valor):
        self.numero_sano = valor

    def _setLetraSana(self, valor):
        self.letra_sana = valor

    def _checkLength(self):
        return len(self.getDni()) == 9

    def _checkNumber(self):
        return self.getDni()[:-1].isdigit()
