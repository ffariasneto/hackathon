from dado_d6 import lancar_dados

class Inimigos():
    def __init__(self, nome, vida, escudo, forca):
        self.nome = nome
        self.vida = vida
        self.escudo = escudo
        self.forca = forca

       
    def ficha_inimigo(self):
        return (f'''
Nome: {self.nome}
Vida: {self.vida}
Escudo: {self.escudo}
Força: {self.forca}
            ''')

    def receber_dano(self, dano):
        dado1, dado2, dado3 = lancar_dados()

        if self.escudo < dado1[0] or self.escudo < dado2[0] or self.escudo < dado3[0]:
            self.vida -= dano
            print(f"{self.nome} recebeu {dano} de dano! Vida Atual: {self.vida}")
        else:
            print(f"{self.nome} bloqueou o dano! Escudo: {self.escudo}, Dado Inimigo: {dado4}")


mestre_um = Inimigos(nome="Coisa Gelatinona",vida=8,escudo=4,forca=3)
mestre_dois = Inimigos(nome="Aranha Gigante",vida=7,escudo=5,forca=3)

goblin_um = Inimigos(nome="Goblin Atirador",vida=1,escudo=6,forca=1)
goblin_dois = Inimigos(nome="Goblin Esfaqueador",vida=1,escudo=4,forca=1)
goblin_tres = Inimigos(nome="Goblin Poderoso",vida=1,escudo=7,forca=1)
goblin_quatro = Inimigos(nome="Goblin Explosivo",vida=1,escudo=4,forca=1)