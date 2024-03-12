city = str(input("Qual cidade você nasceu: ")).strip().lower().split()
if (city[0] != "santo"):
    print(False)
else:
    print(True)
