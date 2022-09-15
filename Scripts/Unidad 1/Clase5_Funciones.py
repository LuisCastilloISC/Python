def f(x):
    return 2*x
y = f(3)
print(y) # 6

#El principio de reusabilidad, que nos dice que si por ejemplo tenemos un fragmento de código usado en muchos sitios, la mejor solución sería pasarlo a una función. Esto nos evitaría tener código repetido, y que modificarlo fuera más fácil, ya que bastaría con cambiar la función una vez.
#El principio de modularidad, que defiende que en vez de escribir largos trozos de código, es mejor crear módulos o funciones que agrupen ciertos fragmentos de código en funcionalidades específicas, haciendo que el código resultante sea más fácil de leer.

#argumentos
def di_hola():
    print("Hola")

def di_hola(nombre):
    print("Hola", nombre)
di_hola("Rocio")
# Hola Rocio

#argumentos por posición
#Los argumentos por posición o posicionales son la forma más básica e intuitiva de pasar parámetros. Si tenemos una función resta() que acepta dos parámetros, se puede llamar como se muestra a continuación.

def resta(a, b):
    return a-b
resta(5, 3) # 2
#Al tratarse de parámetros posicionales, se interpretará que el primer número es la a y el segundo la b. El número de parámetros es fijo, por lo que si intentamos llamar a la función con solo uno, dará error.

#resta(1) # Error! TypeError

#Tampoco es posible usar mas argumentos de los tiene la función definidos, ya que no sabría que hacer con ellos. Por lo tanto si lo intentamos, Python nos dirá que toma 2 posicionales y estamos pasando 3, lo que no es posible.

#TypeError: resta() takes 2 positional arguments but 3 were given
#resta(5,4,3) # Error


#Argumentos por nombre
#Otra forma de llamar a una función, es usando el nombre del argumento con = y su valor. El siguiente código hace lo mismo que el código anterior, con la diferencia de que los argumentos no son posicionales.

resta(a=3, b=5) # -2
#Al indicar en la llamada a la función el nombre de la variable y el valor, el orden ya no importa, y se podría llamar de la siguiente forma.

resta(b=5, a=3) # -2
#Como es de esperar, si indicamos un argumento que no ha sido definido como parámetro de entrada, tendremos un error.

#resta() got an unexpected keyword argument 'c'
#resta(b=5, c=3) # Error!


#Argumentos por defecto
#Tal vez queramos tener una función con algún parámetro opcional, que pueda ser usado o no dependiendo de diferentes circunstancias. Para ello, lo que podemos hacer es asignar un valor por defecto a la función. En el siguiente caso c valdría cero salvo que se indique lo contrario.

def suma(a, b, c=0):
    return a+b+c
suma(5,5,3) # 13
#Dado que el parámetro c tiene un valor por defecto, la función puede ser llamada sin ese valor.

suma(4,3) # 7
#Podemos incluso asignar un valor por defecto a todos los parámetros, por lo que se podría llamar a la función sin ningún argumento de entrada.

def suma(a=3, b=5, c=0):
    return a+b+c
suma() # 8
#Las siguientes llamadas a la función también son válidas

suma(1)     # 6
suma(4,5)   # 9
suma(5,3,2) # 10
#O haciendo uso de lo que hemos visto antes y usando los nombres de los argumentos.

suma(a=5, b=3) #8



#Argumentos de longitud variable
#En el ejemplo con argumentos por defecto, hemos visto que la función puede ser llamada con diferente número de argumentos de entrada, pero esto no es realmente una función con argumentos de longitud variable, ya que existe un número máximo.
#Imaginemos que queremos una función suma() como la de antes, pero en este caso necesitamos que sume todos los números de entrada que se le pasen, sin importar si son 3 o 100. Una primera forma de hacerlo sería con una lista.

def suma(numeros):
    total = 0
    for n in numeros:
        total += n
    return total
suma([1,3,5,4]) # 13
#La forma es válida y cumple nuestro requisito, pero realmente no estamos trabajando con argumentos de longitud variable. En realidad tenemos un solo argumento que es una lista de números.
#Por suerte, Python tiene una herramienta muy potente. Si declaramos un argumento con *, esto hará que el argumento que se pase sea empaquetado en una tupla de manera automática. No confundir * con los punteros en otros lenguajes de programación, no tiene nada que ver.

def suma(*numeros):
    print(numeros)
    print(type(numeros))
    # <class 'tuple'>
    total = 0
    for n in numeros:
        total += n
    return total
suma(1, 3, 5, 4) # 13


#Usando doble ** es posible también tener como parámetro de entrada una lista de elementos almacenados en forma de clave y valor. En este caso podemos iterar los valores haciendo uso de items().

def suma(**kwargs):
    suma = 0
    for key, value in kwargs.items():
        print(key, value)
        suma += value
    return suma

suma(a=5, b=20, c=23) # 48
#De igual manera, podemos pasar un diccionario como parámetro de entrada.

def suma(**kwargs):
    suma = 0
    for key, value in kwargs.items():
        print(key, value)
        suma += value
    return suma
di = {'a': 10, 'b':20}
suma(**di) # 30


#Sentencia return
#El uso de la sentencia return permite realizar dos cosas:

#Salir de la función y transferir la ejecución de vuelta a donde se realizó la llamada.
#Devolver uno o varios parámetros, fruto de la ejecución de la función.
#En lo relativo a lo primero, una vez se llama a return se para la ejecución de la función y se vuelve o retorna al punto donde fue llamada. Es por ello por lo que el código que va después del return no es ejecutado en el siguiente ejemplo.

def mi_funcion():
    print("Entra en mi_funcion")
    return
    print("No llega")
mi_funcion() # Entra en mi_funcion
#Por ello, sólo llamamos a return una vez hemos acabado de hacer lo que teníamos que hacer en la función.

#Por otro lado, se pueden devolver parámetros. Normalmente las funciones son llamadas para realizar unos cálculos en base a una entrada, por lo que es interesante poder devolver ese resultado a quien llamó a la función.

def di_hola():
    return "Hola"
di_hola()
# 'Hola'
#También es posible devolver mas de una variable, separadas por ,. En el siguiente ejemplo tenemos una función que calcula la suma y media de tres números, y devuelve su resultado.

def suma_y_media(a, b, c):
    suma = a+b+c
    media = suma/3
    return suma, media
sumaresultado, mediaresultado = suma_y_media(9, 6, 3)
print(sumaresultado)  # 18
print(mediaresultado) # 6.0


#Documentación
#Ahora que ya tenemos nuestras propias funciones creadas, tal vez alguien se interese en ellas y podamos compartírselas. Las funciones pueden ser muy complejas, y leer código ajeno no es tarea fácil. Es por ello por lo que es importante documentar las funciones. Es decir, añadir comentarios para indicar como deben ser usadas.

def mi_funcion_suma(a, b):
    """
    Descripción de la función. Como debe ser usada,
    que parámetros acepta y que devuelve
    """
    return a+b
#Para ello debemos usar la triple comilla """ al principio de la función. Se trata de una especie de comentario que podemos usar para indicar como la función debe ser usada. No se trata de código, es un simple comentario un tanto especial, conocido como docstring.

#Ahora cualquier persona que tenga nuestra función, podrá llamar a la función help() y obtener la ayuda de como debe ser usada.

help(mi_funcion_suma)
prin
#otra forma de acceder a la documentación es la siguiente.

print(mi_funcion_suma.__doc__)
#Para saber más: Las descripciones de las funciones suelen ser un poco mas detalladas de lo que hemos mostrado. En la PEP257 se define en detalle como debería ser.

#Anotaciones en funciones
#Existe una funcionalidad relativamente reciente en Python llamada function annotation o anotaciones en funciones. Dicha funcionalidad nos permite añadir metadatos a las funciones, indicando los tipos esperados tanto de entrada como de salida.

def multiplica_por_3(numero: int) -> int:
    return numero*3

multiplica_por_3(6) # 18
#Las anotaciones son muy útiles de cara a la documentación del código, pero no imponen ninguna norma sobre los tipos. Esto significa que se puede llamar a la función con un parámetro que no sea int, y no obtendremos ningún error.

multiplica_por_3("Cadena")
# 'CadenaCadenaCadena'

#Mezclando *args y **kwargs
#Una vez entendemos el uso de *args y **kwargs, podemos complicar las cosas un poco más. Es posible mezclar argumentos normales con *args y **kwargs dentro de la misma función. Lo único que necesitas saber es que debes definir la función en el siguiente orden:

#Primero argumentos normales.
#Después los *args.
#Y por último los **kwargs.
#Veamos un ejemplo.

def funcion(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    for arg in args:
        print("args =", arg)
    for key, value in kwargs.items():
        print(key, "=", value)

funcion(10, 20, 1, 2, 3, 4, x="Hola", y="Que", z="Tal")
#Salida
#a = 10
#b = 20
#args = 1
#args = 2
#args = 3
#args = 4
#x = Hola
#y = Que
#z = Tal

#Y por último un truco que no podemos dejar sin mencionar es lo que se conoce como tuple unpacking. Haciendo uso de *, podemos extraer los valores de una lista o tupla, y que sean pasados como argumentos a la función.

def funcion(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    for arg in args:
        print("args =", arg)
    for key, value in kwargs.items():
        print(key, "=", value)

args = [1, 2, 3, 4]
kwargs = {'x':"Hola", 'y':"Que", 'z':"Tal"}

funcion(10, 20, *args, **kwargs)
#Salida
#a = 10
#b = 20
#args = 1
#args = 2
#args = 3
#args = 4
#x = Hola
#y = Que
#z = Tal


numeros = list(range(1,101,1))
print(numeros)
def suma(*numeros):
    print(numeros)
    suma=0
    for n in numeros:
        suma+=n
    return suma
print(suma(*numeros))