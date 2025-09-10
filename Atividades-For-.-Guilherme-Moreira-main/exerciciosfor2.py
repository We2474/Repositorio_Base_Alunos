# Contar números pares de 1 a 20

range(21)

for item in range(1,21):
    if item % 2 == 0:
        print(f'{item } é Par. ')
    else:
        print(f'{item } é Impar. ')