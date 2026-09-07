# Programa para calcular a média de um aluno
print()
print("=== SISTEMA DE NOTAS ===")
print()

# Entrada de dados

nome = input("Digite o nome do aluno: ")
disciplina = input("Digite o nome da disciplina: ")

av1 = float(input("Digite a nota da AV1: "))
av2 = float(input("Digite a nota da AV2: "))

#Cálculo da média

media = (av1 + av2) / 2

# Verificação da situação

if media >=7:
    situacao = "APROVADO"
elif media >= 4:
    situacao = "PROVA FINAL"
else:
    situacao = "REPROVADO"

# Exibição dos resultados

print()
print("=== RESULTADO ===")
print(f"Aluno: {nome}")
print(f"Disciplina: {disciplina}")
print(f"Nota AV1: {av1:.2f}")
print(f"Nota AV2: {av2:.2f}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")