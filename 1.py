"""
Ejercicio 1:

El diseño que vamos a elegir es el siguiente, tendremos una clase abstracta que será Base, que tendrá su nombre y dos métodos a implementar
 (cantidad de ambulancias y tiempo medio de respuesta).

De ella se desprenderán dos subclases, la BaseSimple y la BaseCompuesta.
La BaseSimple se inicializará con el nombre, tiempo medio de respuesta y cantidad de ambulancias.

Las BaseCompuesta se inicializará con el nombre y una lista de bases


"""

from abc import ABC, abstractmethod


class Base(ABC):

    @abstractmethod
    def cantidad_ambulancias(self):
        pass

    @abstractmethod
    def tiempo_respuesta_media(self):
        pass


class BaseSimple(Base):
    def __init__(self, nombre: str, ambulancias: int, tiempo_respuesta: int):
        self.nombre = nombre
        self.ambulancias = ambulancias
        self.tiempo_respuesta = tiempo_respuesta

    def cantidad_ambulancias(self):
        return self.ambulancias

    def tiempo_respuesta_media(self):
        return self.tiempo_respuesta


class BaseCompuesta(Base):
    def __init__(self, nombre: str, bases: list[Base]):
        self.nombre = nombre
        self.bases = bases

    def cantidad_ambulancias(self):
        ambulancias = 0
        for base in self.bases:
            ambulancias += base.cantidad_ambulancias()
        return ambulancias

    def tiempo_respuesta_media(self):
        tiempo_respuesta = 0
        for base in self.bases:
            tiempo_respuesta += base.tiempo_respuesta_media()
        return tiempo_respuesta / len(self.bases)


if __name__ == "__main__":
    base1 = BaseSimple("A", 5, 50)
    base2 = BaseSimple("B", 4, 40)
    base3 = BaseCompuesta("C", [base1, base2])
    print(base1.cantidad_ambulancias())
    print(base2.cantidad_ambulancias())
    print(base3.cantidad_ambulancias())
    print(base1.tiempo_respuesta_media())
    print(base2.tiempo_respuesta_media())
    print(base3.tiempo_respuesta_media())
