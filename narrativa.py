from personagens import *
from comb_abom import *



start = '''
Um pandemônio surgiu no reino de Terra Alta. Um mago chamado Camus, especializado na magia da necromancia,
criou um exército de zumbis que infestou a cidade e seus arredores.
À medida que a praga zumbi se espalhava por todo o reino, um guerreiro surgiu, chamado Cassius e está disposto a acabar com esse mal.
Camus pratica sua magia negra do alto do seu castelo Darkskull, situado em Oceandell, à 50km de Terra Alta. Lá ele controla seu exército maligno.
Cassius, a fim de devolver paz ao reino e aproveitando-se da brecha (a legião de zumbis estava na cidade), 
armou-se com sua espada (apelidada de Ferroada), uma armadura completa e um escudo. Montado em seu cavalo Tormenta, partiu em direção
ao seu destino: o terceiro andar do Castelo Darkskull.

Evento 1

Após 5 horas, Cassius chegou à porta de Darkskull. A porta estava guardada por dois zumbis Abominação. Com uma fúria visível em seus olhos, Cassius começaria sua primeira batalha...
'''
print(start)
combate(guerreiro, abominacao)

event_2 = '''

Evento 2

Os zumbis Abominação foram derrotados. Coberto de sangue por causa da batalha feroz que ocorrera, Cassius seguiu em sua jornada ao entrar no castelo.
O saguão estava vazio. Ele enxerga uma porta e uma escada..
'''
print(f"{event_2}\n")

print('''O que você quer fazer: 
    
        Abrir a porta ou
        
        Subir as escadas?\n''')
esc1 = input("Digite porta ou escadas: ")
if esc1 == "porta":
    print("Cassius encontrou um salão aparentemente vazio...")
    print("Deseja vasculhar o ambiente? ")
    esc2 = input("Digite sim ou não: ")
    if esc2 == "sim":
        print("Você encontrou um baú.")
        print("Neste baú, Cassius usa a espada para quebrar o cadeado e encontra uma poção de cura")
        guerreiro.vida = 100
    else:
        print("Você sai e vai em direção as escadas.")
print("Ao chegar nas escadas, Cassius avista um lobo zumbi e parte para uma nova batalha:")
combate(guerreiro, lobo_zumbi)

event_3 = '''

Evento 3

Após a batalha excruciante, Cassius vasculhou o andar e não encontrou maiores desafios. Partiu logo em direção à próxima escadaria e subiu até o segundo andar.
Ao chegar ao topo da escadaria, Cassius se deparou com uma porta repleta de símbolos estranhos. Ao tentar abrir a porta pela maçaneta não aconteceu nada. 
Cassius notou que existia uma chave inserida na fechadura com setas para direita e para esquerda.
'''
print('''Você decide girar a chave:
    
        Esquerda ou Direita?

    ''')
esc3 = input(": -> ")
if esc3 == "esquerda":
    print("Cassius girou a chave para a esquerda. Sentiu uma dor lancinante no braço. Espinhos saíram da porta e perfuraram seu braço. Recebe 30 de dano.")
    guerreiro.vida -= 30
else:
    print("Cassius girou a chave para a direita. Ouviu um clique e ao empurrar a porta ela se abriu normalmente. O herói adentrou na próxima sala.")

event_4 = '''
Evento 4

A jornada de Cassius estava próximo ao fim. Após passar pela porta assustadora, ele viu uma sala ampla do outro lado e mais uma escadaria que, 
pelos seus cálculos, chegaria ao topo do castelo.
Ao subir cada degrau, Cassius ouvia conjurações proferidas com uma voz gutural de Camus. Todo aquele terror estaria para terminar.
No fim da escadaria, Cassius viu seu algoz diante dele. Verificou um portal verde em cima de Camus e Cassius partiu pra cima do necromante.
Camus percebeu o sorrateiro ataque que estava por vir e conseguiu lançar um feitiço... 

'''
print(event_4)
print("Cassius ficou desnorteado...")
print("Com a visão ainda turva, Cassius encontra uma poção mágica que recupera e aumenta a força.")
guerreiro.vida = 100
guerreiro.forca = 60
print("A Batalha final inicia...")
combate(guerreiro, necromante)
if guerreiro.vida == 0:
    print("Fim de Jogo!")
else:
    print("Cassius derrotou Camus e restaurou a paz em Terra Alta.")



