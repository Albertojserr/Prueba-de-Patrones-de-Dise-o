from subject import Subject

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