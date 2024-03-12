valor = float(input("Qual o seu salário: R$"))
if valor > 1250:
    aumento = (0.10 * valor) + valor
elif valor <= 1250:
    aumento = (0.15 * valor) + valor
print(f"Quem ganhava R${valor:.2f} passará a ganhar R${aumento:.2f}")
