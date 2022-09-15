
class Rectangulo:
    def __init__(self,ancho,largo) -> None:
        self._ancho=ancho
        self._largo=largo
    @property
    def Ancho(self):
        return self._ancho
    @Ancho.setter
    def Ancho(self,a):
        if(a<15):
            print("Ancho invalido")
        else:
            self._ancho=a
    def CalcularArea(self):
        return self._ancho*self._largo
    def Perimetro(self):
        return 2*(self._ancho+self._largo)


class Cuadrado:
    def __init__(self,lado) -> None:
        self._lado = lado
    def Area(self):
        return self._lado*self._lado
    def Perimetro(self):
        return self._lado *4   
