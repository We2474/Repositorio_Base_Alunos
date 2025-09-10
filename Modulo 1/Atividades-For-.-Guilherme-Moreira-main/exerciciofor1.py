# Faça uma tabuada de acordo com o número que o usuário escolher

lista = [1,2,3,4,5,6,7,8,9,10]
numero = int(input('Digite um número para fazer sua tabuada: '))
for item in lista:
    print(numero * item)