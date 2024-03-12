name = str(input("Qual seu nome: ")).lower().strip()
print(f"Seu nome tem Silva?", end=" ")
if "silva" in name:
    print(True)
else:
    print(False)
