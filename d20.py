import random

def rolar_d20():
    return random.randint(1,20)

resultado = rolar_d20()
if resultado >= 14:
    print("Ação bem sucedida")

else:
    print("Ação falhou!")