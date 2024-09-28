class Zumbi():
    
    def __init__(self, nome, forca, vida, inteligencia):
        self.nome = nome
        self.forca = forca
        self.vida = vida
        self.inteligencia = inteligencia
    
    def ficha_zumbi(self):
        return f'''
              
              Nome: {self.nome}
              Força: {self.forca}
              Vida: {self.vida}
              Inteligencia: {self.inteligencia}

              '''

necro = Zumbi(nome="Necromante", forca=30, vida=150, inteligencia=60)
print(necro.ficha_zumbi())
