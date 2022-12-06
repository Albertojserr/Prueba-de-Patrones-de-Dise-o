from subject import Subject
from observadorcargabateria import ObservadorCargaBateria
from bateria import Bateria
from obstiempobateria import ObservadorTiempoBateria


def main():
    obj1 = Bateria(True, True, 90, 50)
    obj2 = Bateria(True, True, 90, 100)

    view1 = ObservadorCargaBateria()
    view2 = ObservadorTiempoBateria()

    obj1.attach(view1)
    obj1.attach(view2)

    obj2.attach(view1)
    obj2.attach(view2)

    obj1.carga = 10
    obj2.carga = 15

if __name__ == "__main__":
    main()
