user1 = {"name":"Ricky","lastName":"Shen","code":"xyz"}
user2 = {"name":"Ricky","lastName":"Shen","code":"xyz"}
user3 = {"name":"Ricky","lastName":"Shen","code":"abc"}
print(user1.keys())

print(user1.values())

for x,y in user1.items():
    print(x,y)

for x in user1.keys():
    print(x)    

print(user1.get("name"))

user1.pop("name")

print(user1.keys())

user1.popitem()

print(user1.keys())


users = {
    "user1":user1,
    "user2":user2,
    "user3":user3
}

print(users["user3"])




#Usando diccionarios y funciones en el que creemos un producto con los siguientes claves
#id, nomnbre, costo, cantidad, margen de ganancia(porcentaje)
#almacenar los productos con dos campos adicionales calculados
#precio de venta =  costo/1-mg
#valor de inventario = cantidad * costo/1
#almacenar los productos dentro de un diccionario de diccionarios