# divide o seu peso (em quilogramas) pela sua altura (em metros) elevada ao quadrado.

# essa parte são as variáveis só:
nome = input('Digite o nome do paciente: ')
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = float(peso / (altura * altura)) 


# Esse é o if, elif e o else que vão separar e fazer condições pra poderem existir pesos diferentes e seus graus: 
if imc >= 40:
    print (f'{nome} tem IMC igual a {imc}, classificado como obesidade grau 3. ')
elif imc >=35:
    print (f'{nome} tem IMC igual a {imc}, classificado como obesidade grau 2. ')
elif imc >=30:
    print (f'{nome} tem IMC igual a {imc}, classificado como obesidade grau 1. ')
elif imc >=25:
    print (f'{nome} tem IMC igual a {imc}, classificado como sobrepeso. ')
elif imc >=18.5:
    print (f'{nome} tem IMC igual a {imc}, classificado como peso ideal. ')
else:
    print (f'{nome} tem IMC igual a {imc}, classificado como abaixo do peso. ')