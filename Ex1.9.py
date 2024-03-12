import random

n1 = str(input("Qual o seu nome: "))
n2 = str(input("Qual o seu nome: "))
n3 = str(input("Qual o seu nome: "))
n4 = str(input("Qual o seu nome: "))
lista = [n1, n2, n3, n4]

sort = random.choice(lista)
print(f"O nome sorteado foi {sort}")
