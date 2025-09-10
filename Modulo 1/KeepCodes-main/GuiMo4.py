valor_dp = float(input("Insira o preço do produto: "))

valor_p = float(input("Insira o valor pago: "))

resultado = valor_p - valor_dp

print (resultado)

if resultado >= 0:
    print('Você ainda tem dinheiro ')
else:
    print('Você está devendo ')