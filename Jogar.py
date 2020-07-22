# Criando os personagens
from ConstroiTela import *
from Personagem import Personagem_Class


def LimparConsole():
    print("\n" * 10)


ListChars = []

op = 0

while 2 > op >= 0:
    LimparConsole()
    # Exibe a mensagem incial
    TelaPrincipal()
    print('')
    opcao = input('O que você deseja fazer?  ')
    if opcao == '1' or opcao == 'cadastrar'.lower() in opcao.lower():

        # Limpa o console
        LimparConsole()

        nome = input('Qual é o nome do personagem: ')
        vida = input('Quanto de vida o personagem tem:  ')
        mana = input('Quanto de mana o persnagem tem:  ')
        forca = input('Quanto de força o personagem tem:  ')
        defesa = input('Quanto de defesa ele tem:  ')

        ListChars.append([Personagem_Class(nome, vida, mana, forca, defesa)])

        print(ListChars)

        if len(ListChars[0].count()) != 0:

            op1 = 0

            while op1 < 5:
                MenuAcoes()

                op1 = int(input('Qual é a opção desejada (escolha apenas o numero)?  '))

                if op1 == 1:
                    print('Atacar')
                    break
                elif op1 == 2:
                    print('Defender')
                    break
                elif op1 == 3:
                    print('Disparar feitiço')
                    break
                elif op1 == 4:
                    print('Finalizar personagem')
                    break

        else:
            print("Ocorreu um erro!")
