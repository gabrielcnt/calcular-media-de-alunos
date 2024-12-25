nome = str(input("Digite um nome: ")).strip().title()
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))

def calcular_media():
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 7:
        print(f"A média de {nome} é {media:.1f}, APROVADO(A)")
    else:
        print(f"A média de {nome} é {media:.1f}, REPROVADO(A)")
    
calcular_media()