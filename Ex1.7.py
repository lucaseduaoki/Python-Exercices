from math import hypot
co = float(input("Comprimento do Cateto Oposto: "))
ca = float(input("Comprimento do Cateto Adjacente: "))
hy = hypot(co, ca)
print(f"A hipotenusa vai medir {hy:.2f}")
