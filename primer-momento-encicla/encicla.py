class Usuario:
    def __init__(self, nombre, apellido, id, email):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.email = email
        self.bicicleta_prestada = None

    def __str__(self):
        return f"{self.nombre} {self.apellido} (ID: {self.id})"


class Bicicleta:
    def __init__(self, id, estado="Disponible"):
        self.id = id
        self.estado = estado

    def __str__(self):
        return f"Bicicleta {self.id} ({self.estado})"


class SistemaBicicletas:
    def __init__(self):
        self.usuarios = []
        self.bicicletas = [Bicicleta(f"B{i+1}") for i in range(10)]

    def crear_usuario(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        id = input("Ingrese su ID: ")
        email = input("Ingrese su correo electrónico: ")

        usuario = Usuario(nombre, apellido, id, email)
        self.usuarios.append(usuario)
        print("Usuario creado con éxito!")

    def iniciar_sesion(self):
        id = input("Ingrese su ID para iniciar sesión: ")
        usuario = next((u for u in self.usuarios if u.id == id), None)
        if usuario:
            return usuario
        else:
            print("Usuario no encontrado. Por favor, regístrese primero.")
            return None

    def prestar_bicicleta(self, usuario):
        if not usuario:
            return

        if usuario.bicicleta_prestada is not None:
            print("Ya ha prestado una bicicleta.")
            return

        bicicletas_disponibles = [b for b in self.bicicletas if b.estado == "Disponible"]
        if not bicicletas_disponibles:
            print("No hay bicicletas disponibles para prestar.")
            return

        print("Bicicletas Disponibles:")
        for i, bicicleta in enumerate(bicicletas_disponibles):
            print(f"{i + 1}. {bicicleta}")

        eleccion = input("Ingrese el número de la bicicleta que desea prestar (o 'q' para salir): ")
        if eleccion == 'q':
            return

        try:
            eleccion = int(eleccion)
            if 1 <= eleccion <= len(bicicletas_disponibles):
                bicicleta_elegida = bicicletas_disponibles[eleccion - 1]
                bicicleta_elegida.estado = "Prestada"
                usuario.bicicleta_prestada = bicicleta_elegida
                print(f"{usuario.nombre} {usuario.apellido} ha prestado {bicicleta_elegida}.")

                origen = input("Ingrese el origen del viaje: ")
                destino = input("Ingrese el destino del viaje: ")
                print(f"Viaje registrado: Origen: {origen}, Destino: {destino}")
            else:
                print("Selección inválida. Por favor, seleccione una bicicleta válida.")
        except ValueError:
            print("Entrada inválida. Ingrese un número o 'q' para salir.")

    def listar_bicicletas_disponibles(self):
        bicicletas_disponibles = [b for b in self.bicicletas if b.estado == "Disponible"]
        if bicicletas_disponibles:
            print("Bicicletas Disponibles:")
            for bicicleta in bicicletas_disponibles:
                print(bicicleta)
        else:
            print("No hay bicicletas disponibles.")

    def listar_usuarios_con_bicicletas(self):
        usuarios_con_bicicletas = [u for u in self.usuarios if u.bicicleta_prestada is not None]
        if usuarios_con_bicicletas:
            print("Usuarios con Bicicletas Prestadas:")
            for usuario in usuarios_con_bicicletas:
                print(usuario)
        else:
            print("Nadie ha prestado bicicletas.")


def main():
    sistema_bicicletas = SistemaBicicletas()

    while True:
        print("\nMenú del Sistema de Préstamo de Bicicletas:")
        print("1. Crear Usuario")
        print("2. Iniciar Sesión")
        print("3. Prestar una Bicicleta")
        print("4. Listar Bicicletas Disponibles")
        print("5. Listar Usuarios con Bicicletas")
        print("6. Salir")

        eleccion = input("Ingrese su elección: ")

        if eleccion == '1':
            sistema_bicicletas.crear_usuario()
        elif eleccion == '2':
            usuario = sistema_bicicletas.iniciar_sesion()
            if usuario:
                print(f"Bienvenido, {usuario.nombre}!")
        elif eleccion == '3':
            sistema_bicicletas.prestar_bicicleta(usuario)
        elif eleccion == '4':
            sistema_bicicletas.listar_bicicletas_disponibles()
        elif eleccion == '5':
            sistema_bicicletas.listar_usuarios_con_bicicletas()
        elif eleccion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Elección inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()