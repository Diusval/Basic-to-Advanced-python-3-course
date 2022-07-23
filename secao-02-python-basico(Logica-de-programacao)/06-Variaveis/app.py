"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = "Diusval Pinheiro" # str
idade = 20 # int
altura = 1.80 #float
e_maior = idade >= 18 # bool
peso = 80
imc = peso / (altura * altura)

"""
print("Nome:" ,nome)
print("Idade:", idade)
print("Altura", altura)
print("É maior de idade:", e_maior)
"""

print("%s tem %d anos de idade e seu Imc é de %d." % (nome, idade, imc))