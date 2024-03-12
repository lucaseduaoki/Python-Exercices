km = int(input("Qual a velocidade atual do carro: "))
if km > 80:
    multa = (km - 80) * 7
    print("\033[31mMULTADO! Você excedeu o limite permitido.\033[m")
    print(f"\033[31mVocê deve pagar uma multa de \033[m\033[33mR${multa}\033[m")
print("\033[32mTenha um bom dia. Dirija com segurança!\033[m")
