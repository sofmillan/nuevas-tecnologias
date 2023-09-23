salario = float(input("Salario: "))

def pagoEps(salario):
    return salario * 0.04

eps = pagoEps(salario)
def pagoPension(salario):
    return salario * 0.04

pension = pagoPension(salario)

def pagoNomina(salario, eps, pension):
    salario_neto = salario - eps - pension
    print(salario_neto)

pagoNomina(salario, eps, pension)

def pagoNomina2(salario):
    eps = pagoEps(salario)
    pension = pagoPension(salario)
    salario_neto = salario - eps - pension
    print(salario_neto)
pagoNomina2(salario)

def pagoNomina3(salario):
    eps = lambda salario: salario * 0.04
    pension = lambda salario: salario * 0.04
    salario_neto = salario - eps(salario) - pension(salario)
    print(salario_neto)
pagoNomina3(salario)



def call(valor):
    print(f"El salario es:{valor}")

def pagoNomina4(salario, call):    
    eps = lambda salario: salario * 0.04
    pension = lambda salario: salario * 0.04
    salario_neto = salario - eps(salario) - pension(salario)
    call(salario_neto)