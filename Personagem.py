from random import randrange

class Personagem_Class:
    def __init__(self, nome, vida, mana, forca, defesa):
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



    def CalculaDano(self,level, forca, defesa):
        return ((((2 * level / 5 + 2) * forca / defesa) / 50) + 2)

    def Ataca(self, vida, level, forca, defesa):

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