print('-=' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    decisao = 'PODEM'
else:
    decisao = 'NÃO PODEM'
print(f'As retas {r1:.0f}, {r2:.0f}, e {r3:.0f} {decisao} formar um triângulo')
