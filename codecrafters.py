person = '''

    1. Guerreiro
    2. Mago
    3. Arqueiro
    4. Sair

'''
print("Escolha sua classe:")

print(person)

main = True
while main == True:
    escolha = input(": -> ")
    if escolha == "1":
        print("Você escolheu Guerreiro")
    elif escolha == "2":
        print("Você escolheu o Mago!")
    elif escolha == "3":
        print("Você escolheu o Arqueiro!")
    elif escolha == "4":
        main == False
        break
