class ObservadorCargaBateria:

    def update(self, subject):
        print('La carga de la batería es {}'.format(subject.carga))
