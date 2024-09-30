import random

dado1 = []
dado2 = []
def lancar_dados():
    dado1 = [random.randint(1,6)]
    dado2 = [random.randint(1,6)]
    dado1.append
    dado2.append
    if dado1[0] == 1 or dado1[0] == 2 or dado2[0] == 1 or dado2[0] == 2:
        res = dado1[0] + dado2[0]
        print(f"{res}")
    print(f"{dado1} {dado2}")
     
lancar_dados()
print(dado1)