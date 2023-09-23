# Inicializar un diccionario vacío para almacenar la información de los empleados.
datos_empleados = {
    "empleado1": {
        "id": 1,
        "nombre": "Juan",
        "apellido": "Pérez",
        "puesto": "Ingeniero",
        "área": "Tecnología de la Información",
        "salario": 2500,
        "rol": "usuario",
        "usuario": "usuario",
        "contraseña": "contraseña",
    },
    "empleado2": {
        "id": 2,
        "nombre": "María",
        "apellido": "González",
        "puesto": "Gerente",
        "área": "Recursos Humanos",
        "salario": 1800,
        "rol": "usuario",
        "usuario": "maria456",
        "contraseña": "clave456",
    },
    "admin": {
        "id": 3,
        "nombre": "Admin",
        "apellido": "Gerente",
        "puesto": "Gerente de Recursos Humanos",
        "área": "Recursos Humanos",
        "salario": 3000,
        "rol": "admin",
        "usuario": "admin",
        "contraseña": "claveadmin",
    },
}

# Función para calcular el salario neto.
def calcular_salario_neto(empleado):
    salario = empleado["salario"]
    if salario < 2000:
        bono_transporte = 200
        salario += bono_transporte  # Agregar bono de transporte
    else:
        bono_transporte = 0
    salud = salario * 0.04
    pensión = salario * 0.04
    salario_neto = salario - salud - pensión
    return salario_neto, salud, pensión, bono_transporte

# Función para imprimir la información del empleado.
def imprimir_informacion_empleado(usuario):
    empleado = datos_empleados.get(usuario)
    if empleado:
        salario_neto, salud, pensión, bono_transporte = calcular_salario_neto(empleado)
        print("\nInformación del Empleado:")
        print(f"ID: {empleado['id']}")
        print(f"Nombre: {empleado['nombre']} {empleado['apellido']}")
        print(f"Puesto: {empleado['puesto']}")
        print(f"Salario Bruto: ${empleado['salario']:.2f}")
        print(f"Bono de Transporte: ${bono_transporte:.2f}")
        print(f"Deducción de Salud: ${salud:.2f}")
        print(f"Deducción de Pensión: ${pensión:.2f}")
        print(f"Salario Neto: ${salario_neto:.2f}")
    else:
        print("Empleado no encontrado.")

# Función para imprimir información de todos los empleados (solo para administradores).
def imprimir_toda_informacion_empleados(usuario_admin):
    if datos_empleados[usuario_admin]["rol"] == "admin":
        print("\nToda la Información de los Empleados:")
        for usuario, empleado in datos_empleados.items():
            salario_neto, salud, pensión, bono_transporte = calcular_salario_neto(empleado)
            print("\nInformación del Empleado:")
            print(f"ID: {empleado['id']}")
            print(f"Nombre: {empleado['nombre']} {empleado['apellido']}")
            print(f"Puesto: {empleado['puesto']}")
            print(f"Salario Bruto: ${empleado['salario']:.2f}")
            print(f"Bono de Transporte: ${bono_transporte:.2f}")
            print(f"Deducción de Salud: ${salud:.2f}")
            print(f"Deducción de Pensión: ${pensión:.2f}")
            print(f"Salario Neto: ${salario_neto:.2f}")

# Función para crear un nuevo empleado (solo para administradores).
def crear_empleado(usuario_admin):
    if datos_empleados[usuario_admin]["rol"] == "admin":
        nuevo_id = len(datos_empleados) + 1
        nuevo_nombre = input("Ingrese el nombre del empleado: ")
        nuevo_apellido = input("Ingrese el apellido del empleado: ")
        nuevo_puesto = input("Ingrese el puesto del empleado: ")
        nueva_area = input("Ingrese el área del empleado: ")
        nuevo_salario = float(input("Ingrese el salario del empleado: "))
        nuevo_rol = input("Ingrese el rol del empleado (usuario/admin): ")
        nuevo_usuario = input("Ingrese el nombre de usuario del empleado: ")
        nueva_contraseña = input("Ingrese la contraseña del empleado: ")

        nuevo_empleado = {
            "id": nuevo_id,
            "nombre": nuevo_nombre,
            "apellido": nuevo_apellido,
            "puesto": nuevo_puesto,
            "área": nueva_area,
            "salario": nuevo_salario,
            "rol": nuevo_rol,
            "usuario": nuevo_usuario,
            "contraseña": nueva_contraseña,
        }
        datos_empleados[nuevo_usuario] = nuevo_empleado
        print("Empleado creado exitosamente.")

# Función para iniciar sesión.
def iniciar_sesion():
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    empleado = datos_empleados.get(usuario)

    if empleado and empleado["contraseña"] == contraseña:
        if empleado["rol"] == "admin":
            while True:
                print("\nMenú de Administrador:")
                print("1: Imprimir Información del Empleado")
                print("2: Imprimir Toda la Información de los Empleados")
                print("3: Crear Nuevo Empleado")
                print("4: Cerrar Sesión")
                opción = input("Ingrese su elección: ")

                if opción == "1":
                    imprimir_informacion_empleado(usuario)
                elif opción == "2":
                    imprimir_toda_informacion_empleados(usuario)
                elif opción == "3":
                    crear_empleado(usuario)
                elif opción == "4":
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
        else:
            imprimir_informacion_empleado(usuario)
    else:
        print("Nombre de usuario o contraseña inválidos.")

# Menú principal utilizando funciones lambda como devoluciones de llamada.
opciones_menu = {
    "1": ("Iniciar Sesión", lambda: iniciar_sesion()),
    "2": ("Salir", exit),
}

while True:
    print("\nMenú Principal:")
    for opción, (descripción, _) in opciones_menu.items():
        print(f"{opción}: {descripción}")

    elección = input("Ingrese su elección: ")

    if elección in opciones_menu:
        opciones_menu[elección][1]()  # Ejecutar la función elegida.
    else:
        print("Elección inválida. Por favor, seleccione una opción válida.")