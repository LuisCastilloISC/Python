#lambda arguments : expression 
(lambda *n:print(sum(n)))(*list(range(0,101,1)))
def multiplicador(n):
    return lambda a:print(a*n)
duplicador = multiplicador(2)
triplicador = multiplicador(3)
duplicador(11)
triplicador(11)

suma = None
try:
    
  suma = 1+"1" 

except Exception as s:
    print(s )
else:
    print(suma)
finally:
    print(suma)
#assert
def suma(a,b):
    assert(type(a)==int)
    assert(type(b)==int)
    print(a+b)
suma(1.2,5)
def multiplicar(n):
    return lambda a:print(a*n)

duplicador =multiplicar(2)
duplicador("hola")

