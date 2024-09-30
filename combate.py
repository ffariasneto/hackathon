from dado_d6 import *

class Combate():

    def __init__(self, forca, habilidade, magia, defesa):
        self.forca = forca
        self.habilidade = habilidade
        self.magia = magia
        self.defesa = defesa

    def forca(self):
        lancar_dados()


'''
Herói 1 - Sir Lanon (Paladino Humano) - Escudo = 5 - Força - 3 Dados - Agilidade - 1 Dado - Inteligencia 2 Dados - 8 Vida - 5 Energia
Herói 2 - Ethairna (Feiticeira Elfa) - Escudo = 3 - Força = 1 Dado - Agilidade = 2 Dados - Inteligencia = 3 Dados - 6 Vida - 8 Energia
Herói 3 - Lâmina da Lua (Ladina Elfa da Floresta) - Escudo = 3 - Força = 2 Dados - Agilidade = 3 Dados - Inteligencia = 1 Dado - 6 Vida - 5 Energia

Coisa Gelatinosa - Escudo - 4 - Força = 3 - 8 Vida
Aranha Gigante - Escudo - 5 - Força = 3 - 7 Vida
Goblin Atirador - Escudo - 5 - Força = 1 - 1 Vida
Goblin Esfaqueador - Escudo - 4 - Força = 1 - 1 Vida
Goblin Poderoso - Escudo 7 - Força = 1 - 1 Vida
Goblin Explosivo - Escudo 4 - Força =1 - 1 Vida
'''