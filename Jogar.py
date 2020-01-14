# Criando os personagens

from Personagem import Personagem_Class
from random import randrange

p1 = Personagem_Class('Gerald', 1000, 356, 689, 521)
ListChars = []

for i in range(100):
    #nome = input('Qual é o nome do personagem?   ')
    nome = "Personagem "+str(randrange(0,100))
    vida = randrange(0, 101)
    print('O valor de vida do personagem é:  ', vida)
    mana = randrange(500, 1500)
    print('O valor de mana do personagem é:  ', mana)
    forca = randrange(500, 1500)
    print('O valor de força do personagem é:  ', forca)
    defesa = randrange(500, 1500)
    print('O valor de defesa do personagem é:  ', defesa)
    print('\n\n')

    ListChars.append([Personagem_Class(nome, vida, mana, forca, defesa)])

for lista in ListChars:
    for col in lista:
        print("Nome:  ", col.nome)
        hp = col.MostrarVida(col.vida)
        print("HP:  ", hp)
        print("Mana:  ", col.mana)
        print("Força:  ", col.forca)
        print("Defesa:  ", col.defesa, "\n\n")
