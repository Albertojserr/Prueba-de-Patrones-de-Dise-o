from Isensor import *
from zope.interface import implementer

@implementer(ISensor)
class Sensor(object):
    def __init__(self, nombre):
        self.nombre=nombre
        self.umbral=0
        self._valor=0
    def comprobar(self):
        self.diferencia=self._valor/self.umbral
        return self.diferencia
    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self,valor :int):
        self._valor=valor
