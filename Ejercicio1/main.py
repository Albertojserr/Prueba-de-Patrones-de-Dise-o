from base import Base
from basecompuesta import BaseCompuesta
from basesimple import BaseSimple


def main():
    base1 = BaseSimple("A", 5, 50)
    base2 = BaseSimple("B", 4, 40)
    base3 = BaseCompuesta("C", [base1, base2])
    print(base1.cantidad_ambulancias())
    print(base2.cantidad_ambulancias())
    print(base3.cantidad_ambulancias())
    print(base1.tiempo_respuesta_media())
    print(base2.tiempo_respuesta_media())

if __name__ == "__main__":
    main()
