# Criando os personagens

from Personagem import Personagem_Class
from random import randrange

ListChars = []
op = 0
for i in range(5):
    #nome = input('Qual é o nome do personagem?   ')
    nome = "Personagem "+str(randrange(0,100))
    vida = randrange(0, 101)
    mana = randrange(500, 1500)
    forca = randrange(500, 1500)
    defesa = randrange(500, 1500)

    ListChars.append([Personagem_Class(nome, vida, mana, forca, defesa)])


while(op < 6):
    print("Escolha uma das opções desejadas:  ")
    print("   1 - Cadastrar personagem")
    print("   2 - Matar personagem")
    print("   3 - Atacar")
    print("   4 - Defender")
    print("   5 - Disparar feitiço")
    print("   6 - Sair")

    op = int(input('Qual é a opção desejada (escolha apenas o numero)?  '))

    if(op == 1):

        # Cadastro
        nome = input('Qual é o nome do personagem: ')
        vida = input('Quanto de vida o personagem tem:  ')
        mana = input('Quanto de mana o persnagem tem:  ')
        forca = input('Quanto de força o personagem tem:  ')
        defesa = input('Quanto de defesa ele tem:  ')

        ListChars.append([Personagem_Class(nome, vida, mana, forca, defesa)])

    elif(op == 2):

        #Matar personagem

        pass
    elif(op == 3):

        #Atacar

        pass
    elif(op == 4):

        #Defender

        pass
    elif(op == 5):

        #Disparar feitiço

        pass