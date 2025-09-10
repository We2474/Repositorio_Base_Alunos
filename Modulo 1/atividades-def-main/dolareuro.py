
dinheiro = float(input('Digite o valor: '))


def nome(n1):
# Valor dolar
    dolar = n1 / 5.51
    euro = n1 / 6.39

    while True:
        if n1 <= 0:
            float(input('Digite o valor: '))
        else:
            print(f'Seu saldo em euro ficaria {euro}, em dolar é {dolar}. ')
            break


