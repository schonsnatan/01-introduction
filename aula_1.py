'''
val1 = int(input("Digite um valor: ")) #casting
val2 = int(input("Digite outro valor: ")) 
print(val1+val2)

nome = input("Qual seu nome: ")
tam = len(nome)
print(tam)
'''
# Desafio

CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome

nome = input("Digite seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

sal = float(input("Informe seu salario: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

bonus = float(input("Digite o seu bonus: "))

# 4) Calcule o valor do bônus final

val_final = CONSTANTE_BONUS + sal * bonus

# 5) Imprima cálculo do KPI para o usuário

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

print(f"Olá {nome}, seu bônus é de {val_final}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
