import requests

pergunta = input('Digite qual pokemon vc quer: ')
r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pergunta}")
j = r.json()

info = input("Qual info tu quer? ")
if info == ('nome'):
    print(j.get('name'))
elif info == ('habilidade'):
    print(j.get('abilities'))
