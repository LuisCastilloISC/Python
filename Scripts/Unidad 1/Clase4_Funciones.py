# def suma(a,b):
#     print(b)
#     print(a)
#     print(a+b)

# suma(b=1,a=2)

# def resta( a=0,b=2,c=1):
#     print(a-b-c)

# resta() 




# def nombres(*nombres):
#     print(type(nombres))
#     for n in nombres:
#         print(n)
# nombres("Pedro","Hugo","Rosa")


def suma(**knumeros):
    suma = 0
    for key , value in knumeros.items():
        print(key,value)
        suma+=value
    print(suma)
d1= dict(a=1.2,c=5)
suma(**d1)

def miFuncion():
    print("Entrada")
    return
    print("No")
miFuncion()

def sumaMedia(a,b,c):
    suma = a+b+c
    media = suma/3
    miTupla = (suma,media)
    return miTupla
sumaResultado , mediaResultado = sumaMedia(1,2,4)
print(sumaResultado,mediaResultado)


def miFuncion(a:int ,b:int ) -> int:
    """ 
    Alguna Descripcion Util
    """
    return a+b
resultado = miFuncion("A","B")
print(resultado)

#help(miFuncion)
#print(miFuncion.__doc__)

def funcion(a,b,*args,**kargs):
    print(a)
    print(b)
    for i in args:
        print(i)
    for key,value in kargs.items():
        print(key,value)

numeros = list(range(1,101,1))
print(numeros)
def suma(*numeros):
    print(numeros)
    suma=0
    for n in numeros:
        suma+=n
    return suma
print(suma(*numeros))



