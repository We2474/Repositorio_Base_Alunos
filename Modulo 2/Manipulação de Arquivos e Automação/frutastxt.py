# frutas.txt

# Função para cadastrar usuário e salvar em arquivo
def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    try:
        with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(nome + "\n")
        print(f"Usuário '{nome}' cadastrado com sucesso!\n")
    except Exception as erro:
        print(f"Erro ao cadastrar usuário: {erro}")

# Função que tenta abrir frutas.txt, e cria caso não exista
def carregar_ou_criar_arquivo():
    try:
        with open("frutas.txt", "r", encoding="utf-8") as arquivo:
            frutas = [linha.strip() for linha in arquivo]
            print("Frutas carregadas do arquivo com sucesso!\n")
    except FileNotFoundError:
        print("Arquivo 'frutas.txt' não encontrado. Criando novo arquivo...")
        frutas = ["Maçã", "Banana", "Laranja", "Manga", "Melancia", "Pera"]
        with open("frutas.txt", "w", encoding="utf-8") as arquivo:
            for fruta in frutas:
                arquivo.write(fruta + "\n")
        print("Arquivo 'frutas.txt' criado com as frutas iniciais!\n")
    return frutas

# Função para adicionar frutas ao final do arquivo
def adicionar_frutas_extra():
    novas_frutas = ["Uva", "Abacaxi"]
    try:
        with open("frutas.txt", "a", encoding="utf-8") as arquivo:
            for fruta in novas_frutas:
                arquivo.write(fruta + "\n")
        print("Novas frutas adicionadas com sucesso (Uva e Abacaxi)!\n")
    except Exception as erro:
        print(f"Erro ao adicionar novas frutas: {erro}")

# Função para exibir frutas cadastradas
def mostrar_frutas():
    try:
        with open("frutas.txt", "r", encoding="utf-8") as arquivo:
            frutas = arquivo.readlines()
        print("=== Lista de Frutas Disponíveis ===")
        for fruta in frutas:
            print("-", fruta.strip())
        print()
    except Exception as erro:
        print(f"Erro ao ler frutas: {erro}")

# Programa principal
def main():
    print("=== Bem-vindo à Loja de Frutas ===\n")

    cadastrar_usuario()

    frutas = carregar_ou_criar_arquivo()

    mostrar_frutas()

    adicionar_frutas_extra()

    mostrar_frutas()

# Execução
if __name__ == "__main__":
    main()
