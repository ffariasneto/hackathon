class Personagem():
    def __init__(self,nome, forca, vida, inteligencia):
        self.nome = nome
        self.forca = forca
        self.vida = vida
        self.inteligencia = inteligencia

       
    def ficha_person(self):
        return (f'''
            Nome: {self.nome}
            Vida: {self.vida}
            Força: {self.forca}
            Inteligência: {self.inteligencia}
            ''')
    
    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0

guerreiro = Personagem(nome="Cassius", forca=50, vida=100, inteligencia=50)
necro = Personagem(nome="Necromante", forca=30, vida=150, inteligencia=60)
abominacao = Personagem(nome="Abominação", forca=6, vida=50, inteligencia=10)