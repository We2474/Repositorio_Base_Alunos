# nome = input('Digite nome do usuário: ')
# email = input('Digite o e-mail do usuário: ')

# with open('pessoa.txt', 'a') as arquivo:
#     arquivo.write(nome + " | " + email + '\n')

with open('pessoa.txt', 'r') as arquivo:
    print(arquivo.read())