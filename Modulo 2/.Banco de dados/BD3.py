from coneccao import Session
from t1 import Loja

with Session() as session:
    lojas=Loja(nome = "carGuiMoreira",endereco="rua padilha", gerente="M.R. Moreira")
    session.add(lojas)
    session.commit()
    print('Cê é loucoooooo')