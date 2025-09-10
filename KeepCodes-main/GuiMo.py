print('Olá, esse código calcula a média de notas de alunos de uma sala.' )

numero_alunos = int(input("Por favor, informe quantos alunos existem na sala: "))

total_nota = 0
for aluno in range (1, numero_alunos + 1):
    nota = int(input(f'Insira a nota do aluno {aluno}: '))
    total_nota = total_nota + nota

    media = float(total_nota / numero_alunos)

    print(f'\nA media é {media: .2f}')