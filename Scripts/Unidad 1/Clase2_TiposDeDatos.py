#Metodos

l = [ 2,3]
l.append(4)
print(l)

#Extend

l = [ 2,3]
l.extend([4,5])
print(l)

#insert
l = [ 2,3]
l.insert(1,1)
print(l)

#remove
l=[2,3]
l.remove(3)
print(l)

#POP
l=[2,3,4]
l.pop()
print(l)

#reverse
l=[2,3,4,5,6]
l.reverse()
print(l)

l=[9,5,6,3,2,1,4]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
indice = l.index(6)
print(indice)

l=["Hugo","Paco","Luis","Petra","Nose","Juan"]
print(l.index("Petra"))


#SET
s = {5,6,7,8,2}
print(s)
print(type(s))


for ss in s:
    print(ss)

print(2 in s)
s1={1,4,3}
s2 ={5,2}
print(s1|s2)

#Metodos SET
s={1,2,3}
s.add(4)
print(s)

#s.remove(5)
s.discard(5)

s.pop()
print(s)

s.clear()
print(s)

# s1 = {1,2,3}
# s2 = {3,4,5}

# print(s1.union(s2))
# print(s1.intersection(s2))


#Diccionarios
d1 = {"Nombre":"Rocio","Edad":24,"Documento":"09012022"}
print(d1)
print(type(d1))
d2 = dict([('Nombre',"Rocio"),("Edad",24),("Documento","09012022")])
print(d2)
d3 = dict(Nombre="Rocio",Edad=24,Documento="09012022")
print(d3)

print(d3.get("Nombre"))

d3["Nombre"]="Pedro"
print(d3)

d3["Comida"] = "Tacos"
print(d3)
d3["Comida"]="burritos"
print(d3)

for x in d3:
    print(x)

for x in d3:
    #d3["key"]
    print(d3[x])

for x,y in d3.items():
    print(x,y)

d1 = {"a":1, "b":2}
d2 = {"a":1,"b":{"c":3}}

d3={
    "d1":d1,
    "d2":d2
}
print(d3)

#Metodos
# d3.clear()
# print(d3)

#get
print(d3.get("d4","No encontrado"))

#items
print(list(d3.items())[0])

#keys

print(list(d3.keys())[0])
print(d3.values())

# d3.pop("d1")
# print(d3)
# resultado =d3.pop("d1",-1)
# print(resultado)

d3.popitem()
print(d3)

#update
d1 = {"a":1,"b":2,"c":100}
d2 = {"a":300,"b":400,"d":400}
d1.update(d2)
print(d1)

d4={"b":2,"b":4}
print(d4)














