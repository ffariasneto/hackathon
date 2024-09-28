import random
import personagens

def combate(player, inimigo):
    while player.vida > 0 and inimigo.vida > 0:
        ataque_player = random.randint(1, player.forca)
        inimigo.receber_dano(ataque_player)
        print(f"{player.nome} atacou {inimigo.nome} causando {ataque_player} de dano.")

        if inimigo.vida <= 0:
            print(f"{inimigo.nome} foi derrotado!")
            break

        ataque_inimigo = random.randint(1, inimigo.forca)
        player.receber_dano(ataque_inimigo)
        print(f"{inimigo.nome} atacou {player.nome} causando {ataque_inimigo} de dano.")

        if player.vida <= 0:
            print(f"{player.nome} foi derrotado!")

# Exemplo de uso:
player = Personagem("Heroi", 10, 50, 5)
inimigo = Personagem("Monstro", 8, 30, 3)
combate(player, inimigo)
