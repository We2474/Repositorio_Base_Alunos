# pede informações:
nome = input('Digite nome do usuário: ')
email = input('Digite o e-mail do usuário: ')

# cria o 'pessoa.txt':
with open('pessoa.txt', 'a') as arquivo:
    arquivo.write(nome + " | " + email + '\n')


# lê o que foi escrito, se já tiver o 'pessoa.txt':
with open('pessoa.txt', 'r') as arquivo:
    print(arquivo.read())