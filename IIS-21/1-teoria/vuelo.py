import time

class propelente:
    def __init__(self, pprop=0, nprop="no indicado"):
        self.pprop = pprop
        self.nprop = nprop
    def setPprop(self, pprop):
        self.pprop = pprop
    def getPprop(self):
        return self.pprop
    def setNprop(self, nprop):
        self.nprop = nprop
    def getNprop(self):
        return self.nprop
    def printProp(self):
        print("Info del propelente\nPeso del propelente:"+str(self.pprop)+"\nNombre propelente:"+self.nprop)
    def iterarQuemado(self, prec):
        self.pprop -= 30*prec

class cohete(propelente):
    def __init__(self,peso=500,vel=[0,0],acc=[0,0],pprop=200):
        # falta implementar uso de aceleracion variable
        propelente.__init__(self,pprop=pprop)
        self.peso = peso
        self.vel = vel
        self.acc = acc
    def setPeso(self, peso):
        self.peso = peso
    def getPeso(self):
        return self.peso
    def setVel(self, vel):
        self.vel = vel
    def getVel(self):
        return self.vel
    def setAcc(self, acc):
        self.acc = acc
    def getAcc(self):
        return self.acc
    def printInfo(self):
        print("Cohete de ejemplo\n\nPeso:"+str(self.peso)+"\nVelocidad en x:"+str(self.vel[0])+"\nVelocidad en y:"+str(self.vel[1]))
        self.printProp()
    def iterarVuelo(self, prec):
        pprop = self.pprop
        self.iterarQuemado(prec)
        self.peso -= pprop - self.pprop
        # toma aceleracion constante [10,3]
        self.vel = [self.vel[0]+1*prec,self.vel[1]+2*prec]
