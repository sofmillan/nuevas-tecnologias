usuarios = {"user1","user2","user2","user3", "user4"}


#usuarios[1] = "usern"

print(usuarios)

usuarios.remove("user4")

print(usuarios)


print("user2" in usuarios)

for i in usuarios:
    print(i)

usuariosNuevos = {"user6","user7"}

usuarios.union(usuariosNuevos)
