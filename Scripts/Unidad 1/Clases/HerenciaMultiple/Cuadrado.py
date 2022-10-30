from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Cuadrado(FiguraGeometrica,Color):
    def __init__(self, color,lado) -> None:
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)
        
    def CalcularArea(self):
        return self.alto*self.ancho