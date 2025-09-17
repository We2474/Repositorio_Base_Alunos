import requests


local = input('Qual mesa vão se sentar? ')
pedido = input('Qual será seu pedido? ')
bebida = input('Bebida pra acompanhamento? ')
lista = (f'{local}, {pedido}, {bebida}')
cliente={
    'prato':pedido,
    'bebida':bebida,
    'mesa':local
}
r = requests.post("https://68ca9f3f430c4476c34a3b5f.mockapi.io/Restaurante",cliente)

print(r.json())


for item in lista:
    print(f'Me acompanhe até a mesa {local}. Irei trazer seu pedido {pedido}, com a bebida {bebida} de acompanhamento: ')
    break