
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