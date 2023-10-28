# coding=utf-8
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from User import User
    from Cliente import Client
    user1 = User(12345, "Ricky", "Shen", "ricky@gmail.com", "lovelicky")

    user1.ver_usuario()

    client1 = Client(
        id=None,
        name=None,
        lastName=None,
        email=None,
        phoneNumber=None,
        address=None,
        password=None
    )

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
