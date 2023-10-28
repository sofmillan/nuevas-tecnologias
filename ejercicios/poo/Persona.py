class Persona:

    compania = "xyz"

    def __init__(self, id, nombre, correo, contrasena):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena

    def verPersona(self):
        print(f"Id:{self.id} ",
              f"Nombre:{self.nombre} \n",
              f"Correo:{self.correo} \n",
              f"Compania:{self.compania}")
            

maria = Persona(1, "Maria","maria@gmail.com","lovelicky")

maria.verPersona()