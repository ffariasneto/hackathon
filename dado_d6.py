import random

def lancar_dados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    dado3 = random.randint(1,6)
    dado4 = random.randint(1,6)
    dados = []
    dados.append(dado1)
    dados.append(dado2)
    dados.append(dado3)
    maior_valor = max(dados)
    soma_adic = sum(dado for dado in dados if dado == 1 or dado == 2)
    res = maior_valor + soma_adic
    print(f"{res}")
    print(dados)
    print(f"Dados Rolados: {dado1}, {dado2}, {dado3}, Dado4 (ataque): {dado4}")
    return dado1, dado2, dado3, dado4

# lancar_dados()