class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.margen_de_venta = margen_de_venta
        self.precio_de_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        try:
            return self.costo / (1 - self.margen_de_venta)
        except ZeroDivisionError:
            print(" El margen de venta no puede ser del 100%")
            return None

class Registradora:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id not in self.productos:
            self.productos[producto.id] = producto
            print( producto.nombre+" fue registrado correctamente")
        else:
            print("El producto con id"+ producto.id  +"ya esta registrado")

    def listar_productos(self):
        print("Listado de Productos:")
        for producto in self.productos.values():
            print("ID: "+ str(producto.id))
            print("Nombre: "+producto.nombre)
            print("Descripcion: "+producto.descripcion)
            print("Costo: "+ str(producto.costo))
            print("Cantidad: "+ str(producto.cantidad))
            print("Precio de Venta: "+ str(producto.precio_de_venta))


if __name__ == "__main__":
    registro = Registradora()

    producto1 = Producto(1, "Nintendo Switch", "Para dos jugadores", 50000, 10, 0.2)
    producto2 = Producto(2, "Album", "Version Dark", 75000, 5, 0.25)


    registro.agregar_producto(producto1)
    registro.agregar_producto(producto2)

    registro.listar_productos()