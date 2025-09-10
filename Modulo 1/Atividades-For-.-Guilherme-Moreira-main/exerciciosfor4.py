# Listar números ímpares de 10 a 20

lista = range(10,21)

for item in lista:
    if item % 2 == 0:
        print('Par')
    else:
        print('impar')