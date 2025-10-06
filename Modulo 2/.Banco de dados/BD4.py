from coneccao import Session
from t1 import Vendedor

with Session() as session:
    vendedores=Vendedor(nome = "func1",lojaid= 1)
    session.add(vendedores)
    session.commit()
    print('Cê é loucoooooo')