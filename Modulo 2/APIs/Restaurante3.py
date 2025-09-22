import requests



passo1 = requests.get(f'https://68ca9f3f430c4476c34a3b5f.mockapi.io/Restaurante/')
print(passo1.json())



id = input('digite seu id para alterar: ')

if passo1 != ("pedido","bebida"):
    passo2 = requests.delete(f'https://68ca9f3f430c4476c34a3b5f.mockapi.io/Restaurante/pedido/bebida')
    pedido = input ('Qual será seu pedido? ')
    bebida = input('Bebida pra acompanhamento? ')
    cliente = {
    'prato':pedido,
    'bebida':bebida,
    }


    resposta = requests.put(f'https://68ca9f3f430c4476c34a3b5f.mockapi.io/Restaurante/pedido/bebida/{id}',cliente)

else:
    print('beleza, sem trocas por hoje. ')

    