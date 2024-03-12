from time import sleep
name = str(input('Digite o seu nome completo: ')).strip()
print("Analisando seu nome")
sleep(0.3)
print(f"Seu nome em maiúsculo é {name.upper()}")
print(f'Seu nome em minúsculo é {name.lower()}')
print(f"Seu nome tem ao todo {len(name) - name.count(' ')} caracteres")
separa = name.split()
print(f"Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras")
