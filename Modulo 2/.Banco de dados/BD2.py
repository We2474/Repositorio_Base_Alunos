from coneccao import Session
from t1 import Venda

with Session() as session:
    vendas=Venda(carro = "Celta Cinza de V8",valor= "R$100.000,00", comissao = "R$2.000", vendedor_id = 1)
    session.add(vendas)
    session.commit()
    print('Cê é loucoooooo')