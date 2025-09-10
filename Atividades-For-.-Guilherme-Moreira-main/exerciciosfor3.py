# Contar vogais em uma palavra

palavra = input('Digite uma palavra: ')
# palavra = 'gabriel'
for item in palavra:
    print(item)
    if item not in 'aeiou'   :
        print('cons')
    else:
        print('vog')