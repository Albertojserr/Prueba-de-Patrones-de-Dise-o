from zope.interface import Interface

class ISensor(Interface):

    def comprobar(self):
        """Devuelve el valor de peligro"""
    def setValor(self):
        """Establece un nuevo valor de peligro"""