#Esto se conoce como crear un script. A medida que tu programa crezca, 
# quizás quieras separarlo en varios archivos para que el mantenimiento sea más sencillo. 
# Quizás también quieras usar una función útil que has escrito en distintos programas sin copiar su definición en cada programa.
#Para soportar esto, Python tiene una manera de poner definiciones en un archivo y usarlos en un script o en una instancia del intérprete. 
# Este tipo de ficheros se llama módulo; las definiciones de un módulo pueden ser importadas a otros módulos o al módulo principal 
# (la colección de variables a las que tienes acceso en un script ejecutado en el nivel superior y en el modo calculadora).


import csv
import random

numRandom = random.randint(0,100)

while True:
    numero = int(input("Cual sera el numero entre 0 y 100?: " ))
    if numero==numRandom:
        break
    if numero > numRandom:
        print("El numero es menor") 
    else:
        print("El numero es mayor")
print(f"Le atinaste al numero!\n{numRandom}")

with open('sample.csv') as file:
    # creating the reader
    reader = csv.reader(file)
    
    # reading line by line using loop
    for row in reader:
        # row is a list containing elements from the CSV file
        # joingin the list using join(list) method
        print(','.join(row))