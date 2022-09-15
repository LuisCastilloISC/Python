import Rectangulo as figuras

miRectangulo=figuras.Rectangulo(5,10)
miRectangulo.Ancho=14
miRectangulo._largo=20
print(miRectangulo.Ancho)
print(miRectangulo._largo)
print(miRectangulo.CalcularArea())
print(miRectangulo.Perimetro())
miCuadrado = figuras.Cuadrado(5)
miCuadrado2=figuras.Cuadrado(6)
print(id(miCuadrado))
print(id(miCuadrado2))
print(miCuadrado.Area())
print(miCuadrado2.Area())