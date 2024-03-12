n = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
n3 = int(input("Digite um valor: "))

maior = n
if n2 > n and n2 > n3:
    maior = n2
elif n3 > n and n3 > n2:
    maior = n3
print(f"O maior número é o {maior}")
