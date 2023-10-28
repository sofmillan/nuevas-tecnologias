from ejercicios.poo.Persona import Persona

class Estudiante(Persona):
    def __init__(self, id, nombre, correo, contrasena, programa, semestre):
        super().__init__(id, nombre, correo, contrasena)
        self.programa = programa
        self.semestre = semestre

    def verPersona(self):
        print(f"Id:{self.id} "
              f"Nombre:{self.nombre} \n"
              f"Correo:{self.correo} \n"
              f"Compania:{self.compania}"
              f"Programa:{self.programa} \n"
              f"Semestre:{self.semestre} \n"
              )
        
estudiante = Estudiante(1,"Ricky","ricky@gmail.com","123456","Software","Primer")       






    