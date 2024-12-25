import pandas as pd

#Lista vazia de alunos
alunos = []

while True:
    nome = str(input("Digite um nome: ")).strip().title()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4
    situacao = "APROVADO(A)" if media >= 7 else "REPROVADO(A)"

#guardar dados dos alunos em um dicionario

    aluno = {
        "nome": nome,
        "media": media,
        "situacao": situacao
    }

    #adiciona aluno a lista
    alunos.append(aluno)

    # pergunta se quer continuar:
    continuar = input("\nQuer adicionar outro aluno ? (S/N): ").upper()
    if continuar != 'S':
        break

tabela_alunos = pd.DataFrame(alunos)
