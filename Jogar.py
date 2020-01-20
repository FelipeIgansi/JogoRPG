# Criando os personagens
from Personagem import Personagem_Class
from random import randrange
import os

def LimparConsole():
    print("\n"*10)

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


while(op < 2):
    print("Escolha uma das opções desejadas:  ")
    print("   1 - Cadastrar personagem")
    print("   2 - Sair")

    op = int(input('Qual é a opção desejada (escolha apenas o numero)?  '))

    if(op == 1):
        LimparConsole()

        nome = input('Qual é o nome do personagem: ')
        vida = input('Quanto de vida o personagem tem:  ')
        mana = input('Quanto de mana o persnagem tem:  ')
        forca = input('Quanto de força o personagem tem:  ')
        defesa = input('Quanto de defesa ele tem:  ')

        ListChars.append([Personagem_Class(nome, vida, mana, forca, defesa)])

        if (len(ListChars) !=  0):

            op1 = 0

            while (op1 < 5):
                print("   1 - Atacar")
                print("   2 - Defender")
                print("   3 - Disparar feitiço")
                print("   4 - Finalizar personagem")
                print("   5 - Sair")

                op1 = int(input('Qual é a opção desejada (escolha apenas o numero)?  '))


                if(op1 == 1):
                    print('Atacar')
                    break
                elif(op1 ==2):
                    print('Defender')
                    break
                elif(op1 == 3):
                    print('Disparar feitiço')
                    break
                elif(op1 == 4):
                    print('Finalizar personagem')
                    break

        else:
            print("Ocorreu um erro!")
'''
    elif(op == 2):

        # Matar personagem

        if (not ListChars):
            LimparConsole()
            print('Personagem ainda não criado!')
            print('Crie-o primeiro.')

        else:
            LimparConsole()
            print('Como diria o grande pensador Sr Omar:')
            print('\n\n - Sr Omar: Tragico!\n\n')

            morte = input('Como o personagem deve morrer?  ')




    elif(op == 3):
        # Atacar

        if (not ListChars):
            LimparConsole()
            print('Personagem ainda não criado!')
            print('Crie-o primeiro.')

        else:
            LimparConsole()





    elif(op == 4):

        # Defender

        if (not ListChars):
            LimparConsole()
            print('Personagem ainda não criado!')
            print('Crie-o primeiro.')

        else:
            LimparConsole()





    elif(op == 5):
        # Disparar feitiço

        if (not ListChars):
            LimparConsole()
            print('Personagem ainda não criado!')
            print('Crie-o primeiro.')

        else:
            LimparConsole()

'''