from User import User

class Client(User):
    def __init__(self, id, name, lastName, email, password, phoneNumber, address):
        super.__init__(id,name, lastName, email, password)
        self._phoneNumber = phoneNumber
        self._address = address

    @property
    def phoneNumber(self):
        return self._phoneNumber

    @phoneNumber.setter
    def phoneNumer(self, phoneNumber):
        self._phoneNumber = phoneNumber

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self.address = address


    def registrar_usuario(self):
        #super().registar_usuario()
        self._address = input("Address: ")
        self._phoneNumber = input("Phone Number: ")

    def login(self):
        emailInput = input("Email ")
        passInput = input("Password ")

        if(emailInput == self.email and passInput == self.password):
            print(self.email)
            return True

    def business(self, login):
        init = login(self)

        #menu