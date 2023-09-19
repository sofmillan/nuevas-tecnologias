
#Usando diccionarios y funciones en el que creemos un producto con los siguientes claves
#id, nomnbre, costo, cantidad, margen de ganancia(porcentaje)
#almacenar los productos con dos campos adicionales calculados
#precio de venta =  costo/1-mg
#valor de inventario = cantidad * costo/1
#almacenar los productos dentro de un diccionario de diccionarios



productos = {
    "123": {"id":"123", "nombre":"Doritos","cantidad":2, "costo":3000, "margen":0.2, "precioVenta":3750, "valorInventario":6000}
}

print(productos)


def crearProducto():

    print("--- Añadir Producto ---")
    id = input("Ingrese el id: ")

    if id in productos.keys():
        print("Producto ya existe")
        return
    
    nombre = input("Ingrese el nombre: ")
    cantidad = int(input("Ingrese el cantidad: "))
    costo = int(input("Ingrese el costo: "))
    margen = float(input("Ingrese el margen: "))

    precioVenta = costo/(1-margen)
    valorInventario = cantidad*costo

    

    productos[str(id)] = {"id":id, "nombre":nombre, "cantidad":cantidad,"costo":costo, "margen":margen, "precioVenta":precioVenta,"valorInventario":valorInventario}

    print(productos)

def venderProducto():
    
    id = input("Ingresa el id del producto ")
    cantidad = int(input("Ingresa la cantidad a vender "))

    if(cantidad<=productos[str(id)]["cantidad"]):
        productos[str(id)]["cantidad"] -= cantidad
        print("Se venden "+str(productos[str(id)]["cantidad"])+" unidades de "+productos[str(id)]["nombre"])    
    else:
        print("Cantidad en inentario insuficiente")

    print(productos[str(id)])

while True:

    print("BIENVENIDO")
    print("1 -> Crear producto")
    print("2 -> Vender producto")
    print("3 -> Listar productos")
    print("4 -> Salir")

    opcion=input("Digita el número ")

    if opcion=="1":
        crearProducto()
    elif opcion=="2":
        venderProducto()  
    elif opcion=="3":
        print(productos)     
    elif opcion=="4":
        break
      
print(productos)
