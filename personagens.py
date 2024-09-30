from dado_d6 import lancar_dados

class Personagem():
    def __init__(self, nome, vida, energia, escudo, forca, agilidade, inteligencia):
        self.nome = nome
        self.vida = vida
        self.energia = energia
        self.escudo = escudo
        self.forca = forca
        self.agilidade = agilidade
        self.inteligencia = inteligencia

       
    def ficha_person(self):
        return (f'''
Nome: {self.nome}
Vida: {self.vida}
Energia: {self.energia}
Escudo: {self.escudo}
Força: {self.forca}
Agilidade: {self.agilidade}
Inteligência: {self.inteligencia}
            ''')
    
    def receber_dano(self, dano):
        dado4 = lancar_dados()

        if self.escudo < dado4:
            self.vida -= dano
            print(f"{self.nome} recebeu {dano} de dano! Vida Atual: {self.vida}")
        else:
            print(f"{self.nome} bloqueou o dano! Escudo: {self.escudo}, Dado Inimido: {dado4}")


palatino = Personagem(nome="SirLanon",vida=8,energia=5,escudo=5,forca=3,agilidade=1,inteligencia=2)
feiticeira = Personagem(nome="Ethairna",vida=6,energia=8,escudo=3,forca=1,agilidade=2,inteligencia=3)
ladina = Personagem(nome="Lâmina da Lua",vida=6,energia=5,escudo=3,forca=2,agilidade=3,inteligencia=1)