class Alarma(object):
    def __init__(self):
        self.sensores=[]
    def addSensor(self,sensor):
        self.sensores.append(sensor)
    def comprobar(self):
        peligro=0
        for sensor in self.sensores:
            peligro+=float(sensor.comprobar())
        if float(peligro/len(self.sensores))>1:
            print("ALARMA!!!")
        else:
            print("Todo OK")