salario = float(input("Digite o valor do seu salário: R$ "))
porcentagem = float(input("Digite o valor do aumento em porcentagem: "))
aumento = salario + (salario*porcentagem/100)
print(f"O salário inicial era de {salario} e agora com o aumento de {porcentagem} é {aumento}.")
