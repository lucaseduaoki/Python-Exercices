frase = str(input("Digite uma frase: ")).lower().strip()
letraA = frase.count("a")
posA = frase.find("a")
posA2 = frase.rfind("a")
print(f"A letra A aparece {letraA} vezes")
print(f"A letra A aparece pela primeira vez na posição {posA+1}")
print(f"A letra A aparece pela última vez na posição {posA2}")

