class ObservadorTiempoBateria:
    def update(self, subject):
        print('A la batería le queda {} minutos de carga'.format(subject.tiempo))