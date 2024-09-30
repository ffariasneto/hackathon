from dado_d6 import *

class Combate():

    def __init__(self, forca, habilidade, magia, defesa):
        self.forca = forca
        self.habilidade = habilidade
        self.magia = magia
        self.defesa = defesa

    def forca(self):
        lancar_dados()
