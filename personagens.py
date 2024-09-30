class Personagem():
    def __init__(self,nome, forca, vida, defesa):
        self.nome = nome
        self.forca = forca
        self.vida = vida
        self.defesa = defesa

       
    def ficha_person(self):
        return (f'''
            Nome: {self.nome}
            Vida: {self.vida}
            Força: {self.forca}
            Defesa: {self.defesa}
            ''')
    
    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0



guerreiro = Personagem(nome="Cassius", forca=50, vida=100, defesa=50)
necro = Personagem(nome="Necromante", forca=30, vida=150, defesa=60)
abominacao = Personagem(nome="Abominação", forca=6, vida=50, defesa=10)