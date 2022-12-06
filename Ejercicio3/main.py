from sensor import Sensor
from alarma import Alarma
from sensor_tipos import SensorHumo, SensorTemperatura, SensorPresion
import random
import time


def main():
    Humo=SensorHumo()
    Temperatura=SensorTemperatura()
    Presion=SensorPresion()
    alarma=Alarma()
    alarma.addSensor(Humo)
    alarma.addSensor(Temperatura)
    alarma.addSensor(Presion)
    seguir='si'
    while seguir=='si':
        for i in range(random.randint(1,10)):
            for sensor in alarma.sensores:
                max=int(sensor.umbral*1.2)
                min=int(sensor.umbral*0.8)
                sensor.valor=random.randint(min,max)
            alarma.comprobar()
            time.sleep(2)
        seguir=input("Desea seguir? Si/No ").lower()

if __name__=="__main__":
    main()