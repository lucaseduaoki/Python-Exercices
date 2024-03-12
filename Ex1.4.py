temperatura = float(input('Informe a temperatura em °C: '))
f = (temperatura * 9/5) + 32 
k = (temperatura + 273.15)
print(f'A temeratura de {temperatura}°C corresponde á {f:.1f}°F')
print(f'A temperatura de {temperatura}°C corresponde á {k:.1f}°K')

