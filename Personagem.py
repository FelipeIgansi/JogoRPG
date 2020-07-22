from random import randrange

class Personagem_Class:
    def __init__(self, nome = 0, vida =  0, mana = 0, forca = 0, defesa = 0):
        self.nome = nome
        self.vida = vida
        self.mana = mana
        self.forca = forca
        self.defesa = defesa



    def MostrarVida(self, hp = 100):
        if (hp == 100):
            return "|{}| - {}%".format("█"*10, hp)
            #print("|." + "█." * 10 + "|" + " - "+ str(hp)+ "%")

        elif (hp < 100 and hp > 0):
            diferenca = 100 - hp
            return "|{}{}| - {}%".format("█"*(hp//10), "_"*(diferenca//10), hp)
            #print("|." + "█." * (hp // 10) + "_." * (diferenca // 10) + "|" + " - "+ str(hp)+ "%")

        elif (hp == 0):
            return "|{}| - {}%".format("_"*10, hp)
            #print("|." + "_." * 10 + "|" + " - "+ str(hp)+ "%")



    def CalculaDano(self,level = 0, forca = 0, defesa = 0):

        if level == 0 or forca == 0 or defesa == 0:
            print('Ocorreu um erro. \nÉ necessário que os atributos do personagem sejam maiores que zero. \nVaores:\nLevel {} \nForça {} \nDefesa {}'.format(level, forca, defesa))

        else:
            return ((((2 * level / 5 + 2) * forca / defesa) / 50) + 2)

    def Ataca(self, vida = 0, level = 0, forca = 0, defesa = 0):

        if (self.forca > self.defesa):
            dano = Personagem_Class.CalculaDano(level, forca, defesa)

        elif (forca == defesa):
            acerto = randrange(0, 2)

            if (acerto == 0):
                print("O inimigo bloqueou!")

            elif (acerto == 1):
                dano = Personagem_Class.CalculaDano(level, forca, defesa)

        else:
            print("O inimigo bloqueou! ")

        dano = Personagem_Class.CalculaDano(level, forca, defesa)
        if (dano < vida):
            vida = vida - dano
        elif (dano == vida):
            print('Game Over!')
        else:
            print('ocorreu um problema!')
        return vida