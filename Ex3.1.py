km = int(input("Informe a distância da viagem: "))
print(f"Você está prestes a fazer uma viagem de {km}km.")
if km <= 200 and km > 0:
    valor = km * 0.50
else:
    valor = km * 0.45
print(f'E o preço de sua passagem será R${valor}')
