#TIPOS DE DATOS
#Numericos
#Integer
integer = 1
integerNegative = -1
zero = 0
print(type(integer),integer,id(integer),type(integerNegative),integerNegative,id(integerNegative),type(zero),zero,id(zero))
#Float
floatNum=3.5
floatNumNegative = -3.9
floatNumZero = 3.0
print(type(floatNum),floatNum,id(floatNum),type(floatNumNegative),floatNumNegative,id(floatNumNegative),type(floatNumZero),floatNumZero,id(floatNumZero))
#Complex
complexNum = 5j
complexNum2= 2 + 4j
print(type(complexNum),complexNum,id(complexNum),type(complexNum2),complexNum2,id(complexNum2))
#Conversiones
intToFloat = float(integer)
floatToInt = int(floatNum)
floatToComplex = complex(floatNumNegative)
print(type(intToFloat),intToFloat,id(intToFloat),type(floatToInt),floatToInt,id(floatToInt),type(floatToComplex),floatToComplex,id(floatToComplex))

#BOOLEANOS
# Regresa falso si X no es igual que Y
x = 5
y = 10
print(bool(x==y)) 
# Regresa falso si X es None(NULL)
x = None
print(bool(x))
# Regresa Falso si X es una secuencia vacia
x = ()
print(bool(x))
# Regresa Falso si X es un Diccionario Vacio
x = {}
print(bool(x))
# Regresa Falso al ser X 0
x = 0.0
print(bool(x))
# Regresa verdadero al no ser X una cadena vacia
x = 'EstaNoEsUnaCadenaVacia:D'
print(bool(x))

#CADENAS
#Impresion Normal
print(type("Hello"),"Hello")
#Cadenas en variables
saludo = "Hola buenos dias"
print(type(saludo),saludo,id(saludo))
despedida = "Adios Tenga buen dia"
print(type(despedida),despedida,id(despedida))
#Tipos de impresion
#Modificacion de parametro end
print(saludo,end=",")
print(despedida)
#InterPolacion
print(f"Saludo:{saludo} Despedida:{despedida}")
#Multilinea
print("""Esto
Es
Un 
Texto
Multilinea """)
#Multilinea Con interpolacion
print(f"""Saludo
{saludo}
Despedida
{despedida}""")
#Operaciones con cadena
for letra in saludo:
    print(letra)
#Revertir cadena
print(saludo[::-1])
print(saludo)
print(''.join(reversed(saludo)))

