name = ["Pepito","Andrés","Juan","Maria","Pedro"]
age = [25, 19, 33, 40]
height = [1.80, 1.65, 1.74, 1.66, 1.54]
is_married = [False, False, False, True, True]

print(name[1:3])
print(name[:3])
print(name[1:])
print(name[-4:-1]) #es igual a name[1:4]

name.insert(2,"Pipe")

print(name)

name.pop(0)

print(name)

name.remove("Pipe")


for i in name:
    print(i)

for i in range (len(height)):
    print(height[i])    

[print(x) for x in name]

for i, h in enumerate(height):
    print(i, h)