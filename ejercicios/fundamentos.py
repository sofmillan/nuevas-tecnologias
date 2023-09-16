
#Condicionales

servicio = True
total = 100000


if(servicio):
    total += total*0.4

print(f"El total a pagar es ",total)


#Listas y ciclos

nombres = ["Pepito","Andrés","Juan","Maria","Pedro"]
edades = [25, 19, 33, 40]
alturas = [1.80, 1.65, 1.74, 1.66, 1.54]
esta_casado = [False, False, False, True, True]

print(nombres[1:3])
print(nombres[:3])
print(nombres[1:])
print(nombres[-4:-1]) #es igual a name[1:4]

nombres.insert(2,"Pipe")

print(nombres)

nombres.pop(0)

print(nombres)

nombres.remove("Pipe")


for i in nombres:
    print(i)

for i in range (len(alturas)):
    print(alturas[i])    

[print(x) for x in nombres]

for i, h in enumerate(alturas):
    print(i, h)


#Funciones

def saludar():
    print("Hola")

saludar()


def greetPerson(name):
    print(f"Hello {name}")