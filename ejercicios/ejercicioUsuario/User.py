class User:
    def __init__(self, id, name, lastName, email, password):
        self._id = id
        self._name = name
        self._lastName = lastName
        self._email = email
        self._password = password

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def email(self, password):
        self._password = password

    def registrar_usuario(self):
        self.id = input("Id : ")
        self.name = input("Name : ")
        self.lastName = input("Last name : ")
        self.email = input("Email: ")
        self.password = input("Password: ")


    def ver_usuario(self):
        print("Id: "+ str(self._id))
        print("Name: "+self._name)
        print("Last Name: "+self._lastName)
        print("Email : "+self._email)
        print("Password: "+self._password)
