from sensor import Sensor

class SensorHumo(Sensor):
    def __init__(self):
        Sensor.__init__(self,"Sensor humo")
        self.umbral=20

class SensorTemperatura(Sensor):
    def __init__(self):
        Sensor.__init__(self,"Sensor temperatura")
        self.umbral=47

class SensorPresion(Sensor):
    def __init__(self):
        Sensor.__init__(self,"Sensor presion")
        self.umbral=40