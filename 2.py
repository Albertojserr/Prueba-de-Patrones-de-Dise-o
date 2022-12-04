class Subject:
    """Representa lo que se observa"""

    def __init__(self):
        self._observers = []

    def notifica(self):
        for observer in self._observers:
            observer.update(self)

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass


class Bateria(Subject):

    def __init__(self, conectado, cargando, carga, tiempo):
        Subject.__init__(self)
        self.name = conectado
        self.cargando = cargando
        self._carga = carga
        self._tiempo = tiempo

    @property
    def carga(self):
        return self._carga

    @carga.setter
    def carga(self, value):
        self._carga = value
        self.notifica()

    @property
    def tiempo(self):
        return self._tiempo

    @tiempo.setter
    def tiempo(self, value):
        self._tiempo = value
        self.notifica()


class ObservadorCargaBateria:

    def update(self, subject):
        print('La carga de la batería es {}'.format(subject.carga))


class ObservadorTiempoBateria:

    def update(self, subject):
        print('A la batería le queda {} minutos de carga'.format(subject.tiempo))


if __name__ == "__main__":
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
