import random
import time

print("\033[33m-=\033[m" * 35)
print("\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m")
print("\033[33m-=\033[m" * 35)
numComp = random.randint(0, 5)
num = int(input("Em que número eu pensei: "))

print("\033[35mPROCESSANDO...\033[m")
time.sleep(0.3)

if num == numComp:
    print("\033[33mParabéns!! Você conseguiu me vencer.\033[m")
else:
    print(f"\033[31mPoxa,você perdeu. Eu pensei no número {numComp} e não no {num}.\033[m")
