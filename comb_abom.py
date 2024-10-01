import random
from personagens import palatino
from inimigos import goblin_um
from dado_d6 import lancar_dados

def combate(palatino, goblin_um):
    while palatino.vida > 0 and goblin_um.vida > 0:
        dado1, dado2, dado3, dado4 = lancar_dados()

        if (dado1 > goblin_um.escudo or dado2 > goblin_um.escudo or dado3 > goblin_um.escudo or
            (dado1 + dado2 > goblin_um.escudo and (dado1 in (1, 2) or dado2 in (1, 2))) or
            (dado1 + dado3 > goblin_um.escudo and (dado1 in (1, 2) or dado3 in (1, 2))) or
            (dado2 + dado3 > goblin_um.escudo and (dado2 in (1, 2) or dado3 in (1, 2)))):
            goblin_um.vida = 0
            print(f"{palatino.nome} derrotou {goblin_um.nome} com um ataque.")
            break

        

        if goblin_um.vida <= 0:
            print(f"{goblin_um.nome} foi derrotado!")
            break
        
        dado4 = random.randint(1,6)
        print(f"Dado do Goblin: {dado4}")

        if dado4 > palatino.escudo:
            ataque_goblin = 1
            palatino.receber_dano(ataque_goblin)
            print(f"{goblin_um.nome} atacou {palatino.nome} causando {ataque_goblin} de dano.")
        else:
            print(f"{goblin_um.nome} tentou atacar {palatino.nome}, mas falhou!")

        if palatino.vida <= 0:
            print(f"{palatino.nome} foi derrotado!")
            break

combate(palatino, goblin_um)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # ataque_player = lancar_dados()
        # goblin_um.receber_dano(ataque_player)
        # print(f"{palatino.nome} atacou {goblin_um.nome} causando {ataque_player} de dano.")

        # if goblin_um.vida <= 0:
        #     print(f"{goblin_um.nome} foi derrotado!")
        #     break

        # # ataque_inimigo = random.randint(1, inimigo.forca)
        # # player.receber_dano(ataque_inimigo)
        # # print(f"{inimigo.nome} atacou {player.nome} causando {ataque_inimigo} de dano.")

        # # if player.vida <= 0:
        # #     print(f"{player.nome} foi derrotado!")