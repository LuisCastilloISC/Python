#Estructuras de Control

#If
a = 4
b = 2
if b != 0:
    print(a/b)

#Indentacion
if b != 0:
    c = a/b
    d = c + 1
    print(d)
if b != 0:
    c = a/b
    print("Dentro if")
print("Fuera if")


#AND
a = 10
if a > 5 and a < 15:
    print("Mayor que 5 y menos que 15")

#PASS
#if a > 5:
if a > 5:
    pass

#If en una linea
if a > 5: print("Es > 5")
if a > 5: print("Es > 5"); print("Dentro del if"); 

#Uso de else y elif
x = 5
if x == 5:
    print("Es 5")
else:
    print("No es 5")

x = 5
if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x == 7:
    print("Es 7")
#Solo un else
x = 5
if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x == 7:
    print("Es 7")
else:#R
    print("Es otro")
#Operador ternario
x = 5
print("Es 5" if x == 5 else "No es 5")
#Es 5
a = 10
b = 5
c = a/b if b!=0 else -1
print(c)
#2


#FOR
for i in "Python":
    print(i)
#For anidado
lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]

for i in lista:
    print(i)
#[56, 34, 1]
#[12, 4, 5]
#[9, 4, 3]
for i in lista:
    for j in i:
        print(j)

#Range
for i in range(6):
    print(i) #0, 1, 2, 3, 4, 5

#range(inicio, fin, salto)

for i in range(5, 20, 2):
    print(i) #5,7,9,11,13,15,17,19

#Break y Continue

cadena = 'Python'
for letra in cadena:
    if letra == 'y':
        print(letra)
        break
    

cadena = 'Python'
for letra in cadena:
    if letra == 'P':
        continue
    print(letra)

#While
x = 5
while x > 0:
    x -=1
    print(x)

# while True:
#     print("Bucle infinito")

x = 5
while x > 0: x-=1; print(x)
#Else en while
x = 5
while x > 0:
    x -=1
    print(x) #4,3,2,1,0
else:
    print("El bucle ha finalizado")
    x = 5
#while break    
while True:
    x -= 1
    print(x) #4, 3, 2, 1, 0
    if x == 0:
        break
else:
    # El print no se ejecuta
    print("Fin del bucle")

z = 7
x = 1
while z > 0:
    print(' ' * z + '*' * x + ' ' * z)
    x+=2
    z-=1